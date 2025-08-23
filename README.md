# ROS2 Depth to Point Cloud Converter
This project demonstrates depth image to point cloud conversion in a differential drive robot simulation using ros_gz_bridge. The package processes depth camera data and converts it to point cloud format using ros_gz_bridge for real-time 3D visualization and perception applications. View the project visualization [here]().

## System Requirements
- **Ubuntu**: 22.04 LTS
- **ROS 2**: Jazzy Jalisco
- **Gazebo**: Harmonic

## Usage

### Prerequisites
Install required ROS 2 packages:
```bash
sudo apt install ros-jazzy-robot-state-publisher \
                 ros-jazzy-joint-state-publisher \
                 ros-jazzy-xacro \
                 ros-jazzy-teleop-twist-keyboard \
                 ros-jazzy-ros-gz-sim \
                 ros-jazzy-ros-gz-bridge \
                 ros-jazzy-sensor-msgs \
                 ros-jazzy-rviz2
```

### Installation & Setup
1. **Create Workspace and Clone Repository**
```bash
mkdir -p my_ws/src && cd my_ws/src
git clone https://github.com/yashikasharma0301/depth_to_pcl.git
```

2. **Build the Workspace**
```bash
cd ..
colcon build
```

3. **Source the Workspace**
```bash
source install/setup.bash
```

### Running the Simulation

1. **Launch Robot with Depth Camera in Gazebo**
```bash
ros2 launch depth_to_pcl gazebo_spawn.launch.py
```
<img width="1028" height="911" alt="image" src="https://github.com/user-attachments/assets/1020aeae-be2c-4346-8362-5c1983da2453" />

To enable robot control within Gazebo:
- Click on the three dots on the upper right corner of your Gazebo window
- Search for **Teleop** from the menu and click on it
- This will open the teleop plugin allowing you to control the robot directly from Gazebo

2. **Start RViz2 for Point Cloud Visualization**

In another terminal run:
```bash
rviz2 -d /home/yashika-arz-i007/my_ws/src/depth_to_pcl/rviz/pcl.rviz
```
- Ensure the **Fixed Frame** is set to `camera_optical_frame`
- You will be able to see the point cloud visualization in RViz2
- Move the robot around in Gazebo using **Teleop** and you will be able to see the corresponding point cloud
<img width="1832" height="879" alt="image" src="https://github.com/user-attachments/assets/fe09c769-7123-47f8-b60f-4af8eab3764d" />


3. **Alternative: Depth Image Visualization**

If you want to see the depth image instead of the point cloud:
- Turn off the point cloud display in RViz2
- Set the **Fixed Frame** to `base_footprint`
- Select the corresponding RViz plugins for camera and image visualization
- You will be able to see some rough visualization in the set format (refer rqt for better visualization)
<img width="1228" height="1012" alt="image" src="https://github.com/user-attachments/assets/97a78c50-f71d-464f-96d9-496b8fd9cdcc" />

<img width="1390" height="876" alt="image" src="https://github.com/user-attachments/assets/fe3f12d8-4c61-41d1-865f-3fe42fa9831e" />


## Credits & References
**Robot Model**: This project uses a URDF model adapted from the TortoiseBot example in the [OSRF ROS Book](https://github.com/osrf/rosbook/blob/master/code/tortoisebot/tortoisebot.urdf). The original model has been modified for ROS 2 Jazzy and Gazebo Harmonic integration with depth camera sensor capabilities.

**Original Authors**: Open Source Robotics Foundation (OSRF)
