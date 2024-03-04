#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',anonymous=True)

robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()


group_name = "arm_group"
group = moveit_commander.MoveGroupCommander(group_name)

group_names = robot.get_group_names()
print("============ Robot Groups:", robot.get_group_names())

print("============ Printing robot state")
print(robot.get_current_state())