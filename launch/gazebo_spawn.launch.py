import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    this_pkg = 'depth_to_pcl'
    world_file_name = 'custom_world.sdf'
    xacro_file_name = 'model.xacro'

    world_path = os.path.join(
        get_package_share_directory(this_pkg),
        'worlds',
        world_file_name)

    xacro_file = os.path.join(
        get_package_share_directory(this_pkg),
        'urdf',
        xacro_file_name)

    robot_description_raw = xacro.process_file(xacro_file).toxml()

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_raw,
                     'use_sim_time': True}]
    )
    
    gazebo = ExecuteProcess(
        cmd=['gz', 'sim', world_path, '--verbose', '-r'],
        output='screen'
    )

    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'tortoisebot',
            '-topic', 'robot_description',
            '-x', '0', '-y', '0', '-z', '0.335'
        ],
        output='screen',
    )

    bridge_params = os.path.join(
        get_package_share_directory('tortoisebot'),
        'params',
        'bridge_params.yaml'
    )

    start_gazebo_ros_bridge_cmd = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ],
        output='screen',
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    return LaunchDescription([
        start_gazebo_ros_bridge_cmd,
        gazebo,
        spawn_entity,
        joint_state_publisher_node,
        node_robot_state_publisher
    ])
