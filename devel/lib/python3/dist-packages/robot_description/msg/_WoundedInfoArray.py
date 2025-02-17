# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_description/WoundedInfoArray.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import robot_description.msg
import sensor_msgs.msg
import std_msgs.msg

class WoundedInfoArray(genpy.Message):
  _md5sum = "07b0456bba6d17c8cb49b73aee6e6de4"
  _type = "robot_description/WoundedInfoArray"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """WoundedInfo[] wounded_array
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
"""
  __slots__ = ['wounded_array']
  _slot_types = ['robot_description/WoundedInfo[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       wounded_array

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WoundedInfoArray, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.wounded_array is None:
        self.wounded_array = []
    else:
      self.wounded_array = []

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
      length = len(self.wounded_array)
      buff.write(_struct_I.pack(length))
      for val1 in self.wounded_array:
        _v1 = val1.Image
        _v2 = _v1.header
        _x = _v2.seq
        buff.write(_get_struct_I().pack(_x))
        _v3 = _v2.stamp
        _x = _v3
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v2.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v1
        buff.write(_get_struct_2I().pack(_x.height, _x.width))
        _x = _v1.encoding
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v1
        buff.write(_get_struct_BI().pack(_x.is_bigendian, _x.step))
        _x = _v1.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
        else:
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v4 = val1.location
        _v5 = _v4.header
        _x = _v5.seq
        buff.write(_get_struct_I().pack(_x))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v7 = _v4.status
        _x = _v7
        buff.write(_get_struct_bH().pack(_x.status, _x.service))
        _x = _v4
        buff.write(_get_struct_3d().pack(_x.latitude, _x.longitude, _x.altitude))
        buff.write(_get_struct_9d().pack(*_v4.position_covariance))
        _x = _v4.position_covariance_type
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
      if self.wounded_array is None:
        self.wounded_array = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.wounded_array = []
      for i in range(0, length):
        val1 = robot_description.msg.WoundedInfo()
        _v8 = val1.Image
        _v9 = _v8.header
        start = end
        end += 4
        (_v9.seq,) = _get_struct_I().unpack(str[start:end])
        _v10 = _v9.stamp
        _x = _v10
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v9.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v9.frame_id = str[start:end]
        _x = _v8
        start = end
        end += 8
        (_x.height, _x.width,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v8.encoding = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v8.encoding = str[start:end]
        _x = _v8
        start = end
        end += 5
        (_x.is_bigendian, _x.step,) = _get_struct_BI().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v8.data = str[start:end]
        _v11 = val1.location
        _v12 = _v11.header
        start = end
        end += 4
        (_v12.seq,) = _get_struct_I().unpack(str[start:end])
        _v13 = _v12.stamp
        _x = _v13
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v12.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v12.frame_id = str[start:end]
        _v14 = _v11.status
        _x = _v14
        start = end
        end += 3
        (_x.status, _x.service,) = _get_struct_bH().unpack(str[start:end])
        _x = _v11
        start = end
        end += 24
        (_x.latitude, _x.longitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 72
        _v11.position_covariance = _get_struct_9d().unpack(str[start:end])
        start = end
        end += 1
        (_v11.position_covariance_type,) = _get_struct_B().unpack(str[start:end])
        self.wounded_array.append(val1)
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
      length = len(self.wounded_array)
      buff.write(_struct_I.pack(length))
      for val1 in self.wounded_array:
        _v15 = val1.Image
        _v16 = _v15.header
        _x = _v16.seq
        buff.write(_get_struct_I().pack(_x))
        _v17 = _v16.stamp
        _x = _v17
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v16.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v15
        buff.write(_get_struct_2I().pack(_x.height, _x.width))
        _x = _v15.encoding
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = _v15
        buff.write(_get_struct_BI().pack(_x.is_bigendian, _x.step))
        _x = _v15.data
        length = len(_x)
        # - if encoded as a list instead, serialize as bytes instead of string
        if type(_x) in [list, tuple]:
          buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
        else:
          buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v18 = val1.location
        _v19 = _v18.header
        _x = _v19.seq
        buff.write(_get_struct_I().pack(_x))
        _v20 = _v19.stamp
        _x = _v20
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v19.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v21 = _v18.status
        _x = _v21
        buff.write(_get_struct_bH().pack(_x.status, _x.service))
        _x = _v18
        buff.write(_get_struct_3d().pack(_x.latitude, _x.longitude, _x.altitude))
        buff.write(_v18.position_covariance.tostring())
        _x = _v18.position_covariance_type
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
      if self.wounded_array is None:
        self.wounded_array = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.wounded_array = []
      for i in range(0, length):
        val1 = robot_description.msg.WoundedInfo()
        _v22 = val1.Image
        _v23 = _v22.header
        start = end
        end += 4
        (_v23.seq,) = _get_struct_I().unpack(str[start:end])
        _v24 = _v23.stamp
        _x = _v24
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v23.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v23.frame_id = str[start:end]
        _x = _v22
        start = end
        end += 8
        (_x.height, _x.width,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v22.encoding = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v22.encoding = str[start:end]
        _x = _v22
        start = end
        end += 5
        (_x.is_bigendian, _x.step,) = _get_struct_BI().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        _v22.data = str[start:end]
        _v25 = val1.location
        _v26 = _v25.header
        start = end
        end += 4
        (_v26.seq,) = _get_struct_I().unpack(str[start:end])
        _v27 = _v26.stamp
        _x = _v27
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v26.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v26.frame_id = str[start:end]
        _v28 = _v25.status
        _x = _v28
        start = end
        end += 3
        (_x.status, _x.service,) = _get_struct_bH().unpack(str[start:end])
        _x = _v25
        start = end
        end += 24
        (_x.latitude, _x.longitude, _x.altitude,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 72
        _v25.position_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=9)
        start = end
        end += 1
        (_v25.position_covariance_type,) = _get_struct_B().unpack(str[start:end])
        self.wounded_array.append(val1)
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
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
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
_struct_bH = None
def _get_struct_bH():
    global _struct_bH
    if _struct_bH is None:
        _struct_bH = struct.Struct("<bH")
    return _struct_bH
