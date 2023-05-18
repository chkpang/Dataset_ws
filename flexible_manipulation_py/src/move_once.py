#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy, sys
import _thread, copy
import moveit_commander
from moveit_commander import RobotCommander, MoveGroupCommander, PlanningSceneInterface
from geometry_msgs.msg import PoseStamped, Pose
from moveit_msgs.msg import CollisionObject, AttachedCollisionObject, PlanningScene
from math import radians
from copy import deepcopy
import tf2_ros
from tf_trans import tf_listener


# 初始化move_group的API
moveit_commander.roscpp_initialize(sys.argv)

# 初始化ROS节点
rospy.init_node('moveit_ik_demo')

# 初始化场景对象，用来监听外部环境的变化
scene = PlanningSceneInterface()
rospy.sleep(1)
        
# 初始化需要使用move group控制的机械臂中的arm group
ur = moveit_commander.MoveGroupCommander('manipulator')
gripper = moveit_commander.MoveGroupCommander('gripper') 

end_effector_link = 'yixiuge_ee_link'

# 设置目标位置所使用的参考坐标系
reference_frame = 'world'
gripper.set_pose_reference_frame(reference_frame)
        
# 当运动规划失败后，允许重新规划
gripper.allow_replanning(True)


# 设置位置(单位：米)和姿态（单位：弧度）的允许误差
gripper.set_goal_position_tolerance(0.05)
gripper.set_goal_orientation_tolerance(0.05)

# 设置允许的最大速度和加速度
ur.set_max_acceleration_scaling_factor(0.5)
ur.set_max_velocity_scaling_factor(0.5)
ur.set_max_acceleration_scaling_factor(0.5)
ur.set_max_velocity_scaling_factor(0.5)


# 控制机械臂先回到初始化位置
ur.set_named_target('yixiuge_home')
ur.go()

scene.remove_world_object('table') 
scene.remove_world_object('target')

table1_size = [0.5, 1.2, 0.6]  # 设置长宽高




# 将table加入场景当中
table1_pose = PoseStamped()
table1_pose.header.frame_id = 'world'
table1_pose.pose.position.x = 0
table1_pose.pose.position.y = 1.13
table1_pose.pose.position.z = 0
table1_pose.pose.orientation.w = 1.0
scene.add_box('table1', table1_pose, table1_size)  #添加障碍物

rospy.sleep(2)


""" buffer = tf2_ros.Buffer()	#初始化缓冲区
listener = tf2_ros.TransformListener(buffer)	#初始化监听对象

trans = buffer.lookup_transform("world","camera_marker",rospy.Time(0),rospy.Duration(5.0))

#tfl = tf.TransformListener()
#(trans,rot) = tfl.lookupTransform('world', 'camera_marker', rospy.Time(0))

print(trans) """




target_pose0 = PoseStamped()


#参考坐标系，前面设置了
target_pose0.header.frame_id = reference_frame
target_pose0.header.stamp = rospy.Time.now() #时间戳？

#末端位置2，右手预备位置1   
""" target_pose0.pose.position.x = trans.transform.translation.x
target_pose0.pose.position.y = trans.transform.translation.y - 0.1
target_pose0.pose.position.z = trans.transform.translation.z + 0.6 """

target_pose0.pose.position.x = -0.4
target_pose0.pose.position.y = 0.7
target_pose0.pose.position.z = 1.2
#末端姿态，四元数
target_pose0.pose.orientation.x = 0
target_pose0.pose.orientation.y = 0
target_pose0.pose.orientation.z = 0.707
target_pose0.pose.orientation.w = 0.707

# 设置机器臂当前的状态作为运动初始状态

ur.set_start_state_to_current_state()

# 设置机械臂终端运动的目标位姿

#ur.set_pose_target(target_pose0, end_effector_link)
#ur.go()

# rospy.sleep(1)
# 设置机械臂工作空间中的目标位姿，位置使用x、y、z坐标描述，
# 姿态使用四元数描述，基于base_link坐标系
target_pose1 = PoseStamped()


#参考坐标系，前面设置了
target_pose1.header.frame_id = reference_frame
target_pose1.header.stamp = rospy.Time.now() #时间戳？

#末端位置2，右手预备位置1   
""" target_pose1.pose.position.x = trans.transform.translation.x
target_pose1.pose.position.y = trans.transform.translation.y - 0.1
target_pose1.pose.position.z = trans.transform.translation.z + 0.6 """

target_pose1.pose.position.x = -0.4
target_pose1.pose.position.y = 0.7
target_pose1.pose.position.z = 1.013
#末端姿态，四元数
target_pose1.pose.orientation.x = 0
target_pose1.pose.orientation.y = 0
target_pose1.pose.orientation.z = 0.707
target_pose1.pose.orientation.w = 0.707

# 设置机器臂当前的状态作为运动初始状态

ur.set_start_state_to_current_state()

# 设置机械臂终端运动的目标位姿

ur.set_pose_target(target_pose1, end_effector_link)
ur.go()

rospy.sleep(1)

""" gripper.set_named_target("close")
gripper.go()

rospy.sleep(1) """

target_pose2 = PoseStamped()


#参考坐标系，前面设置了
target_pose2.header.frame_id = reference_frame
target_pose2.header.stamp = rospy.Time.now() #时间戳？

#末端位置2，右手预备位置1   
""" target_pose2.pose.position.x = trans.transform.translation.x
target_pose2.pose.position.y = trans.transform.translation.y - 0.1
target_pose2.pose.position.z = trans.transform.translation.z + 0.6 """

target_pose2.pose.position.x = -0.4
target_pose2.pose.position.y = 0.7
target_pose2.pose.position.z = 1.2
#末端姿态，四元数
target_pose2.pose.orientation.x = 0
target_pose2.pose.orientation.y = 0
target_pose2.pose.orientation.z = 0.707
target_pose2.pose.orientation.w = 0.707

# 设置机器臂当前的状态作为运动初始状态

ur.set_start_state_to_current_state()

# 设置机械臂终端运动的目标位姿

#ur.set_pose_target(target_pose2, end_effector_link)
#ur.go()

#rospy.sleep(1)


target_pose3 = PoseStamped()


#参考坐标系，前面设置了
target_pose3.header.frame_id = reference_frame
target_pose3.header.stamp = rospy.Time.now() #时间戳？

#末端位置2，右手预备位置1   
""" target_pose3.pose.position.x = trans.transform.translation.x
target_pose3.pose.position.y = trans.transform.translation.y - 0.1
target_pose3.pose.position.z = trans.transform.translation.z + 0.6 """

target_pose3.pose.position.x = -0.2
target_pose3.pose.position.y = 0.9
target_pose3.pose.position.z = 1.2
#末端姿态，四元数
target_pose3.pose.orientation.x = 0
target_pose3.pose.orientation.y = 0
target_pose3.pose.orientation.z = 0.707
target_pose3.pose.orientation.w = 0.707

# 设置机器臂当前的状态作为运动初始状态

ur.set_start_state_to_current_state()

# 设置机械臂终端运动的目标位姿

#ur.set_pose_target(target_pose3, end_effector_link)
#ur.go()

#rospy.sleep(1)


target_pose4 = PoseStamped()


#参考坐标系，前面设置了
target_pose4.header.frame_id = reference_frame
target_pose4.header.stamp = rospy.Time.now() #时间戳？

#末端位置2，右手预备位置1   
""" target_pose4.pose.position.x = trans.transform.translation.x
target_pose4.pose.position.y = trans.transform.translation.y - 0.1
target_pose4.pose.position.z = trans.transform.translation.z + 0.6 """

target_pose4.pose.position.x = -0.2
target_pose4.pose.position.y = 0.9
target_pose4.pose.position.z = 1.015
#末端姿态，四元数
target_pose4.pose.orientation.x = 0
target_pose4.pose.orientation.y = 0
target_pose4.pose.orientation.z = 0.707
target_pose4.pose.orientation.w = 0.707

# 设置机器臂当前的状态作为运动初始状态

ur.set_start_state_to_current_state()

# 设置机械臂终端运动的目标位姿

ur.set_pose_target(target_pose4, end_effector_link)
ur.go()

rospy.sleep(1)

gripper.set_named_target("open")
gripper.go()

rospy.sleep(1)

# 控制机械臂先回到初始化位置
ur.set_named_target('yixiuge_home')
ur.go()	


# 关闭并退出moveit
moveit_commander.roscpp_shutdown()
moveit_commander.os._exit(0)

