#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rospy.init_node('ObiTwo')

def callback(msg):
	if msg.ranges[0] < 0.5:			# ranges degree scan
		move.linear.x = 0.0
		move.angular.z = 0.5
	elif msg.ranges[30] < 0.5:
		move.linear.x = 0.0
		move.angular.z = 0.5
	elif msg.ranges[180] < 0.5:
		move.linear.x = 0.0
		move.angular.z = 0.5
	else:
		move.linear.x = 0.5
		move.angular.z = 0.0


	pub.publish(move)
	
#rate = rospy.Rate(2)


pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
move = Twist()
rospy.spin()


#   while not rospy.is_shutdown():
#   	pub.publish(move)
#   	rate.sleep()
