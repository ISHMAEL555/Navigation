"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Simulation State
Purpose: Stores the current state of the navigation simulation.
Author : ISHMAEL
License: MIT
===============================================================================
"""

from dataclasses import dataclass

from dynamics.truth_model import TruthModel
from sensors.sensor_manager import SensorManager
from attitude_determination.algorithms.base_algorithm import (
    BaseAttitudeAlgorithm
)


@dataclass
class SimulationState:
    """
    Current state of the navigation simulation.
    """

    truth_model: TruthModel

    sensor_manager: SensorManager

    algorithm: BaseAttitudeAlgorithm

    time: float

    dt: float