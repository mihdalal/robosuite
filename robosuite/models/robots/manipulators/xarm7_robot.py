import numpy as np

from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion


class Xarm7(ManipulatorModel):
    """
    Panda is a sensitive single-arm robot designed by Franka.

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    def __init__(
        self,
        idn=0,
        xml_path="robots/xarm7/robot.xml",
    ):
        super().__init__(
            xml_path_completion(xml_path),
            idn=idn,
        )

        # TODO fix this!
        self.set_joint_attribute(
            attrib="damping", values=np.array((0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.01))
        )

    @property
    def dof(self):
        return 7

    @property
    def gripper(self):
        return None

    @property
    def default_controller_config(self):
        return "default_xarm7_unused"

    @property
    def init_qpos(self):
        # This is the initial position when loaded with MoveIt
        # return np.array([0, -0.5, -0.4, 0, 0, 0])
        # return np.array([0, 0, 0, 0, 0, np.pi]).astype(np.float32)
        # The initial config chosen from a reasonable looking retarget
        # return np.array(
        #     [-2.32716536, 0.89906459, -1.68806129, 0.97207676, 2.31516003, 1.38369078]
        # )
        return np.zeros(7)

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
        }

    @property
    def arm_type(self):
        return "single"

    @property
    def _eef_name(self):
        return "right_hand"

    @property
    def _robot_base(self):
        return "base"

    @property
    def default_mount(self):
        return "RethinkMount"
