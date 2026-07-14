import numpy as np


class SensorManager:
    """
    Manages spacecraft sensors and collects vector
    observations for attitude determination algorithms.
    """

    def __init__(self):

        self.vector_sensors = []

    def add_vector_sensor(self, sensor):
        """
        Register a vector sensor.
        """

        self.vector_sensors.append(sensor)

    def get_vector_observations(self, truth_model):
        """
        Collect vector observations from all registered
        vector sensors.

        Returns
        -------
        V_B : ndarray (N,3)
            Measured body-frame vectors.

        V_N : ndarray (N,3)
            Reference inertial-frame vectors.

        w : ndarray (N,)
            Sensor weights.
        """

        body_vectors = []
        reference_vectors = []
        weights = []

        for sensor in self.vector_sensors:

            body_vectors.append(
                sensor.measure(truth_model)
            )

            reference_vectors.append(
                sensor.reference_vector
            )

            weights.append(1.0)

        return (
            np.asarray(body_vectors),
            np.asarray(reference_vectors),
            np.asarray(weights)
        )