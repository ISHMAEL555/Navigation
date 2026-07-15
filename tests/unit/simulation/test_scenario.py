"""
===============================================================================
Spacecraft Navigation Framework
-------------------------------------------------------------------------------
Module : Test Scenario
Purpose: Unit tests for the abstract Scenario interface.
Author : ISHMAEL
License : MIT
===============================================================================
"""

import pytest

from simulation.scenario import Scenario


class DummyScenario(Scenario):
    """
    Concrete implementation of the abstract Scenario class
    used for unit testing.
    """

    def initialize(self):
        """
        Initialize the scenario.
        """

        return {}

    def update(self, time, dt):
        """
        Update the scenario.
        """

        pass

    def is_complete(self, time):
        """
        Determine whether the scenario is complete.
        """

        return False


# =============================================================================
# TC-SIM-001
# =============================================================================

def test_scenario_is_abstract():
    """
    Verify that the abstract Scenario class
    cannot be instantiated.
    """

    with pytest.raises(TypeError):
        Scenario()


# =============================================================================
# TC-SIM-002
# =============================================================================

def test_dummy_scenario_instantiation():
    """
    Verify that a concrete implementation of
    Scenario can be instantiated.
    """

    scenario = DummyScenario()

    assert scenario is not None


# =============================================================================
# TC-SIM-003
# =============================================================================

def test_initialize_returns_dictionary():
    """
    Verify that initialize() executes successfully
    and returns a dictionary.
    """

    scenario = DummyScenario()

    result = scenario.initialize()

    assert isinstance(result, dict)


# =============================================================================
# TC-SIM-004
# =============================================================================

def test_update_executes():
    """
    Verify that update() executes without raising
    an exception.
    """

    scenario = DummyScenario()

    scenario.update(
        time=0.0,
        dt=1.0
    )


# =============================================================================
# TC-SIM-005
# =============================================================================

def test_is_complete_returns_boolean():
    """
    Verify that is_complete() returns
    a boolean value.
    """

    scenario = DummyScenario()

    result = scenario.is_complete(
        time=0.0
    )

    assert isinstance(result, bool)