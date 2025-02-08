
(cl:in-package :asdf)

(defsystem "robot_description-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "WoundedInfo" :depends-on ("_package_WoundedInfo"))
    (:file "_package_WoundedInfo" :depends-on ("_package"))
    (:file "WoundedInfoArray" :depends-on ("_package_WoundedInfoArray"))
    (:file "_package_WoundedInfoArray" :depends-on ("_package"))
  ))