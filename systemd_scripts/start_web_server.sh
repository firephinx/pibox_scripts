#!/bin/bash

sleep 75
source /home/iam-lab/.bashrc
source /opt/ros/noetic/setup.bash
source /home/iam-lab/catkin_ws/devel/setup.bash
rosrun web_video_server web_video_server
