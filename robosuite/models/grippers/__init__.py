from .gripper_factory import gripper_factory
from .gripper_model import GripperModel
from .gripper_tester import GripperTester
from .jaco_three_finger_gripper import (JacoThreeFingerDexterousGripper,
                                        JacoThreeFingerGripper)
from .null_gripper import NullGripper
from .panda_gripper import PandaGripper
from .rethink_gripper import RethinkGripper
from .robotiq_85_gripper import Robotiq85Gripper
from .robotiq_140_gripper import Robotiq140Gripper
from .robotiq_three_finger_gripper import (RobotiqThreeFingerDexterousGripper,
                                           RobotiqThreeFingerGripper)
from .wiping_gripper import WipingGripper
from .xarm_gripper import XarmGripper

GRIPPER_MAPPING = {
    "RethinkGripper": RethinkGripper,
    "PandaGripper": PandaGripper,
    "JacoThreeFingerGripper": JacoThreeFingerGripper,
    "JacoThreeFingerDexterousGripper": JacoThreeFingerDexterousGripper,
    "WipingGripper": WipingGripper,
    "Robotiq85Gripper": Robotiq85Gripper,
    "Robotiq140Gripper": Robotiq140Gripper,
    "RobotiqThreeFingerGripper": RobotiqThreeFingerGripper,
    "RobotiqThreeFingerDexterousGripper": RobotiqThreeFingerDexterousGripper,
    "XarmGripper": XarmGripper,
    None: NullGripper,
}

ALL_GRIPPERS = GRIPPER_MAPPING.keys()
