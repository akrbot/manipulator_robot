#!/usr/bin/env python2


import rospy
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def send_2dnav_goal(Pose2d,orientation):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = Pose2d[0]
    goal.target_pose.pose.position.y = Pose2d[1]

    goal.target_pose.pose.orientation.x = orientation[0]
    goal.target_pose.pose.orientation.y = orientation[1]
    goal.target_pose.pose.orientation.z = orientation[2]
    goal.target_pose.pose.orientation.w = orientation[3]

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    goal_list = [[0,-5],[-2,-5],[-2,0],[-4,-0],[-4,-5]]
    orientation_list = [[ 0, 0, -0.7071068, 0.7071068 ],[ 0, 0, 1, 0 ],[ 0, 0, 0.7071068, 0.7071068 ],[ 0, 0, 1, 0 ],[ 0, 0, -0.7071068, 0.7071068 ]]
   
    try:
        rospy.init_node('movebase_client_py')
        for i in range(len(goal_list)):
            result = send_2dnav_goal(goal_list[i],orientation_list[i])
            if result:
                rospy.loginfo("Goal execution done!")
            time.sleep(1)
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")


