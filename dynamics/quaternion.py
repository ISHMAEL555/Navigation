import numpy as np


# =============================================================================
# Quaternion Utilities
# =============================================================================

def normalize(q):
    """
    Normalize a quaternion.

    Parameters
    ----------
    q : ndarray (4,)
        Quaternion [q0, q1, q2, q3]

    Returns
    -------
    ndarray (4,)
        Unit quaternion.
    """

    q = np.asarray(q, dtype=float)

    return q / np.linalg.norm(q)


# =============================================================================
# Quaternion Conjugate
# =============================================================================

def conjugate(q):
    """
    Quaternion conjugate.

    Parameters
    ----------
    q : ndarray (4,)

    Returns
    -------
    ndarray (4,)
    """

    q = np.asarray(q, dtype=float)

    return np.array([
        q[0],
        -q[1],
        -q[2],
        -q[3]
    ])


# =============================================================================
# Quaternion Multiplication
# =============================================================================

def multiply(q1, q2):
    """
    Hamilton quaternion multiplication.

    Parameters
    ----------
    q1 : ndarray (4,)
    q2 : ndarray (4,)

    Returns
    -------
    ndarray (4,)
    """

    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    return np.array([

        w1*w2 - x1*x2 - y1*y2 - z1*z2,

        w1*x2 + x1*w2 + y1*z2 - z1*y2,

        w1*y2 - x1*z2 + y1*w2 + z1*x2,

        w1*z2 + x1*y2 - y1*x2 + z1*w2

    ])


# =============================================================================
# Quaternion → DCM
# =============================================================================

def quaternion_to_dcm(q):
    """
    Convert quaternion to Direction Cosine Matrix.

    Parameters
    ----------
    q : ndarray (4,)

    Returns
    -------
    ndarray (3,3)
    """

    q = normalize(q)

    q0, q1, q2, q3 = q

    return np.array([

        [
            q0**2 + q1**2 - q2**2 - q3**2,
            2*(q1*q2 + q0*q3),
            2*(q1*q3 - q0*q2)
        ],

        [
            2*(q1*q2 - q0*q3),
            q0**2 - q1**2 + q2**2 - q3**2,
            2*(q2*q3 + q0*q1)
        ],

        [
            2*(q1*q3 + q0*q2),
            2*(q2*q3 - q0*q1),
            q0**2 - q1**2 - q2**2 + q3**2
        ]

    ])


# =============================================================================
# DCM → Quaternion
# =============================================================================

def dcm_to_quaternion(C):
    """
    Convert Direction Cosine Matrix to quaternion
    (Schaub & Junkins convention).

    Parameters
    ----------
    C : ndarray (3,3)

    Returns
    -------
    ndarray (4,)
    """

    tr = np.trace(C)

    if tr > 0:

        s = 2.0 * np.sqrt(tr + 1.0)

        q0 = 0.25 * s
        q1 = (C[1, 2] - C[2, 1]) / s
        q2 = (C[2, 0] - C[0, 2]) / s
        q3 = (C[0, 1] - C[1, 0]) / s

    elif (C[0, 0] > C[1, 1]) and (C[0, 0] > C[2, 2]):

        s = 2.0 * np.sqrt(1.0 + C[0, 0] - C[1, 1] - C[2, 2])

        q0 = (C[1, 2] - C[2, 1]) / s
        q1 = 0.25 * s
        q2 = (C[0, 1] + C[1, 0]) / s
        q3 = (C[0, 2] + C[2, 0]) / s

    elif C[1, 1] > C[2, 2]:

        s = 2.0 * np.sqrt(1.0 + C[1, 1] - C[0, 0] - C[2, 2])

        q0 = (C[2, 0] - C[0, 2]) / s
        q1 = (C[0, 1] + C[1, 0]) / s
        q2 = 0.25 * s
        q3 = (C[1, 2] + C[2, 1]) / s

    else:

        s = 2.0 * np.sqrt(1.0 + C[2, 2] - C[0, 0] - C[1, 1])

        q0 = (C[0, 1] - C[1, 0]) / s
        q1 = (C[0, 2] + C[2, 0]) / s
        q2 = (C[1, 2] + C[2, 1]) / s
        q3 = 0.25 * s

    return normalize(np.array([q0, q1, q2, q3]))