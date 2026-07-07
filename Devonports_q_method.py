# Davenport_q_method.py

import numpy as np

def q_method(V_N, V_B, w, n):
    """
    Davenport's q-Method Attitude Determination Algorithm

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
    B : ndarray (3,3)
        Attitude profile matrix.

    sigma : float
        Trace of the attitude profile matrix.

    S : ndarray (3,3)
        Symmetric matrix.

    Z : ndarray (3,1)
        Vector part of the K matrix.

    K : ndarray (4,4)
        Davenport's K matrix.

    Eigenvalues : ndarray (4,)
        Eigenvalues of K.

    Eigenvectors : ndarray (4,4)
        Eigenvectors of K.

    q : ndarray (4,)
        Optimal Euler parameter (quaternion).
    """

    # ---------------------------------------------------------------------
    # Construct the Attitude Profile Matrix [B]
    # ---------------------------------------------------------------------

    B = np.zeros((3, 3))

    for i in range(n):

        # Extract vectors
        r = V_N[i].reshape(3, 1)
        b = V_B[i].reshape(3, 1)

        # Normalize
        r = r / np.linalg.norm(r)
        b = b / np.linalg.norm(b)

        # Accumulate weighted outer product
        B += w[i] * (b @ r.T)

    # ---------------------------------------------------------------------
    # Compute sigma, S and Z
    # ---------------------------------------------------------------------

    sigma = np.trace(B)

    S = B + B.T

    Z = np.array([
        [B[1, 2] - B[2, 1]],
        [B[2, 0] - B[0, 2]],
        [B[0, 1] - B[1, 0]]
    ])

    # ---------------------------------------------------------------------
    # Construct Davenport's K Matrix
    # ---------------------------------------------------------------------

    K = np.zeros((4, 4))

    K[0, 0] = sigma
    K[0, 1:] = Z.flatten()

    K[1:, 0] = Z.flatten()
    K[1:, 1:] = S - sigma * np.eye(3)

    # ---------------------------------------------------------------------
    # Eigenvalue Problem
    # ---------------------------------------------------------------------

    Eigenvalues, Eigenvectors = np.linalg.eigh(K)

    # Largest eigenvalue
    idx = np.argmax(Eigenvalues)

    # Corresponding Euler parameter (Quaternion)
    q = Eigenvectors[:, idx]

    # Normalize
    q = q / np.linalg.norm(q)

    q0 = q[0]      # Scalar part
    q1 = q[1]
    q2 = q[2]
    q3 = q[3]

    B_est_N = np.array([
      [q0**2 + q1**2 - q2**2 - q3**2, 2*(q1*q2 + q0*q3), 2*(q1*q3 - q0*q2)],

      [2*(q1*q2 - q0*q3),q0**2 - q1**2 + q2**2 - q3**2, 2*(q2*q3 + q0*q1)],

      [2*(q1*q3 + q0*q2), 2*(q2*q3 - q0*q1),q0**2 - q1**2 - q2**2 + q3**2]])
    
    
    return B, sigma, S, Z, K, Eigenvalues, Eigenvectors, q, B_est_N
