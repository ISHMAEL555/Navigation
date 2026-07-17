"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module  : Truth State
Purpose : Noise-free spacecraft state.
Author  : ISHMAEL
License : MIT
===============================================================================
"""

from dataclasses import dataclass

from core.types import Quaternion
from core.types import Vector3


@dataclass(slots=True)
class TruthState:
    """
    Noise-free spacecraft state.

    Parameters
    ----------
    time : float
        Simulation time [s].

    position_eci : Vector3
        Position in the Earth-Centered Inertial frame [m].

    velocity_eci : Vector3
        Velocity in the Earth-Centered Inertial frame [m/s].

    quaternion : Quaternion
        Body-to-Inertial attitude quaternion.
        Scalar-first convention.

    angular_velocity : Vector3
        Body angular velocity [rad/s].
    """

    time: float

    position_eci: Vector3

    velocity_eci: Vector3

    quaternion: Quaternion

    angular_velocity: Vector3