#!/bin/bash

sleep 60
source /home/iam-lab/.bashrc
source /opt/ros/noetic/setup.bash
source /home/iam-lab/catkin_ws/devel/setup.bash
rosrun sounddevice_ros sounddevice_ros_publisher_node.py