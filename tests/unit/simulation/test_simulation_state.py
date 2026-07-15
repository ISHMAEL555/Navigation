"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Test Simulation State
Purpose: Unit tests for the SimulationState dataclass.
Author : ISHMAEL
License: MIT
===============================================================================
"""

from unittest.mock import MagicMock

from simulation.simulation_state import SimulationState


# =============================================================================
# TC-SIM-011
# =============================================================================

def test_simulation_state_instantiation():
    """
    Verify that a SimulationState object
    can be instantiated.
    """

    state = SimulationState(
        truth_model=MagicMock(),
        sensor_manager=MagicMock(),
        algorithm=MagicMock(),
        time=0.0,
        dt=0.1
    )

    assert state is not None


# =============================================================================
# TC-SIM-012
# =============================================================================

def test_truth_model_reference():
    """
    Verify that the TruthModel reference
    is stored correctly.
    """

    truth = MagicMock()

    state = SimulationState(
        truth_model=truth,
        sensor_manager=MagicMock(),
        algorithm=MagicMock(),
        time=0.0,
        dt=0.1
    )

    assert state.truth_model is truth


# =============================================================================
# TC-SIM-013
# =============================================================================

def test_sensor_manager_reference():
    """
    Verify that the SensorManager reference
    is stored correctly.
    """

    sensor_manager = MagicMock()

    state = SimulationState(
        truth_model=MagicMock(),
        sensor_manager=sensor_manager,
        algorithm=MagicMock(),
        time=0.0,
        dt=0.1
    )

    assert state.sensor_manager is sensor_manager


# =============================================================================
# TC-SIM-014
# =============================================================================

def test_algorithm_reference():
    """
    Verify that the navigation algorithm
    reference is stored correctly.
    """

    algorithm = MagicMock()

    state = SimulationState(
        truth_model=MagicMock(),
        sensor_manager=MagicMock(),
        algorithm=algorithm,
        time=0.0,
        dt=0.1
    )

    assert state.algorithm is algorithm


# =============================================================================
# TC-SIM-015
# =============================================================================

def test_simulation_time():
    """
    Verify that the simulation time
    and time step are stored correctly.
    """

    state = SimulationState(
        truth_model=MagicMock(),
        sensor_manager=MagicMock(),
        algorithm=MagicMock(),
        time=10.0,
        dt=0.5
    )

    assert state.time == 10.0

    assert state.dt == 0.5