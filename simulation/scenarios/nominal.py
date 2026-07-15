"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Nominal Scenario
Purpose: Defines the nominal spacecraft attitude simulation scenario.
Author : ISHMAEL
License: MIT
===============================================================================
"""

import numpy as np

from simulation.scenario import Scenario


class NominalScenario(Scenario):
    """
    Nominal spacecraft attitude simulation.

    Assumptions
    -----------
    - Constant angular velocity
    - No disturbance torques
    - Sun sensor available
    - Magnetometer available
    - Ideal environment
    """

    def __init__(self):

        self.initial_quaternion = np.array([
            1.0,
            0.0,
            0.0,
            0.0
        ])

        self.initial_angular_velocity = np.deg2rad([
            0.5,
            0.2,
           -0.3
        ])

        self.simulation_time = 100.0

    def initialize(self):
        """
        Initialize the nominal scenario.
        """

        return {

            "initial_quaternion": self.initial_quaternion,

            "initial_angular_velocity": self.initial_angular_velocity,

            "simulation_time": self.simulation_time

        }

    def update(self, time, dt):
        """
        Update the scenario.

        The nominal scenario contains no time-varying events.
        """

        pass

    def is_complete(self, time):
        """
        Check whether the simulation is complete.
        """

        return time >= self.simulation_time