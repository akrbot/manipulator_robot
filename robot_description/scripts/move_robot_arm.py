#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

if __name__ == '__main__':
    rospy.init_node('arm_controller_publisher')

    pub = rospy.Publisher('/arm_controller/command', JointTrajectory, queue_size=10)
    rospy.sleep(1)  # Wait for publisher to initialize

    # Create a JointTrajectory message
    msg = JointTrajectory()
    msg.joint_names = ["arm_base_joint", "shoulder_joint", "bottom_wrist_joint", "elbow_joint", "top_wrist_joint"]

    # Create a JointTrajectoryPoint message
    point = JointTrajectoryPoint()
    point.positions = [-1.5794, -1.8918, 2.3778, 0.0868, 1.0935]
    point.time_from_start = rospy.Duration(1.0)  # 1 second from start

    # Add the point to the trajectory
    msg.points.append(point)

    rate = rospy.Rate(10)  # 10Hz

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()