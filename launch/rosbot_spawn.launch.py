from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch_ros.actions
  
def generate_launch_description():
    rosbot_description_dir = get_package_share_directory('rosbot_description')
    return LaunchDescription([
        launch_ros.actions.Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '0', '-1.5707', '0', '-1.5707', 'camera_link', 'camera_depth_frame'],
            parameters=[
        		rosbot_description_dir + '/config/static_tf.yaml'
        	],
            ),
        launch_ros.actions.Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            output='screen',
            arguments=['-0.03', '0', '0.11', '0', '0', '0', 'base_link', 'camera_link'],
            parameters=[
        		rosbot_description_dir + '/config/static_tf.yaml'
            ]
            ),
        launch_ros.actions.Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '0.07', '0', '0', '0', 'base_link', 'laser'],
            parameters=[
        		rosbot_description_dir + '/config/static_tf_sim.yaml'
            ]
            ),
        launch_ros.actions.Node(
            package='gazebo_ros',
            node_executable='spawn_entity.py',
            output='screen',
            arguments=['-entity', 'rosbot', '-x', '0', '-y', '0', '-z', '0.03', '-file', rosbot_description_dir + '/models/rosbot.sdf']),
    ])

