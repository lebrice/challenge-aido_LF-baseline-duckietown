#!/bin/bash

cp -rf 1_develop/catkin_ws/src/codequackers 3_submit/
cp 1_develop/custom/lf_slim.launch 3_submit/

cd 3_submit
dts challenges submit --challenge aido3-LF-sim-validation
