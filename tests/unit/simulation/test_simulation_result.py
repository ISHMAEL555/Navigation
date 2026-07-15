"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Test Simulation Result
Purpose: Unit tests for the SimulationResult dataclass.
Author : ISHMAEL
License: MIT
===============================================================================
"""

import numpy as np

from simulation.simulation_result import SimulationResult


# =============================================================================
# TC-SIM-016
# =============================================================================

def test_simulation_result_instantiation():
    """
    Verify that a SimulationResult object
    can be instantiated.
    """

    result = SimulationResult(
        time=np.array([]),
        true_quaternion=np.empty((0, 4)),
        estimated_dcm=np.empty((0, 3, 3)),
        attitude_error=np.array([])
    )

    assert result is not None


# =============================================================================
# TC-SIM-017
# =============================================================================

def test_time_history_storage():
    """
    Verify that the time history is stored correctly.
    """

    time = np.array([0.0, 1.0, 2.0])

    result = SimulationResult(
        time=time,
        true_quaternion=np.empty((0, 4)),
        estimated_dcm=np.empty((0, 3, 3)),
        attitude_error=np.array([])
    )

    np.testing.assert_array_equal(
        result.time,
        time
    )


# =============================================================================
# TC-SIM-018
# =============================================================================

def test_true_quaternion_storage():
    """
    Verify that the true quaternion history
    is stored correctly.
    """

    q = np.array([
        [1.0, 0.0, 0.0, 0.0]
    ])

    result = SimulationResult(
        time=np.array([]),
        true_quaternion=q,
        estimated_dcm=np.empty((0, 3, 3)),
        attitude_error=np.array([])
    )

    np.testing.assert_array_equal(
        result.true_quaternion,
        q
    )


# =============================================================================
# TC-SIM-019
# =============================================================================

def test_estimated_dcm_storage():
    """
    Verify that the estimated DCM history
    is stored correctly.
    """

    dcm = np.array([
        np.eye(3)
    ])

    result = SimulationResult(
        time=np.array([]),
        true_quaternion=np.empty((0, 4)),
        estimated_dcm=dcm,
        attitude_error=np.array([])
    )

    np.testing.assert_array_equal(
        result.estimated_dcm,
        dcm
    )


# =============================================================================
# TC-SIM-020
# =============================================================================

def test_attitude_error_storage():
    """
    Verify that the attitude error history
    is stored correctly.
    """

    error = np.array([
        0.01,
        0.02,
        0.03
    ])

    result = SimulationResult(
        time=np.array([]),
        true_quaternion=np.empty((0, 4)),
        estimated_dcm=np.empty((0, 3, 3)),
        attitude_error=error
    )

    np.testing.assert_array_equal(
        result.attitude_error,
        error
    )