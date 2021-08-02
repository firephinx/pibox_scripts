#!/bin/bash

sleep 45
source /home/iam-lab/.bashrc
source /opt/ros/noetic/setup.bash
source /home/iam-lab/catkin_ws/devel/setup.bash
rosrun seekthermal_ros seekthermal_ros_node
