#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import curses

def keyboard_control():
    rospy.init_node('keyboard_control_node', anonymous=False)
    pub = rospy.Publisher('/bumperbot_controller/cmd_vel', Twist, queue_size=10)  # Değişiklik yapıldı
    rate = rospy.Rate(100)
    move_cmd = Twist()

    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(True)

    stdscr.addstr("Klavye ile robotu yönlendirmek için kullanabileceğiniz tuşlar: \n")
    stdscr.addstr("Yukarı ok -> ileri, Aşağı ok -> geri, Sol ok -> sola, Sağ ok -> sağa, Q -> çıkış\n")
    stdscr.refresh()

    current_linear_speed = 0.0
    current_angular_speed = 0.0
    speed_increment = 0.1

    while not rospy.is_shutdown():
        key = stdscr.getch()

        if key == curses.KEY_UP:
            current_linear_speed = min(current_linear_speed + speed_increment, 0.7)
            current_angular_speed = 0.0
        elif key == curses.KEY_DOWN:
            current_linear_speed = max(current_linear_speed - speed_increment, -0.7)
            current_angular_speed = 0.0
        elif key == curses.KEY_LEFT:
            current_linear_speed = 0.0
            current_angular_speed = 0.4
        elif key == curses.KEY_RIGHT:
            current_linear_speed = 0.0
            current_angular_speed = -0.4
        elif key == ord('q'):
            current_linear_speed = 0.0
            current_angular_speed = 0.0
            stdscr.addstr("Çıkılıyor...\n")
            stdscr.refresh()
            break
        else:
            current_linear_speed = 0.0
            current_angular_speed = 0.0

        move_cmd.linear.x = current_linear_speed
        move_cmd.angular.z = current_angular_speed

        pub.publish(move_cmd)
        rate.sleep()

    curses.endwin()

if __name__ == '__main__':
    try:
        keyboard_control()
    except rospy.ROSInterruptException:
        pass
