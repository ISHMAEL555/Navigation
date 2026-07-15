"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Test Nominal Scenario
Purpose: Unit tests for the NominalScenario class.
Author : ISHMAEL
License: MIT
===============================================================================
"""

import numpy as np

from simulation.scenarios.nominal import NominalScenario


# =============================================================================
# TC-SIM-006
# =============================================================================

def test_nominal_scenario_instantiation():
    """
    Verify that NominalScenario can be instantiated.
    """

    scenario = NominalScenario()

    assert scenario is not None


# =============================================================================
# TC-SIM-007
# =============================================================================

def test_initial_quaternion():
    """
    Verify the initial spacecraft attitude quaternion.
    """

    scenario = NominalScenario()

    expected = np.array([
        1.0,
        0.0,
        0.0,
        0.0
    ])

    np.testing.assert_allclose(
        scenario.initial_quaternion,
        expected
    )


# =============================================================================
# TC-SIM-008
# =============================================================================

def test_initial_angular_velocity():
    """
    Verify the initial spacecraft angular velocity.
    """

    scenario = NominalScenario()

    expected = np.deg2rad([
        0.5,
        0.2,
       -0.3
    ])

    np.testing.assert_allclose(
        scenario.initial_angular_velocity,
        expected
    )


# =============================================================================
# TC-SIM-009
# =============================================================================

def test_initialize():
    """
    Verify that initialize() returns the required
    simulation configuration.
    """

    scenario = NominalScenario()

    config = scenario.initialize()

    assert isinstance(config, dict)

    assert "initial_quaternion" in config
    assert "initial_angular_velocity" in config
    assert "simulation_time" in config


# =============================================================================
# TC-SIM-010
# =============================================================================

def test_is_complete():
    """
    Verify the scenario completion condition.
    """

    scenario = NominalScenario()

    assert scenario.is_complete(0.0) is False

    assert scenario.is_complete(
        scenario.simulation_time
    ) is True

    assert scenario.is_complete(
        scenario.simulation_time + 1.0
    ) is True