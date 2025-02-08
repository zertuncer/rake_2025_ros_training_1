#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO
import os
import time
import logging
import shutil

# YOLO çıktılarının görünmemesi için log seviyesini kapatıyoruz
logging.getLogger('ultralytics').setLevel(logging.CRITICAL)

class YoloDetector:
    def __init__(self):
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt')  # Standart nesne tespiti modelini yükle
        self.image_sub = rospy.Subscriber('/bumper_bot/front_camera', Image, self.callback)
        self.detection_pub = rospy.Publisher('/detection_result', Image, queue_size=10)

        # Fotoğrafların kaydedileceği dizin (Windows dizini)
        self.save_folder = "/mnt/c/Users/ros/catkin_ws/src/rake_projesi/robot_description/photos" 
        
        # Klasörü temizle
        self.clean_folder()

        # Klasör yoksa oluştur
        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

        # Kişilerin fotoğraf sayılarını tutacak bir sözlük
        self.person_photos = {}

        # Son fotoğrafın çekildiği zaman
        self.last_photo_time = time.time()

    def clean_folder(self):
        # Eğer dizin varsa, içindekileri temizle
        if os.path.exists(self.save_folder):
            shutil.rmtree(self.save_folder)  # Dizini ve içeriğini sil
        os.makedirs(self.save_folder)  # Yeniden oluştur

    def callback(self, data):
        # ROS mesajını OpenCV formatına çevir
        cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        
        # Nesne tespiti yap
        results = self.model(cv_image)
        
        # Deteksiyonları işleyelim
        boxes = results[0].boxes
        global a
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            label = box.cls[0]
            conf = box.conf[0]
            
            # Güven oranını düşürerek daha fazla tespit yapılmasını sağlıyoruz
            if conf >= 0.75:
                a=1
                label = "INSAN"
                
                # Kişiyi tanımlamak için bounding box koordinatları
                person_id = (int(x1), int(y1), int(x2), int(y2))

                # Kişinin fotoğraf sayısını kontrol et
                if person_id not in self.person_photos:
                    self.person_photos[person_id] = 0  # İlk fotoğraf kaydedilmesi için başlat

                # Eğer kişinin fotoğraf sayısı 5'ten azsa ve yeterince zaman geçmişse fotoğraf kaydet
                current_time = time.time()
                if self.person_photos[person_id] < 5 and (current_time - self.last_photo_time) >= 2:
                    # Fotoğraf kaydetme işlemi
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    image_filename = os.path.join(self.save_folder, f"human_{timestamp}.jpg")
                    success = cv2.imwrite(image_filename, cv_image)  # Fotoğrafı kaydet
                    if success:
                        self.person_photos[person_id] += 1  # Fotoğraf sayısını artır
                        rospy.loginfo(f"Fotoğraf kaydedildi: {image_filename}")
                        
                        # Fotoğraf kaydedildikten sonra zaman kaydını güncelle
                        self.last_photo_time = current_time

                # Nesne etiketini ve çerçeve rengini yeşil yapalım (insan için)
                color = (0, 255, 0)  # Yeşil
            elif 0.75> conf >= 0.6:
                a=2
                label = "TANIMLANIYOR"     
                # Çerçeve rengini sarı yapalım
                color = (0, 255, 255)  # Sarı
            else:
                a=3
                label = "ENGEL"
                # Çerçeve rengini kırmızı yapalım
                color = (0, 0, 255)  # Kırmızı


            # Çerçeveyi çizelim
            cv2.rectangle(cv_image, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            if a==1:
                cv2.putText(cv_image, f'{label} ({conf:.2f})', 
                            (int(x1), int(y1)-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, (255, 0, 0), 2)
            elif a==2:
                cv2.putText(cv_image, f'{label}', 
                            (int(x1), int(y1)-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, (0, 255, 255), 2)
            else:
                cv2.putText(cv_image, f'{label}', 
                            (int(x1), int(y1)-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.5, (0, 0, 255), 2)
                

        # Görüntüyü yeniden yayımlayalım
        detection_result = self.bridge.cv2_to_imgmsg(cv_image, "bgr8")
        self.detection_pub.publish(detection_result)
        
        # Görüntüyü gösterelim
        cv2.imshow("Detection", cv_image)
        cv2.waitKey(1)

if __name__ == '__main__':
    rospy.init_node('yolo_detector', anonymous=True)
    detector = YoloDetector()
    rospy.spin()
