import numpy as np


class Gyroscope:
    """
    Ideal gyroscope model with constant bias
    and white Gaussian measurement noise.
    """

    def __init__(
        self,
        bias=np.zeros(3),
        noise_std=0.0
    ):

        self.bias = np.asarray(bias, dtype=float)
        self.noise_std = noise_std

    def measure(self, truth_model):
        """
        Generate a gyroscope measurement.

        Parameters
        ----------
        truth_model : TruthModel

        Returns
        -------
        ndarray (3,)
            Measured body angular velocity [rad/s].
        """

        state = truth_model.get_state()

        omega_true = state["angular_velocity"]

        noise = np.random.normal(
            loc=0.0,
            scale=self.noise_std,
            size=3
        )

        omega_measured = (
            omega_true
            + self.bias
            + noise
        )

        return omega_measured

    def reset(self):
        """
        Reset sensor state.
        """

        pass