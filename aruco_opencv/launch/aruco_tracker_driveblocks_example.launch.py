# Copyright 2023 driveblocks GmbH
# driveblocks proprietary license
from launch import LaunchDescription
from launch_ros.actions import Node

# ----------------
def generate_launch_description():

    camera_name_aruco_tracking = "camera_front"

    # ----------------
    # ArUco marker tracking
    aruco_opencv_launch = Node(
        package="aruco_opencv",
        executable="aruco_tracker_autostart",
        arguments=["--ros-args", "--log-level", "info"],
        parameters=[
            {
                "cam_base_topic": "/camera/"
                + camera_name_aruco_tracking
                + "/image/compressed",
                "marker_dict": "7X7_50",
                "image_sub_compressed": True,
                "image_is_rectified": False,
                "publish_tf": True,
                "marker_size": 0.235,
            }
        ],
    )

    # ----------------
    # launch configuration
    return LaunchDescription([aruco_opencv_launch])
