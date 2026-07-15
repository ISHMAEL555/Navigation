"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Simulation Result
Purpose: Stores the results of a navigation simulation.
Author : ISHMAEL
License: MIT
===============================================================================
"""

from dataclasses import dataclass

import numpy as np


@dataclass
class SimulationResult:

    time: np.ndarray

    true_quaternion: np.ndarray

    estimated_dcm: np.ndarray

    attitude_error: np.ndarray