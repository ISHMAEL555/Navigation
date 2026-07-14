import numpy as np

from .attitude_kinematics import propagate_rk4
from .quaternion import quaternion_to_dcm


class TruthModel:
    """
    Spacecraft attitude truth model.

    Propagates the true spacecraft attitude using the prescribed
    body angular velocity.
    """

    def __init__(self, q0, omega):

        self.q = np.asarray(q0, dtype=float)
        self.omega = np.asarray(omega, dtype=float)

    def propagate(self, dt):
        """
        Propagate the truth model by one time step.
        """

        self.q = propagate_rk4(
            self.q,
            self.omega,
            dt
        )

    def get_quaternion(self):
        """
        Returns the current true quaternion.
        """
        return self.q.copy()

    def get_dcm(self):
        """
        Returns the current true Direction Cosine Matrix.
        """
        return quaternion_to_dcm(self.q)

    def get_angular_velocity(self):
        """
        Returns the true body angular velocity.
        """
        return self.omega.copy()

    def get_state(self):
        """
        Returns the complete spacecraft truth state.
        """

        return {
            "quaternion": self.get_quaternion(),
            "dcm": self.get_dcm(),
            "angular_velocity": self.get_angular_velocity()
        }