#!/bin/bash

sleep 60
source /home/iam-lab/.bashrc
source /opt/ros/noetic/setup.bash
source /home/iam-lab/catkin_ws/devel/setup.bash
python3 /home/iam-lab/catkin_ws/src/seekthermal_ros/scripts/seekthermal.py