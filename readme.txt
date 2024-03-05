create a new ws
clone the repo in src folder
do catkin_make


roslaunch robot_gazebo mobile_robot_world.launch 
roslaunch robot_gazebo moveit_gazebo.launch
roslaunch robot_navigation robot_navigation.launch
rosrun robot_navigation do_task.py
