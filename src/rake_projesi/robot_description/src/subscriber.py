#!/usr/bin/env python3

import rospy
import numpy as np
import math
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from geometry_msgs.msg import TransformStamped
import tf_conversions
from tf2_ros import TransformBroadcaster

class SimpleController(object):
    def __init__(self, wheel_radius, wheel_separation):
        # Initialize the SimpleController
        rospy.loginfo("Using wheel radius %d" % wheel_radius)
        rospy.loginfo("Using wheel separation %d" % wheel_separation)

        self.wheel_radius_ = wheel_radius
        self.wheel_separation_ = wheel_separation
        self.left_wheel_prev_pos_ = 0.0
        self.right_wheel_prev_pos_ = 0.0
        self.x_ = 0.0
        self.y_ = 0.0
        self.theta_ = 0.0

        # Publishers and Subscribers
        self.right_cmd_pub_ = rospy.Publisher("wheel_right_controller/command", Float64, queue_size=10)
        self.left_cmd_pub_ = rospy.Publisher("wheel_left_controller/command", Float64, queue_size=10)
        self.vel_sub_ = rospy.Subscriber("bumperbot_controller/cmd_vel", Twist, self.velCallback)
        self.joint_sub_ = rospy.Subscriber("joint_states", JointState, self.jointCallback)
        self.odom_pub_ = rospy.Publisher("bumperbot_controller/odom", Odometry, queue_size=10)

        # Conversion matrix
        self.speed_conversion_ = np.array([
            [self.wheel_radius_ / 2, self.wheel_radius_ / 2],
            [self.wheel_radius_ / self.wheel_separation_, -self.wheel_radius_ / self.wheel_separation_],
        ])
        rospy.loginfo("The conversion matrix is %s" % self.speed_conversion_)

        # Odometry message initialization
        self.odom_msg_ = Odometry()
        self.odom_msg_.header.frame_id = "odom"
        self.odom_msg_.child_frame_id = "base_footprint"
        self.odom_msg_.twist.twist.linear.y = 0.0
        self.odom_msg_.twist.twist.linear.z = 0.0
        self.odom_msg_.twist.twist.angular.x = 0.0
        self.odom_msg_.twist.twist.angular.y = 0.0
        self.odom_msg_.pose.pose.orientation.x = 0.0
        self.odom_msg_.pose.pose.orientation.y = 0.0
        self.odom_msg_.pose.pose.orientation.z = 0.0
        self.odom_msg_.pose.pose.orientation.w = 1.0

        # TF message initialization
        self.br_ = TransformBroadcaster()
        self.transform_stamped_ = TransformStamped()
        self.transform_stamped_.header.frame_id = "odom"
        self.transform_stamped_.child_frame_id = "base_footprint"
        self.transform_stamped_.transform.translation.z = 0.0

        self.prev_time_ = rospy.Time.now()

    def velCallback(self, msg):
        """
        Callback function for velocity command. 
        Implements the differential kinematic model to calculate wheel speeds
        from linear and angular velocities.
        """
        robot_speed = np.array([[msg.linear.x], [msg.angular.z]])
        wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion_), robot_speed)
        right_speed = Float64(wheel_speed[0, 0])
        left_speed = Float64(wheel_speed[1, 0])

        # Publish the wheel speeds
        self.right_cmd_pub_.publish(right_speed)
        self.left_cmd_pub_.publish(left_speed)

    def jointCallback(self, msg):
        """
        Callback function for joint states. 
        Implements the inverse differential kinematic model to calculate robot's position and orientation.
        """
        if not msg.position:
            rospy.logwarn("Received empty joint position data!")
            return  # Boş veri geldiğinde fonksiyonu sonlandırıyoruz.

        dp_left = msg.position[0] - self.left_wheel_prev_pos_
        dp_right = msg.position[1] - self.right_wheel_prev_pos_
        dt = (msg.header.stamp - self.prev_time_).to_sec()

        # Update previous wheel positions and time
        self.left_wheel_prev_pos_ = msg.position[0]
        self.right_wheel_prev_pos_ = msg.position[1]
        self.prev_time_ = msg.header.stamp

        # Calculate rotational speeds of each wheel
        fi_left = dp_left / dt
        fi_right = dp_right / dt

        # Calculate the robot's linear and angular velocity
        linear = (self.wheel_radius_ * fi_right + self.wheel_radius_ * fi_left) / 2
        angular = (self.wheel_radius_ * fi_right - self.wheel_radius_ * fi_left) / self.wheel_separation_

        # Calculate the position increment
        d_s = (self.wheel_radius_ * dp_right + self.wheel_radius_ * dp_left) / 2
        d_theta = (self.wheel_radius_ * dp_right - self.wheel_radius_ * dp_left) / self.wheel_separation_

        # Update the robot's position and orientation
        self.theta_ += d_theta
        self.x_ += d_s * math.cos(self.theta_)
        self.y_ += d_s * math.sin(self.theta_)

        # Compose and publish the odometry message
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, self.theta_)
        self.odom_msg_.header.stamp = rospy.Time.now()
        self.odom_msg_.pose.pose.position.x = self.x_
        self.odom_msg_.pose.pose.position.y = self.y_
        self.odom_msg_.pose.pose.orientation.x = q[0]
        self.odom_msg_.pose.pose.orientation.y = q[1]
        self.odom_msg_.pose.pose.orientation.z = q[2]
        self.odom_msg_.pose.pose.orientation.w = q[3]
        self.odom_msg_.twist.twist.linear.x = linear
        self.odom_msg_.twist.twist.angular.z = angular

        # Publish the odometry
        self.odom_pub_.publish(self.odom_msg_)

        # Publish the TF transform
        self.transform_stamped_.transform.translation.x = self.x_
        self.transform_stamped_.transform.translation.y = self.y_
        self.transform_stamped_.transform.rotation.x = q[0]
        self.transform_stamped_.transform.rotation.y = q[1]
        self.transform_stamped_.transform.rotation.z = q[2]
        self.transform_stamped_.transform.rotation.w = q[3]
        self.transform_stamped_.header.stamp = rospy.Time.now()
        self.br_.sendTransform(self.transform_stamped_)

    # rospy.loginfo(f"fi_left: {fi_left}, fi_right: {fi_right}")
    # rospy.loginfo(f"fi_left: {fi_left}, fi_right: {fi_right}")
    # rospy.loginfo(f"fi_left: {fi_left}, fi_right: {fi_right}")
    # rospy.loginfo(f"fi_left: {fi_left}, fi_right: {fi_right}")
    # rospy.loginfo(f"fi_left: {fi_left}, fi_right: {fi_right}")


if __name__ == "__main__":
    rospy.init_node("simple_controller")
    wheel_radius = rospy.get_param("~wheel_radius", 0.1)  # Varsayılan değer: 0.1
    wheel_separation = rospy.get_param("~wheel_separation", 0.5)  # Varsayılan değer: 0.5
    controller = SimpleController(wheel_radius, wheel_separation)
    rospy.spin()