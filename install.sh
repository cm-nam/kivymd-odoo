#!/bin/bash
sudo apt-get update
sudo apt-get remove -y cython
sudo apt-get install -y python3-dev net-tools build-essential adb aidl openssh-server
sudo apt-get install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake
sudo apt-get install -y libmesa-dev mesa-common-dev libglu1-mesa-dev freeglut3-dev

sudo python3 -m pip install buildozer
sudo python3 -m pip install cython==0.29.6
sudo python3 -m pip install virtualenv