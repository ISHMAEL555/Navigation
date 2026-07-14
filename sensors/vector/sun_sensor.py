import numpy as np


class SunSensor:
    """
    Ideal coarse sun sensor.

    Measures the direction of the Sun in the spacecraft
    body frame.
    """

    def __init__(
        self,
        reference_vector,
        noise_std=0.0
    ):

        self.reference_vector = np.asarray(
            reference_vector,
            dtype=float
        )

        self.reference_vector /= np.linalg.norm(
            self.reference_vector
        )

        self.noise_std = noise_std

    def measure(self, truth_model):
        """
        Generate a Sun sensor measurement.

        Parameters
        ----------
        truth_model : TruthModel

        Returns
        -------
        ndarray (3,)
            Measured Sun vector in body frame.
        """

        state = truth_model.get_state()

        C_BN = state["dcm"]

        sun_body = C_BN @ self.reference_vector

        noise = np.random.normal(
            0.0,
            self.noise_std,
            3
        )

        measurement = sun_body + noise

        measurement /= np.linalg.norm(
            measurement
        )

        return measurement