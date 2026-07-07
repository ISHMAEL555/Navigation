import numpy as np

# =============================================================================
# Valid Euler Sequences
# =============================================================================

SYMMETRIC_SEQUENCES = {
    (1, 2, 1), (1, 3, 1),
    (2, 1, 2), (2, 3, 2),
    (3, 1, 3), (3, 2, 3)
}

ASYMMETRIC_SEQUENCES = {
    (1, 2, 3), (1, 3, 2),
    (2, 1, 3), (2, 3, 1),
    (3, 1, 2), (3, 2, 1)
}

VALID_SEQUENCES = SYMMETRIC_SEQUENCES | ASYMMETRIC_SEQUENCES


# =============================================================================
# Elementary Direction Cosine Matrices (Schaub Convention)
# =============================================================================

def C1(angle):
    """Passive rotation about axis-1."""

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [1, 0, 0],
        [0, c, s],
        [0,-s, c]
    ], dtype=float)


def C2(angle):
    """Passive rotation about axis-2."""

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [ c, 0,-s],
        [ 0, 1, 0],
        [ s, 0, c]
    ], dtype=float)


def C3(angle):
    """Passive rotation about axis-3."""

    c = np.cos(angle)
    s = np.sin(angle)

    return np.array([
        [ c, s, 0],
        [-s, c, 0],
        [ 0, 0, 1]
    ], dtype=float)


ROTATION_MAP = {
    1: C1,
    2: C2,
    3: C3
}


# =============================================================================
# Euler Angles → Direction Cosine Matrix [BN]
# =============================================================================

def euler_to_dcm(sequence, euler_angles):
    """
    Computes the Direction Cosine Matrix [BN] from Euler angles.

    Parameters
    ----------
    sequence : tuple[int]
        Euler rotation sequence.
        Example: (3, 2, 1)

    euler_angles : array_like
        Euler angles in degrees.
        Example: [30, 20, -10]

    Returns
    -------
    BN : ndarray (3×3)
        Direction Cosine Matrix [BN].
    """

    sequence = tuple(sequence)

    if sequence not in VALID_SEQUENCES:
        raise ValueError(
            f"Invalid Euler sequence {sequence}."
        )

    angles = np.asarray(euler_angles, dtype=float)

    if angles.shape != (3,):
        raise ValueError(
            "Exactly three Euler angles are required."
        )

    # Convert degrees to radians
    angles = np.deg2rad(angles)

    # Construct the DCM
    BN = np.eye(3)

    # Schaub convention:
    # [BN] = C_last @ ... @ C_first
    for axis, angle in zip(sequence, angles):
        BN = ROTATION_MAP[axis](angle) @ BN

    return BN