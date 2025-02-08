;; Auto-generated. Do not edit!


(when (boundp 'robot_description::WoundedInfoArray)
  (if (not (find-package "ROBOT_DESCRIPTION"))
    (make-package "ROBOT_DESCRIPTION"))
  (shadow 'WoundedInfoArray (find-package "ROBOT_DESCRIPTION")))
(unless (find-package "ROBOT_DESCRIPTION::WOUNDEDINFOARRAY")
  (make-package "ROBOT_DESCRIPTION::WOUNDEDINFOARRAY"))

(in-package "ROS")
;;//! \htmlinclude WoundedInfoArray.msg.html


(defclass robot_description::WoundedInfoArray
  :super ros::object
  :slots (_wounded_array ))

(defmethod robot_description::WoundedInfoArray
  (:init
   (&key
    ((:wounded_array __wounded_array) ())
    )
   (send-super :init)
   (setq _wounded_array __wounded_array)
   self)
  (:wounded_array
   (&rest __wounded_array)
   (if (keywordp (car __wounded_array))
       (send* _wounded_array __wounded_array)
     (progn
       (if __wounded_array (setq _wounded_array (car __wounded_array)))
       _wounded_array)))
  (:serialization-length
   ()
   (+
    ;; robot_description/WoundedInfo[] _wounded_array
    (apply #'+ (send-all _wounded_array :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robot_description/WoundedInfo[] _wounded_array
     (write-long (length _wounded_array) s)
     (dolist (elem _wounded_array)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robot_description/WoundedInfo[] _wounded_array
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _wounded_array (let (r) (dotimes (i n) (push (instance robot_description::WoundedInfo :init) r)) r))
     (dolist (elem- _wounded_array)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get robot_description::WoundedInfoArray :md5sum-) "07b0456bba6d17c8cb49b73aee6e6de4")
(setf (get robot_description::WoundedInfoArray :datatype-) "robot_description/WoundedInfoArray")
(setf (get robot_description::WoundedInfoArray :definition-)
      "WoundedInfo[] wounded_array
================================================================================
MSG: robot_description/WoundedInfo
sensor_msgs/Image Image
sensor_msgs/NavSatFix location
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sensor_msgs/NavSatFix
# Navigation Satellite fix for any Global Navigation Satellite System
#
# Specified using the WGS 84 reference ellipsoid

# header.stamp specifies the ROS time for this measurement (the
#        corresponding satellite time may be reported using the
#        sensor_msgs/TimeReference message).
#
# header.frame_id is the frame of reference reported by the satellite
#        receiver, usually the location of the antenna.  This is a
#        Euclidean frame relative to the vehicle, not a reference
#        ellipsoid.
Header header

# satellite fix status information
NavSatStatus status

# Latitude [degrees]. Positive is north of equator; negative is south.
float64 latitude

# Longitude [degrees]. Positive is east of prime meridian; negative is west.
float64 longitude

# Altitude [m]. Positive is above the WGS 84 ellipsoid
# (quiet NaN if no altitude is available).
float64 altitude

# Position covariance [m^2] defined relative to a tangential plane
# through the reported position. The components are East, North, and
# Up (ENU), in row-major order.
#
# Beware: this coordinate system exhibits singularities at the poles.

float64[9] position_covariance

# If the covariance of the fix is known, fill it in completely. If the
# GPS receiver provides the variance of each measurement, put them
# along the diagonal. If only Dilution of Precision is available,
# estimate an approximate covariance from that.

uint8 COVARIANCE_TYPE_UNKNOWN = 0
uint8 COVARIANCE_TYPE_APPROXIMATED = 1
uint8 COVARIANCE_TYPE_DIAGONAL_KNOWN = 2
uint8 COVARIANCE_TYPE_KNOWN = 3

uint8 position_covariance_type

================================================================================
MSG: sensor_msgs/NavSatStatus
# Navigation Satellite fix status for any Global Navigation Satellite System

# Whether to output an augmented fix is determined by both the fix
# type and the last time differential corrections were received.  A
# fix is valid when status >= STATUS_FIX.

int8 STATUS_NO_FIX =  -1        # unable to fix position
int8 STATUS_FIX =      0        # unaugmented fix
int8 STATUS_SBAS_FIX = 1        # with satellite-based augmentation
int8 STATUS_GBAS_FIX = 2        # with ground-based augmentation

int8 status

# Bits defining which Global Navigation Satellite System signals were
# used by the receiver.

uint16 SERVICE_GPS =     1
uint16 SERVICE_GLONASS = 2
uint16 SERVICE_COMPASS = 4      # includes BeiDou.
uint16 SERVICE_GALILEO = 8

uint16 service

")



(provide :robot_description/WoundedInfoArray "07b0456bba6d17c8cb49b73aee6e6de4")


