#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

# Define Twist messages for clear representation
red_light_twist = Twist()
green_light_twist = Twist()
green_light_twist.linear.x = 0.5  # Set forward speed to 0.5 m/s

# ROS initialization
rospy.init_node('red_light_green_light')
rospy.loginfo("started")

# Publisher for velocity commands
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

# Flags and timing variables
driving_forward = False
light_change_time = rospy.Time.now()

# Loop rate for smooth execution (10 Hz)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  # Publish twist message based on driving state
  if driving_forward:
    cmd_vel_pub.publish(green_light_twist)
  else:
    cmd_vel_pub.publish(red_light_twist)

  # Check for light change timer
  if light_change_time < rospy.Time.now():
    driving_forward = not driving_forward
    light_change_time = rospy.Time.now() + rospy.Duration(3)  # Update timer for 3 second cycle

  # Sleep to maintain loop rate
  rate.sleep()
