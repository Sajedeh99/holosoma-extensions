"""Observation presets that incorporate extension-defined terms."""

from __future__ import annotations

from holosoma.config_types.robot import (
    RobotAssetConfig,
    RobotBridgeConfig,
    RobotConfig,
    RobotControlConfig,
    RobotInitState,
)

from holosoma.config_values.robot import DEFAULTS as CORE_DEFAULTS

go2_12dof = RobotConfig(
    num_bodies=17,
    dof_obs_size=12,
    actions_dim=12,
    policy_obs_dim=-1,
    critic_obs_dim=-1,
    algo_obs_dim_dict={},
    key_bodies=["FL_foot_contact_point", "FR_foot_contact_point", "RL_foot_contact_point", "RR_foot_contact_point"],
    num_feet=4,
    foot_body_name="foot",
    foot_height_name="foot_contact_point",
    torso_name="base",
    contact_pairs_multiplier=1,
    knee_name="",
    knee_dof_names=[],
    hips_dof_names=[],
    dof_names=[
        "FL_hip_joint", "FL_thigh_joint", "FL_calf_joint",
        "FR_hip_joint", "FR_thigh_joint", "FR_calf_joint",
        "RL_hip_joint", "RL_thigh_joint", "RL_calf_joint",
        "RR_hip_joint", "RR_thigh_joint", "RR_calf_joint"
    ],
    upper_dof_names=[],
    upper_left_arm_dof_names=[],
    upper_right_arm_dof_names=[],
    lower_dof_names=[
        "FL_hip_joint", "FL_thigh_joint", "FL_calf_joint",
        "FR_hip_joint", "FR_thigh_joint", "FR_calf_joint",
        "RL_hip_joint", "RL_thigh_joint", "RL_calf_joint",
        "RR_hip_joint", "RR_thigh_joint", "RR_calf_joint"
    ],
    has_torso=True,
    has_upper_body_dof=False,
    left_ankle_dof_names=[],
    right_ankle_dof_names=[],
    dof_pos_lower_limit_list=[
        -1.0472, -1.5708, -2.7227,  # FL
        -1.0472, -1.5708, -2.7227,  # FR
        -1.0472, -0.5236, -2.7227,  # RL
        -1.0472, -0.5236, -2.7227   # RR
    ],
    dof_pos_upper_limit_list=[
        1.0472, 3.4907, -0.83776,   # FL
        1.0472, 3.4907, -0.83776,   # FR
        1.0472, 4.5379, -0.83776,   # RL
        1.0472, 4.5379, -0.83776    # RR
    ],
    dof_vel_limit_list=[
        30.1, 30.1, 15.70,
        30.1, 30.1, 15.70,
        30.1, 30.1, 15.70,
        30.1, 30.1, 15.70
    ],
    dof_effort_limit_list=[
        23.7, 23.7, 45.43,
        23.7, 23.7, 45.43,
        23.7, 23.7, 45.43,
        23.7, 23.7, 45.43
    ],
    dof_armature_list=[
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    ],  # right wrist
    dof_joint_friction_list=[
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ],
    body_names=[
        "base",
        "FL_hip", "FL_thigh", "FL_calf", "FL_foot", "FL_foot_contact_point",
        "FR_hip", "FR_thigh", "FR_calf", "FR_foot", "FR_foot_contact_point",
        "Head_upper", "Head_lower",
        "RL_hip", "RL_thigh", "RL_calf", "RL_foot", "RL_foot_contact_point",
        "RR_hip", "RR_thigh", "RR_calf", "RR_foot", "RR_foot_contact_point"
    ],
    terminate_after_contacts_on=[
        "base",
        "Head_upper",
        "Head_lower"
    ],
    penalize_contacts_on=[ # TODO: Remove this from the robot config since it's in the reward config
        "FL_thigh", "FR_thigh", "RL_thigh", "RR_thigh",
        "FL_calf", "FR_calf", "RL_calf", "RR_calf",
    ],
    init_state=RobotInitState(
        pos=[0.0, 0.0, 0.42],  # x,y,z [m]
        rot=[0.0, 0.0, 0.0, 1.0],  # x,y,z,w [quat]
        lin_vel=[0.0, 0.0, 0.0],  # x,y,z [m/s]
        ang_vel=[0.0, 0.0, 0.0],  # x,y,z [rad/s]
        default_joint_angles={
            "FL_hip_joint": 0.1,
            "FL_thigh_joint": 0.8,
            "FL_calf_joint": -1.5,
            "FR_hip_joint": 0.1,
            "FR_thigh_joint": 0.8,
            "FR_calf_joint": -1.5,
            "RL_hip_joint": -0.1,
            "RL_thigh_joint": 1.0,
            "RL_calf_joint": -1.5,
            "RR_hip_joint": -0.1,
            "RR_thigh_joint": 1.0,
            "RR_calf_joint": -1.5,
        },
    ),
    randomize_link_body_names=[
        "base",
        "FL_hip", "FL_thigh", "FL_calf",
        "FR_hip", "FR_thigh", "FR_calf",
        "RL_hip", "RL_thigh", "RL_calf",
        "RR_hip", "RR_thigh", "RR_calf"
    ],
    
    symmetry_joint_names={
        "FL_hip_joint": "FR_hip_joint", # fl_hip_joint
        "FL_thigh_joint": "FR_thigh_joint", # fl_thigh_joint
        "FL_calf_joint": "FR_calf_joint", # fl_calf_joint
        "FR_hip_joint": "FL_hip_joint", # fr_hip_joint
        "FR_thigh_joint": "FL_thigh_joint", # fr_thigh_joint
        "FR_calf_joint": "FL_calf_joint", # fr_calf_joint
        "RL_hip_joint": "RR_hip_joint", # rl_hip_joint
        "RL_thigh_joint": "RR_thigh_joint", # rl_thigh_joint
        "RL_calf_joint": "RR_calf_joint", # rl_calf_joint
        "RR_hip_joint": "RL_hip_joint", # rr_hip_joint
        "RR_thigh_joint": "RL_thigh_joint", # rr_thigh_joint
        "RR_calf_joint": "RL_calf_joint", # rr_calf_joint
    },
    flip_sign_joint_names=[
        "FL_hip_joint", "FR_hip_joint", "RL_hip_joint", "RR_hip_joint",
    ],
    apply_dof_armature_in_isaacgym=True,
    control=RobotControlConfig(
        control_type="P",
        stiffness={
            "FL_hip_joint": 20,
            "FL_thigh_joint": 20,
            "FL_calf_joint": 20,
            "FR_hip_joint": 20,
            "FR_thigh_joint": 20,
            "FR_calf_joint": 20,
            "RL_hip_joint": 20,
            "RL_thigh_joint": 20,
            "RL_calf_joint": 20,
            "RR_hip_joint": 20,
            "RR_thigh_joint": 20,
            "RR_calf_joint": 20,
        },
        damping={
            "FL_hip_joint": 0.5,
            "FL_thigh_joint": 0.5,
            "FL_calf_joint": 0.5,
            "FR_hip_joint": 0.5,
            "FR_thigh_joint": 0.5,
            "FR_calf_joint": 0.5,
            "RL_hip_joint": 0.5,
            "RL_thigh_joint": 0.5,
            "RL_calf_joint": 0.5,
            "RR_hip_joint": 0.5,
            "RR_thigh_joint": 0.5,
            "RR_calf_joint": 0.5,
        },
        action_scale=0.25,  # 0.25 for locomotion, 1.0 for whole body tracking
        action_clip_value=100.0,
        clip_actions=True,
        clip_torques=True,
    ),
    asset=RobotAssetConfig(
        asset_root="@holosoma_ext/data/robots",
        collapse_fixed_joints=True,
        replace_cylinder_with_capsule=True,
        flip_visual_attachments=True,
        armature=0.001,
        thickness=0.01,
        max_angular_velocity=1000.0,
        max_linear_velocity=1000.0,
        angular_damping=0.0,
        linear_damping=0.0,
        urdf_file="go2/go2_12dof.urdf",
        usd_file=None,
        xml_file="go2/go2_12dof.xml",
        robot_type="go2_12dof",
        enable_self_collisions=True,
        default_dof_drive_mode=3,
        fix_base_link=False,
    ),
    bridge=RobotBridgeConfig(
        sdk_type="unitree",
        motor_type="serial",
    ),
)

ilia_19dof = RobotConfig(
    num_bodies=22,
    dof_obs_size=19,
    actions_dim=19,
    policy_obs_dim=-1,
    critic_obs_dim=-1,
    algo_obs_dim_dict={},
    key_bodies=["left_foot_contact_point", "right_foot_contact_point"],
    num_feet=2,
    foot_body_name="foot_link",
    foot_height_name="foot_contact_point",
    knee_name="shank_link",
    torso_name="torso_link",
    dof_names=[
        "left_hip_pitch_joint",
        "left_hip_roll_joint",
        "left_hip_yaw_joint",
        "left_knee_joint",
        "left_ankle_pitch_joint",
        "right_hip_pitch_joint",
        "right_hip_roll_joint",
        "right_hip_yaw_joint",
        "right_knee_joint",
        "right_ankle_pitch_joint",
        "waist_yaw_joint",
        "left_shoulder_pitch_joint",
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "left_elbow_joint",
        "right_shoulder_pitch_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
        "right_elbow_joint",
    ],
    upper_dof_names=[
        "waist_yaw_joint",
        "left_shoulder_pitch_joint",
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "left_elbow_joint",
        "right_shoulder_pitch_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
        "right_elbow_joint",
    ],
    upper_left_arm_dof_names=[
        "left_shoulder_pitch_joint",
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "left_elbow_joint",
    ],
    upper_right_arm_dof_names=[
        "right_shoulder_pitch_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
        "right_elbow_joint",
    ],
    lower_dof_names=[
        "left_hip_pitch_joint",
        "left_hip_roll_joint",
        "left_hip_yaw_joint",
        "left_knee_joint",
        "left_ankle_pitch_joint",
        "right_hip_pitch_joint",
        "right_hip_roll_joint",
        "right_hip_yaw_joint",
        "right_knee_joint",
        "right_ankle_pitch_joint",
    ],
    has_torso=True,
    has_upper_body_dof=True,
    left_ankle_dof_names=["left_ankle_pitch_joint"],
    right_ankle_dof_names=["right_ankle_pitch_joint"],
    knee_dof_names=["left_knee_joint", "right_knee_joint"],
    hips_dof_names=[
        "left_hip_pitch_joint",
        "left_hip_roll_joint",
        "left_hip_yaw_joint",
        "right_hip_pitch_joint",
        "right_hip_roll_joint",
        "right_hip_yaw_joint",
    ],
    dof_pos_lower_limit_list=[
        -3.14,      # left leg
        -0.26,
        -3.14,
         0,
        -1.117,
        -3.14,      # right leg
        -2.61,
        -3.14,
         0,
        -1.117,
        -3.14,      # waist yaw
         0,         # left arm
        -3.14,
        -3.14,
         0,
        -3.14,      # right arm
        -3.14,
        -3.14,
         0,
    ],
    dof_pos_upper_limit_list=[
        3.14,       # left leg
        2.61,
        3.14,
        2.18,
        1.029,
        3.14,       # right leg
        0.26,
        3.14,
        2.18,
        1.029,
        3.14,       # waist yaw
        3.14,       # left arm
        3.14,
        3.14,
        2.79,
        3.14,       # right arm
        0,
        3.14,
        2.79,
    ],
    dof_vel_limit_list=[
        39.0,       # left leg
        48.0,
        48.0,
        19.5,
        24,
        39.0,       # right leg
        48.0,
        48.0,
        19.5,
        24,
        48,         # waist yaw
        48,         # left arm   
        48,   
        48,
        35.55,
        48,         # right arm   
        48,   
        48,
        35.55,
    ],  
    dof_effort_limit_list=[
        72.0,       # left leg
        33.6,
        33.6,
        144,
        67.2,
        72.0,       # right leg
        33.6,
        33.6,
        144,
        67.2,
        33.6,       # waist yaw
        33.6,       # left arm   
        33.6,  
        33.6,
        45.36,   
        33.6,       # right arm   
        33.6,  
        33.6,
        45.36, 
    ],  
    dof_armature_list=[
        0.010177520,
        0.025101925,
        0.010177520,
        0.025101925,
        0.007219450,  # left leg
        0.010177520,
        0.025101925,
        0.010177520,
        0.025101925,
        0.007219450,  # right leg
        0.007219450,  # waist
        0.003609725,
        0.003609725,
        0.003609725,
        0.003609725,  # left arm
        0.003609725,
        0.003609725,
        0.003609725,
        0.003609725,  # right arm
    ], 
    dof_joint_friction_list=[
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ],
    body_names=[
        "base",
        "left_hip_first_link",
        "left_hip_second_link",
        "left_thigh_link",
        "left_shank_link",
        "left_foot_link",
        "left_foot_contact_point",
        "right_hip_first_link",
        "right_hip_second_link",
        "right_thigh_link",
        "right_shank_link",
        "right_foot_link",
        "right_foot_contact_point",
        "torso_link",
        "left_shoulder_first_link",
        "left_shoulder_second_link",
        "left_upper_arm_link",
        "left_fore_arm_link",
        "right_shoulder_first_link",
        "right_shoulder_second_link",
        "right_upper_arm_link",
        "right_fore_arm_link",
    ],
    terminate_after_contacts_on=["base", "shoulder", "hip"],
    penalize_contacts_on=["base", "shoulder", "hip"],
    init_state=RobotInitState(
        pos=[0.0, 0.0, 0.72],  # x,y,z [m]
        rot=[0.0, 0.0, 0.0, 1.0],  # x,y,z,w [quat]
        lin_vel=[0.0, 0.0, 0.0],  # x,y,z [m/s]
        ang_vel=[0.0, 0.0, 0.0],  # x,y,z [rad/s]
        default_joint_angles={
            "left_hip_pitch_joint": -0.174,
            "left_hip_roll_joint": 0.0,
            "left_hip_yaw_joint": -0.087,
            "left_knee_joint": 0.349,
            "left_ankle_pitch_joint": -0.191,
            "right_hip_pitch_joint": -0.174,
            "right_hip_roll_joint": 0.0,
            "right_hip_yaw_joint": 0.087,
            "right_knee_joint": 0.349,
            "right_ankle_pitch_joint": -0.191,
            "waist_yaw_joint": 0.0,
            "left_shoulder_pitch_joint": 0.261,
            "left_shoulder_roll_joint": 0.174,
            "left_shoulder_yaw_joint": 0.0,
            "left_elbow_joint": 1.134,
            "right_shoulder_pitch_joint": 0.261,
            "right_shoulder_roll_joint": -0.174,
            "right_shoulder_yaw_joint": 0.0,
            "right_elbow_joint": 1.134,
        },
    ),
    randomize_link_body_names=[
        "base",
        "left_hip_first_link",
        "left_hip_second_link",
        "left_thigh_link",
        "left_shank_link",
        "right_hip_first_link",
        "right_hip_second_link",
        "right_thigh_link",
        "right_shank_link",
    ],
    waist_dof_names=["waist_yaw_joint"],
    waist_yaw_dof_name="waist_yaw_joint",
    waist_roll_dof_name=None,
    waist_pitch_dof_name=None,
    arm_dof_names=[
        "left_shoulder_pitch_joint",
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "left_elbow_joint",
        "right_shoulder_pitch_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
        "right_elbow_joint",
    ],
    left_arm_dof_names=[
        "left_shoulder_pitch_joint",
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "left_elbow_joint",
    ],
    right_arm_dof_names=[
        "right_shoulder_pitch_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
        "right_elbow_joint",
    ],
    symmetry_joint_names={
        # Lower body joints
        "left_hip_pitch_joint": "right_hip_pitch_joint",
        "left_hip_roll_joint": "right_hip_roll_joint",
        "left_hip_yaw_joint": "right_hip_yaw_joint",
        "left_knee_joint": "right_knee_joint",
        "left_ankle_pitch_joint": "right_ankle_pitch_joint",
        "right_hip_pitch_joint": "left_hip_pitch_joint",
        "right_hip_roll_joint": "left_hip_roll_joint",
        "right_hip_yaw_joint": "left_hip_yaw_joint",
        "right_knee_joint": "left_knee_joint",
        "right_ankle_pitch_joint": "left_ankle_pitch_joint",
        # Upper body joints
        "left_shoulder_pitch_joint": "right_shoulder_pitch_joint",
        "left_shoulder_roll_joint": "right_shoulder_roll_joint",
        "left_shoulder_yaw_joint": "right_shoulder_yaw_joint",
        "left_elbow_joint": "right_elbow_joint",
        "right_shoulder_pitch_joint": "left_shoulder_pitch_joint",
        "right_shoulder_roll_joint": "left_shoulder_roll_joint",
        "right_shoulder_yaw_joint": "left_shoulder_yaw_joint",
        "right_elbow_joint": "left_elbow_joint",
        # Central joints (map to themselves)
        "waist_yaw_joint": "waist_yaw_joint",
    },
    flip_sign_joint_names=[
        # Hip roll and yaw joints
        "left_hip_roll_joint",
        "left_hip_yaw_joint",
        "right_hip_roll_joint",
        "right_hip_yaw_joint",
        # Waist yaw joints
        "waist_yaw_joint",
        # Shoulder roll and yaw joints
        "left_shoulder_roll_joint",
        "left_shoulder_yaw_joint",
        "right_shoulder_roll_joint",
        "right_shoulder_yaw_joint",
    ],
    apply_dof_armature_in_isaacgym=True,
    contact_pairs_multiplier=16,
    control=RobotControlConfig(
        control_type="P",
        stiffness={
            "hip_yaw": 40.179238471,  # STIFFNESS_7520_14
            "hip_roll": 99.098427777,  # STIFFNESS_7520_22
            "hip_pitch": 40.179238471,  # STIFFNESS_7520_14
            "knee": 99.098427777,  # STIFFNESS_7520_22
            "ankle_pitch": 28.501246196,  # 2*STIFFNESS_5020
            "waist_yaw": 40.179238471,  # STIFFNESS_7520_14
            "shoulder_pitch": 14.250623098,  # STIFFNESS_5020
            "shoulder_roll": 14.250623098,  # STIFFNESS_5020
            "shoulder_yaw": 14.250623098,  # STIFFNESS_5020
            "elbow": 14.250623098,  # STIFFNESS_5020
        },
        damping={
            "hip_yaw": 2.557889765,  # DAMPING_7520_14
            "hip_roll": 6.308801854,  # DAMPING_7520_22
            "hip_pitch": 2.557889765,  # DAMPING_7520_14
            "knee": 6.308801854,  # DAMPING_7520_22
            "ankle_pitch": 1.814445687,  # 2*DAMPING_5020
            "waist_yaw": 2.557889765,  # DAMPING_7520_14
            "shoulder_pitch": 0.907222843,  # DAMPING_5020
            "shoulder_roll": 0.907222843,  # DAMPING_5020
            "shoulder_yaw": 0.907222843,  # DAMPING_5020
            "elbow": 0.907222843,  # DAMPING_5020
        },
        action_scale=0.25,  # 0.25 for locomotion, 1.0 for whole body tracking
        action_clip_value=100.0,
        clip_actions=True,
        clip_torques=True,
    ),
    asset=RobotAssetConfig(
        asset_root="@holosoma_ext/data/robots",
        collapse_fixed_joints=True,
        replace_cylinder_with_capsule=True,
        flip_visual_attachments=False,
        armature=0.001,
        thickness=0.01,
        max_angular_velocity=1000.0,
        max_linear_velocity=1000.0,
        angular_damping=0.0,
        linear_damping=0.0,
        urdf_file="ilia/ILIA.urdf",
        usd_file="ilia/ILIA/ILIA.usd",
        xml_file="ilia/ILIA.xml",
        robot_type="ilia_19dof",
        enable_self_collisions=False,
        default_dof_drive_mode=3,
        fix_base_link=False,
    ),
    bridge=RobotBridgeConfig(
        sdk_type="unitree",
        motor_type="serial",
    ),
)

CORE_DEFAULTS.update(
    {
        "go2_12dof": go2_12dof,
        "ilia_19dof": ilia_19dof,
    }
)

DEFAULTS = CORE_DEFAULTS

__all__ = [
    "DEFAULTS",
    "go2_12dof",
    "ilia_19dof",
]
