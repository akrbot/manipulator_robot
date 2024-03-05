#! /usr/bin/env python
import rospy
import time
from moveit_arm_cntrl import MyRobot
from send_2d_navGoal import send_2dnav_goal

rospy.init_node('do_task_node', anonymous=True)
arm = MyRobot("arm_group")
gripper = MyRobot("gripper")

def pick_object():
    gripper.set_pose("open")
    time.sleep(1)
    arm.set_pose("home")
    time.sleep(1)
    arm.set_pose("pick")
    time.sleep(1)
    gripper.set_pose("close")
    time.sleep(1)
    arm.set_pose("home")
    time.sleep(1)

def place_object():
    arm.set_pose("pick")
    time.sleep(1)
    gripper.set_pose("open")
    time.sleep(1)
    arm.set_pose("home")
    time.sleep(1)

if __name__ == "__main__":
    goal_list = [[0,-5],[-2,-5],[-2,0],[-4,-0],[-4,-5]]
    orientation_list = [[ 0, 0, -0.7071068, 0.7071068 ],
                        [ 0, 0, 1, 0 ],
                        [ 0, 0, 0.7071068, 0.7071068 ],
                        [ 0, 0, 1, 0 ],
                        [ 0, 0, -0.7071068, 0.7071068 ]]
    

    try:
        pick_object()
        for i in range(len(goal_list)):
            result = send_2dnav_goal(goal_list[i],orientation_list[i])
            if result:
                rospy.loginfo("Goal execution done!")
            time.sleep(1)
        place_object()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
   