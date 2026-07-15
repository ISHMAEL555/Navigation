"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Scenario
Purpose: Defines the abstract interface for spacecraft simulation scenarios.
Author : ISHMAEL
License: MIT
===============================================================================
"""

from abc import ABC, abstractmethod


class Scenario(ABC):
    """
    Base class for spacecraft simulation scenarios.

    A scenario defines the initial conditions, environment,
    and termination conditions for a simulation.
    """

    @abstractmethod
    def initialize(self):
        """
        Initialize the simulation scenario.

        Returns
        -------
        dict
            Initial simulation configuration.
        """
        pass

    @abstractmethod
    def update(self, time, dt):
        """
        Update the scenario.

        Parameters
        ----------
        time : float
            Current simulation time [s].

        dt : float
            Simulation time step [s].
        """
        pass

    @abstractmethod
    def is_complete(self, time):
        """
        Determine whether the simulation has completed.

        Parameters
        ----------
        time : float
            Current simulation time [s].

        Returns
        -------
        bool
            True if the simulation is complete.
        """
        pass