"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Navigation Simulation
Purpose: Executes spacecraft navigation simulations.
Author : ISHMAEL
License: MIT
===============================================================================
"""

from simulation.simulation_state import SimulationState
from simulation.simulation_result import SimulationResult


class NavigationSimulation:
    """
    Executes a spacecraft navigation simulation.
    """

    def __init__(self, scenario):

        self.scenario = scenario

        self.state = None

    def initialize(self):
        """
        Initialize the simulation.
        """
        raise NotImplementedError

    def step(self):
        """
        Execute one simulation step.
        """
        raise NotImplementedError

    def run(self):
        """
        Execute the complete simulation.
        """
        raise NotImplementedError

    def reset(self):
        """
        Reset the simulation.
        """
        raise NotImplementedError