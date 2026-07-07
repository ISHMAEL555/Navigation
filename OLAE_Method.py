# OLAE.py

import numpy as np


def olae(V_N, V_B, w, k):
    """
    Optimal Linear Attitude Estimator (OLAE)

    Parameters
    ----------
    V_N : ndarray (k,3)
        Reference vectors expressed in the inertial frame.

    V_B : ndarray (k,3)
        Corresponding observations expressed in the body frame.

    w : ndarray (k,)
        Weights associated with each vector observation.

    k : int
        Number of vector observations.

    Returns
    -------
    s : ndarray (k,3)
        Sum vectors.

    d : ndarray (k,3)
        Difference vectors.

    S : ndarray (3k,3)
        Observation matrix.

    W : ndarray (3k,3k)
        Weight matrix.

    STWS : ndarray (3,3)
        Normal matrix.

    STWd : ndarray (3,1)
        Right-hand-side vector.

    q_crp : ndarray (3,1)
        Estimated Classical Rodrigues Parameters.

    B_est_N : ndarray (3,3)
        Estimated Direction Cosine Matrix.
    """

    # ---------------------------------------------------------------------
    # Normalize Input Vectors
    # ---------------------------------------------------------------------

    s = np.zeros((k,3))
    d = np.zeros((k,3))

    for i in range(k):

        r = V_N[i] / np.linalg.norm(V_N[i])
        b = V_B[i] / np.linalg.norm(V_B[i])

        # Sum and Difference vectors
        s[i] = b + r
        d[i] = b - r

    # ---------------------------------------------------------------------
    # Construct Observation Matrix
    # ---------------------------------------------------------------------

    S = np.zeros((3*k,3))

    for i in range(k):

        sx, sy, sz = s[i]

        S_i = np.array([
            [0,   -sz,  sy],
            [sz,   0,  -sx],
            [-sy, sx,   0]
        ])

        S[3*i:3*i+3, :] = S_i

    # ---------------------------------------------------------------------
    # Construct Difference Vector
    # ---------------------------------------------------------------------

    d_vec = d.reshape(3*k,1)

    # ---------------------------------------------------------------------
    # Construct Weight Matrix
    # ---------------------------------------------------------------------

    W = np.zeros((3*k,3*k))

    for i in range(k):

        W[3*i:3*i+3, 3*i:3*i+3] = w[i] * np.eye(3)

    # ---------------------------------------------------------------------
    # Weighted Least Squares
    # ---------------------------------------------------------------------

    STWS = S.T @ W @ S

    STWd = S.T @ W @ d_vec

    q_crp = np.linalg.solve(STWS, STWd)

    # ---------------------------------------------------------------------
    # CRP to DCM
    # ---------------------------------------------------------------------

    q1 = q_crp[0,0]
    q2 = q_crp[1,0]
    q3 = q_crp[2,0]

    q_sq = q1**2 + q2**2 + q3**2

    q_cross = np.array([
        [0,   -q3,  q2],
        [q3,   0,  -q1],
        [-q2,  q1,   0]
    ])

    B_est_N = (
        (1 - q_sq) * np.eye(3)
        + 2 * (q_crp @ q_crp.T)
        - 2 * q_cross
    ) / (1 + q_sq)

    return (
        s,
        d,
        S,
        W,
        STWS,
        STWd,
        q_crp,
        B_est_N
    )