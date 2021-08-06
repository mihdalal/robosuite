"""
Aravind's janky attempt
"""
import numpy as np

from robosuite.models.grippers.gripper_model import GripperModel
from robosuite.utils.mjcf_utils import xml_path_completion


class XarmGripper(GripperModel):
    """"""

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("grippers/xarm_gripper.xml"), idn=idn)

    def format_action(self, action):
        """Here, we take in a scalar action and just duplicate it 6 times."""
        assert len(action) == 1
        return np.tile(action, 6)

    @property
    def dof(self):
        return 1

    @property
    def init_qpos(self):
        return np.array([0.020833, -0.020833])

    @property
    def _joints(self):
        return [
            "drive_joint",
            "left_finger_joint",
            "left_inner_knuckle_joint",
            "right_outer_knuckle_joint",
            "right_finger_joint",
            "right_inner_knuckle_joint",
        ]

    @property
    def _actuators(self):
        return [
            "gripper_drive_joint",
            "gripper_left_finger_joint",
            "gripper_left_inner_knuckle_joint",
            "gripper_right_outer_knuckle_joint",
            "gripper_right_finger_joint",
            "gripper_right_inner_knuckle_joint",
        ]

    @property
    def _contact_geoms(self):
        # Hoping i dont need to do anything here
        return []

    @property
    def _important_geoms(self):
        # Hoping i dont need to do anything here
        return {}
