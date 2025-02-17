#!/usr/bin/env python3

import rospy
import message_filters
from sensor_msgs.msg import Image, NavSatFix
from robot_description.msg import WoundedInfo, WoundedInfoArray

class WoundedInfoPublisher:
    def __init__(self):
        rospy.init_node('wounded_info_publisher', anonymous=True)

        # GPS ve görüntü topic'lerine abone ol
        self.image_sub = message_filters.Subscriber("/detection_result", Image)
        self.gps_sub = message_filters.Subscriber("/gps/fix", NavSatFix)

        # İki mesajı zaman eşlemesi ile senkronize et
        self.ts = message_filters.ApproximateTimeSynchronizer([self.image_sub, self.gps_sub], queue_size=10, slop=0.5)
        self.ts.registerCallback(self.callback)

        # WoundedInfoArray mesajını yayınlayacak publisher
        self.pub = rospy.Publisher("/wounded_info_topic", WoundedInfoArray, queue_size=10)

        # Tespit edilen insanların bilgilerini saklamak için liste
        self.wounded_array = WoundedInfoArray()

    def callback(self, image_msg, gps_msg):
        # Yeni WoundedInfo nesnesi oluştur
        wounded_info = WoundedInfo()
        wounded_info.image = image_msg
        wounded_info.location = gps_msg

        # WoundedInfoArray'e ekle
        self.wounded_array.wounded_array.append(wounded_info)

        # Mesajı yayınla
        self.pub.publish(self.wounded_array)
        rospy.loginfo("Yeni yaralı bilgisi yayınlandı. Toplam kayıt: %d", len(self.wounded_array.wounded_array))

if __name__ == '__main__':
    try:
        WoundedInfoPublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass