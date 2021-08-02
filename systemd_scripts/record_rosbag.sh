#!/bin/bash

sleep 60
source /home/iam-lab/.bashrc
source /opt/ros/noetic/setup.bash
source /home/iam-lab/catkin_ws/devel/setup.bash
cd /home/iam-lab
rosbag record /audio /audio_info /camera/color/image_raw /camera/depth/image_rect_raw /seekthermal/image