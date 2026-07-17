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

from dynamics.truth_model import TruthModel

from sensors.sensor_manager import SensorManager
from sensors.absolute.sun_sensor import SunSensor
from sensors.absolute.magnetometer import Magnetometer

from attitude_determination.algorithms.algorithm_factory import (
    AlgorithmFactory
)

from simulation.simulation_state import SimulationState


class NavigationSimulation:
    """
    Executes a spacecraft navigation simulation.
    """

    def __init__(
        self,
        scenario,
        algorithm_name="TRIAD",
        dt=0.1
    ):

        self.scenario = scenario

        self.algorithm_name = algorithm_name

        self.dt = dt

        self.state = None

        self.result = None

        self.current_time = 0.0

        self.step_number = 0

    def initialize(self):
        """
        Initialize the navigation simulation.
        """

        config = self.scenario.initialize()

        truth_model = TruthModel(

            config["initial_quaternion"],

            config["initial_angular_velocity"]

        )

        sensor_manager = SensorManager()

        sensor_manager.add_vector_sensor(

            SunSensor(

                reference_vector=config[
                    "sun_reference_vector"
                ]

            )

        )

        sensor_manager.add_vector_sensor(

            Magnetometer(

                reference_vector=config[
                    "magnetic_reference_vector"
                ]

            )

        )

        algorithm = AlgorithmFactory.create(

            self.algorithm_name

        )

        self.state = SimulationState(

            truth_model=truth_model,

            sensor_manager=sensor_manager,

            algorithm=algorithm,

            time=0.0,

            dt=self.dt

        )

        self.current_time = 0.0

        self.step_number = 0

    def step(self):
        """
        Execute one simulation step.
        """

        raise NotImplementedError

    def run(self):
        """
        Execute the simulation.
        """

        raise NotImplementedError

    def reset(self):
        """
        Reset the simulation.
        """

        self.state = None

        self.result = None

        self.current_time = 0.0

        self.step_number = 0