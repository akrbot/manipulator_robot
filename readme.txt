create a new ws
clone the repo in src folder
do catkin_make

roslaunch robot_description mobile_manipulator_gazebo_new.launch
roslaunch navigation mobile_manipulator_move_base.launch

for task2
roslaunch robot_gazebo mobile_robot_world.launch 
roslaunch robot_navigation robot_navigation.launch
rosrun robot_navigation send_2d_navGoal.py
