# RAKE Arama Kurtarma Robot Projesi

## Proje Açıklaması

Bu proje, arama kurtarma operasyonları için tasarlanmış bir ROS tabanlı robot sistemidir. Sistemin temel amacı, afet bölgelerinde yaralı kişilerin tespiti ve konumlandırılmasıdır.

## Temel Özellikler

### Donanım Bileşenleri
- **Robot Platformu**: Diferansiyel sürüşlü "bumperbot" mobil robot
- **Sensörler**:
  - Ön monteli kamera (görüntü işleme için)
  - GPS modülü (konum tespiti için)
  - Tekerlek enkoderleri (hareket kontrolü için)

### Yazılım Özellikleri
- **İnsan Tespiti**: YOLOv8 tabanlı gerçek zamanlı insan ve poz tespiti
- **Konum Takibi**: GPS ve odometri verilerinin füzyonu
- **Kontrol Sistemi**: 
  - Manuel kontrol (klavye ile)
  - ROS Control tabanlı motor kontrolü
- **Görüntü İşleme**: 
  - Gerçek zamanlı kamera görüntü işleme
  - Yaralı tespiti ve konumlandırma
  - Image Transport ile optimize edilmiş görüntü iletimi

## Kurulum

### Gereksinimler
- ROS Noetic
- Gazebo Simulator
- Python 3.x
- YOLOv8

### Bağımlılıklar
```bash
# ROS paketleri
- gazebo_ros
- geometry_msgs
- roscpp
- rospy
- std_msgs
- urdf
- xacro
- robot_state_publisher
- image_transport
```

### Kurulum Adımları
1. Catkin workspace oluşturun:
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
```

2. Projeyi klonlayın:
```bash
git clone [proje-repo-url]
```

3. Bağımlılıkları yükleyin:
```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
```

4. Workspace'i derleyin:
```bash
catkin_make
```

## Kullanım

### Simülasyonu Başlatma
```bash
source devel/setup.bash
roslaunch robot_description gazebo.launch
```

### Manuel Kontrol
- Klavye kontrolleri:
  - ↑: İleri hareket
  - ↓: Geri hareket
  - ←: Sola dönüş
  - →: Sağa dönüş
  - Q: Çıkış

### Görselleştirme
- RViz ile robot ve sensör verilerini görüntüleme:
```bash
roslaunch robot_description display.launch
```

## Proje Yapısı

### Ana Bileşenler
- **/src/rake_projesi/robot_description**: Ana robot tanımlamaları ve kontrol kodları
- **/launch**: Çalıştırma dosyaları
- **/urdf**: Robot model tanımlamaları
- **/msg**: Özel mesaj tipleri (WoundedInfo, WoundedInfoArray)
- **/worlds**: Gazebo simülasyon dünyaları

### Önemli Nodlar
1. **keyboard_control_node**: Manuel kontrol arayüzü
2. **yolo_detector_node**: İnsan tespiti ve poz tahmini
3. **wounded_info_publisher**: Yaralı bilgisi yayınlayıcı
4. **image_republisher**: Kamera görüntü işleme

## Lisans
BSD Lisansı altında dağıtılmaktadır.

## İletişim
Geliştirici: Yusuf Zer Tuncer
E-posta: zertuncer@gmail.com
