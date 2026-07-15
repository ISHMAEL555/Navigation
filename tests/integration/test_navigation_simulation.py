"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Navigation Simulation Integration Tests
Purpose: Verify NavigationSimulation initialization.
Author : ISHMAEL
License: MIT
===============================================================================
"""

from simulation.navigation_simulation import NavigationSimulation
from simulation.scenarios.nominal import NominalScenario


def test_navigation_simulation_initialization():
    """
    TC-INT-001

    Verify that NavigationSimulation initializes correctly.
    """

    simulation = NavigationSimulation(
        scenario=NominalScenario()
    )

    simulation.initialize()

    assert simulation.state is not None

    assert simulation.state.truth_model is not None

    assert simulation.state.sensor_manager is not None

    assert simulation.state.algorithm is not None

    assert simulation.current_time == 0.0