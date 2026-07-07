import numpy as np


def quest(V_N, V_B, w, k):
    """
    QUEST Attitude Determination Algorithm

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
    q_crp : ndarray (3,1)
        Optimal Classical Rodrigues Parameters.

    B_est_N : ndarray (3,3)
        Estimated Direction Cosine Matrix.
    """

    # ---------------------------------------------------------------------
    # Construct the Attitude Profile Matrix [B]
    # ---------------------------------------------------------------------

    B = np.zeros((3,3))

    for i in range(k):

        r = V_N[i].reshape(3,1)
        b = V_B[i].reshape(3,1)

        r = r / np.linalg.norm(r)
        b = b / np.linalg.norm(b)

        B += w[i] * (b @ r.T)

    # ---------------------------------------------------------------------
    # Compute sigma
    # ---------------------------------------------------------------------

    sigma = np.trace(B)

    # ---------------------------------------------------------------------
    # Compute S
    # ---------------------------------------------------------------------

    S = B + B.T

    # ---------------------------------------------------------------------
    # Compute Z
    # ---------------------------------------------------------------------

    Z = np.array([
        [B[1,2] - B[2,1]],
        [B[2,0] - B[0,2]],
        [B[0,1] - B[1,0]]
    ])

    # ---------------------------------------------------------------------
    # Construct Davenport Matrix [K]
    # ---------------------------------------------------------------------

    K = np.zeros((4,4))

    K[0,0] = sigma
    K[0,1:] = Z.flatten()

    K[1:,0] = Z.flatten()
    K[1:,1:] = S - sigma*np.eye(3)

    # ---------------------------------------------------------------------
    # Initial Eigenvalue Estimate
    # ---------------------------------------------------------------------

    lambda_old = np.sum(w)

    # ---------------------------------------------------------------------
    # Newton-Raphson Iteration
    # ---------------------------------------------------------------------

    #
    # Evaluate
    #
    # f(lambda)  = det(K - lambda*I)
    #
    # f'(lambda)
    #
    # Iterate until convergence
    #
    # lambda_new = lambda_old - f/f'
    #

    lambda_max = lambda_old      # Placeholder

    # ---------------------------------------------------------------------
    # Compute the Optimal CRP
    # ---------------------------------------------------------------------

    q_crp = np.linalg.inv(
        (lambda_max + sigma)*np.eye(3) - S
    ) @ Z

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
        [-q2,  q1,  0]
    ])

    B_est_N = (
        (1 - q_sq)*np.eye(3)
        + 2*np.outer(q_crp.flatten(), q_crp.flatten())
        - 2*q_cross
    ) / (1 + q_sq)

    

    return (
        B,
        sigma,
        S,
        Z,
        K,
        lambda_max,
        q_crp,
        B_est_N
    )