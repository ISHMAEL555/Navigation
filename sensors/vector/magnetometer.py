import numpy as np


class Magnetometer:
    """
    Ideal three-axis magnetometer.

    Measures the Earth's magnetic field direction in the
    spacecraft body frame.
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
        Generate a magnetometer measurement.

        Parameters
        ----------
        truth_model : TruthModel

        Returns
        -------
        ndarray (3,)
            Measured magnetic field vector
            expressed in the body frame.
        """

        state = truth_model.get_state()

        C_BN = state["dcm"]

        magnetic_body = C_BN @ self.reference_vector

        noise = np.random.normal(
            loc=0.0,
            scale=self.noise_std,
            size=3
        )

        measurement = magnetic_body + noise

        measurement /= np.linalg.norm(
            measurement
        )

        return measurement