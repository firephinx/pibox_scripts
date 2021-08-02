#!/bin/bash

sleep 30
source /home/iam-lab/.bashrc
source /opt/ros/noetic/setup.bash
source /home/iam-lab/catkin_ws/devel/setup.bash
roslaunch realsense2_camera rs_aligned_depth.launch
