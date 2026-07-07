import numpy as np


def triad(V_N, V_B):
    """
    TRIAD Attitude Determination Algorithm

    Parameters
    ----------
    V_N : ndarray (k,3)
        Reference vectors expressed in the inertial frame.

    V_B : ndarray (k,3)
        Corresponding observations expressed in the body frame.

    Returns
    -------
    B_est_T : ndarray (3,3)
        Estimated TRIAD frame expressed in the body frame.

    NT : ndarray (3,3)
        TRIAD frame expressed in the inertial frame.

    B_est_N : ndarray (3,3)
        Estimated Direction Cosine Matrix [B_est N].
    """

    # ---------------------------------------------------------------------
    # Use the first two vector observations
    # ---------------------------------------------------------------------

    v1_N = V_N[0]
    v2_N = V_N[1]

    v1_B = V_B[0]
    v2_B = V_B[1]

    # ---------------------------------------------------------------------
    # Normalize the Reference Vectors
    # ---------------------------------------------------------------------

    v1_N = v1_N / np.linalg.norm(v1_N)
    v2_N = v2_N / np.linalg.norm(v2_N)

    # ---------------------------------------------------------------------
    # Normalize the Body Observation Vectors
    # ---------------------------------------------------------------------

    v1_B = v1_B / np.linalg.norm(v1_B)
    v2_B = v2_B / np.linalg.norm(v2_B)

    # ---------------------------------------------------------------------
    # Construct the Inertial TRIAD Frame
    # ---------------------------------------------------------------------

    t1_N = v1_N

    t2_N = np.cross(v1_N, v2_N)
    t2_N = t2_N / np.linalg.norm(t2_N)

    t3_N = np.cross(t1_N, t2_N)

    NT = np.column_stack((t1_N, t2_N, t3_N))

    # ---------------------------------------------------------------------
    # Construct the Body TRIAD Frame
    # ---------------------------------------------------------------------

    t1_B = v1_B

    t2_B = np.cross(v1_B, v2_B)
    t2_B = t2_B / np.linalg.norm(t2_B)

    t3_B = np.cross(t1_B, t2_B)

    B_est_T = np.column_stack((t1_B, t2_B, t3_B))

    # ---------------------------------------------------------------------
    # Estimated Attitude
    # ---------------------------------------------------------------------

    B_est_N = B_est_T @ NT.T

    return B_est_T, NT, B_est_N