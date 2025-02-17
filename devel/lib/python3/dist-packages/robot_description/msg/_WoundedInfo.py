# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_description/WoundedInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import std_msgs.msg

class WoundedInfo(genpy.Message):
  _md5sum = "57ede16e4d40ac346b417d6edabd31c3"
  _type = "robot_description/WoundedInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """sensor_msgs/Image Image
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
"""
  __slots__ = ['Image','location']
  _slot_types = ['sensor_msgs/Image','sensor_msgs/NavSatFix']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Image,location

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WoundedInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Image is None:
        self.Image = sensor_msgs.msg.Image()
      if self.location is None:
        self.location = sensor_msgs.msg.NavSatFix()
    else:
      self.Image = sensor_msgs.msg.Image()
      self.location = sensor_msgs.msg.NavSatFix()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.Image.header.seq, _x.Image.header.stamp.secs, _x.Image.header.stamp.nsecs))
      _x = self.Image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.Image.height, _x.Image.width))
      _x = self.Image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.Image.is_bigendian, _x.Image.step))
      _x = self.Image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.location.header.seq, _x.location.header.stamp.secs, _x.location.header.stamp.nsecs))
      _x = self.location.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_bH3d().pack(_x.location.status.status, _x.location.status.service, _x.location.latitude, _x.location.longitude, _x.location.altitude))
      buff.write(_get_struct_9d().pack(*self.location.position_covariance))
      _x = self.location.position_covariance_type
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.Image is None:
        self.Image = sensor_msgs.msg.Image()
      if self.location is None:
        self.location = sensor_msgs.msg.NavSatFix()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.Image.header.seq, _x.Image.header.stamp.secs, _x.Image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Image.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.Image.height, _x.Image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Image.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.Image.is_bigendian, _x.Image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.Image.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.location.header.seq, _x.location.header.stamp.secs, _x.location.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.location.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.location.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 27
      (_x.location.status.status, _x.location.status.service, _x.location.latitude, _x.location.longitude, _x.location.altitude,) = _get_struct_bH3d().unpack(str[start:end])
      start = end
      end += 72
      self.location.position_covariance = _get_struct_9d().unpack(str[start:end])
      start = end
      end += 1
      (self.location.position_covariance_type,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.Image.header.seq, _x.Image.header.stamp.secs, _x.Image.header.stamp.nsecs))
      _x = self.Image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.Image.height, _x.Image.width))
      _x = self.Image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_BI().pack(_x.Image.is_bigendian, _x.Image.step))
      _x = self.Image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.location.header.seq, _x.location.header.stamp.secs, _x.location.header.stamp.nsecs))
      _x = self.location.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_bH3d().pack(_x.location.status.status, _x.location.status.service, _x.location.latitude, _x.location.longitude, _x.location.altitude))
      buff.write(self.location.position_covariance.tostring())
      _x = self.location.position_covariance_type
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.Image is None:
        self.Image = sensor_msgs.msg.Image()
      if self.location is None:
        self.location = sensor_msgs.msg.NavSatFix()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.Image.header.seq, _x.Image.header.stamp.secs, _x.Image.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Image.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.Image.height, _x.Image.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.Image.encoding = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.Image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.Image.is_bigendian, _x.Image.step,) = _get_struct_BI().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.Image.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.location.header.seq, _x.location.header.stamp.secs, _x.location.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.location.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.location.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 27
      (_x.location.status.status, _x.location.status.service, _x.location.latitude, _x.location.longitude, _x.location.altitude,) = _get_struct_bH3d().unpack(str[start:end])
      start = end
      end += 72
      self.location.position_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
      start = end
      end += 1
      (self.location.position_covariance_type,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_9d = None
def _get_struct_9d():
    global _struct_9d
    if _struct_9d is None:
        _struct_9d = struct.Struct("<9d")
    return _struct_9d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_BI = None
def _get_struct_BI():
    global _struct_BI
    if _struct_BI is None:
        _struct_BI = struct.Struct("<BI")
    return _struct_BI
_struct_bH3d = None
def _get_struct_bH3d():
    global _struct_bH3d
    if _struct_bH3d is None:
        _struct_bH3d = struct.Struct("<bH3d")
    return _struct_bH3d
