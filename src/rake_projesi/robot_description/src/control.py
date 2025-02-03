#!/usr/bin/env python3

import rospy
import numpy as np
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState

class SimpleController(object):
    def __init__(self, wheel_radius, wheel_separation):
        # Robot tekerlek yarıçapı ve tekerlekler arası mesafe
        self.wheel_radius_ = wheel_radius
        self.wheel_separation_ = wheel_separation

        # Publishers
        self.left_cmd_pub_ = rospy.Publisher("/wheel_left_controller/command", Float64, queue_size=10)
        self.right_cmd_pub_ = rospy.Publisher("/wheel_right_controller/command", Float64, queue_size=10)
        self.joint_state_pub_ = rospy.Publisher("/joint_states", JointState, queue_size=10)

        # Velocity Subscriber
        self.vel_sub_ = rospy.Subscriber("/bumperbot_controller/cmd_vel", Twist, self.velCallback)

        # JointState message
        self.joint_state_msg_ = JointState()
        self.joint_state_msg_.name = ["wheel_left_joint", "wheel_right_joint"]
        self.joint_state_msg_.position = [0.0, 0.0]  # Başlangıç pozisyonları
        self.joint_state_msg_.velocity = [0.0, 0.0]  # Başlangıç hızları
        self.joint_state_msg_.effort = [0.0, 0.0]    # Başlangıç kuvveti

    def velCallback(self, msg):
        """
        Gelen cmd_vel mesajını alıp, kinematik modelle wheel hızlarını hesaplar.
        """
        linear_velocity = msg.linear.x
        angular_velocity = msg.angular.z

        # Kinematik dönüşüm (differential drive model)
        wheel_speed = np.array([[linear_velocity], [angular_velocity]])
        conversion_matrix = np.array([
            [self.wheel_radius_ / 2, self.wheel_radius_ / 2],  # Tekerlek hızları
            [self.wheel_radius_ / self.wheel_separation_, -self.wheel_radius_ / self.wheel_separation_]
        ])

        # Wheel hızlarını hesapla
        wheel_velocities = np.matmul(conversion_matrix, wheel_speed)
        left_wheel_speed = wheel_velocities[1, 0]
        right_wheel_speed = wheel_velocities[0, 0]

        # Tekerlek hızlarını yayınla
        self.left_cmd_pub_.publish(Float64(left_wheel_speed))
        self.right_cmd_pub_.publish(Float64(right_wheel_speed))

        # JointState mesajını güncelle
        self.joint_state_msg_.header.stamp = rospy.Time.now()
        self.joint_state_msg_.velocity = [left_wheel_speed, right_wheel_speed]

        # JointState mesajını yayınla
        self.joint_state_pub_.publish(self.joint_state_msg_)


if __name__ == "__main__":
    rospy.init_node("simple_controller")

    # Parametreleri al (varsayılan değerler)
    wheel_radius = rospy.get_param("~wheel_radius", 0.1)  # Örnek: 0.1 m
    wheel_separation = rospy.get_param("~wheel_separation", 0.5)  # Örnek: 0.5 m

    # Controller'ı başlat
    controller = SimpleController(wheel_radius, wheel_separation)

    # ROS'un çalışmaya devam etmesi için
    rospy.spin()