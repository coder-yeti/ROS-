#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publishMethod():
    pub = rospy.Publisher('talker', String, queue_size=10) #defining the publisher by topic, message type and queue size
    rospy.init_node('publish_node', anonymous=True) #defining the ROS node - publish node
    rate = rospy.Rate(10) #10hz #frequency at which the publishing is done
    while not rospy.is_shutdown():
        publishString = "This is being published" #variable
        rospy.loginfo("Data is being sent") #to print on the terminal
        pub.publish(publishString)
        rate.sleep()
if __name__ == '__main__':
    try:
        publishMethod()
    except rospy.ROSInterruptException:
        pass