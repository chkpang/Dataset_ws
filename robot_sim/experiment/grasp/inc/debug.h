#ifndef _DEBUG_H_
#define _DEBUG_H_

#include <ros/ros.h>
#include <dynamic_reconfigure/server.h>
#include <robot_sim/graspConfig.h>
#include <robot_sim/data_collectionConfig.h>

#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

extern string obj_name;
extern double obj_x;
extern double obj_y;
extern double obj_z;
extern double obj_roll;
extern double obj_pitch;
extern double obj_yaw;
extern double eelink_x;
extern double eelink_y;
extern double eelink_z;
extern double eelink_roll;
extern double eelink_pitch;
extern double eelink_yaw;
extern double grasp_angle;

extern double shoulder_pan_joint;
extern double shoulder_lift_joint;
extern double elbow_joint;
extern double wrist_1_joint;
extern double wrist_2_joint;
extern double wrist_3_joint;
extern double gripper_finger1_joint;

extern double tcp_eelink_x;
extern double tcp_eelink_y;
extern double tcp_eelink_z;
extern double tcp_eelink_roll;
extern double tcp_eelink_pitch;
extern double tcp_eelink_yaw;


extern bool enable_move_and_grasp_flag;
extern bool enable_move_obj_flag;
extern bool reset_obj_pos_flag;
extern bool enable_moveit_flag;
extern bool enable_grasp_flag;
extern bool save_image_flag;
extern bool save_mask_flag;

extern bool enable_move_tcp_eelink_flag;
extern bool enable_move_tcp_eelink_and_grasp_flag;
extern bool enable_move_forward_flag;

extern bool next_pose;
extern bool save_data;

void grasp_dynamic_callback(robot_sim::graspConfig &config);
void data_collection_dynamic_callback(robot_sim::data_collectionConfig &config);

#endif