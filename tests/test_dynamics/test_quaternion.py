import numpy as np

from dynamics.quaternion import (
    normalize,
    conjugate,
    multiply,
    quaternion_to_dcm,
    dcm_to_quaternion
)


# =============================================================================
# TC-001
# Function : normalize()
# Requirement:
# The normalized quaternion shall have unit magnitude.
# =============================================================================

def test_normalize_returns_unit_quaternion():

    q = np.array([2.0, 3.0, 4.0, 5.0])

    q_norm = normalize(q)

    assert np.isclose(
        np.linalg.norm(q_norm),
        1.0,
        atol=1e-12
    )


# =============================================================================
# TC-002
# Function : normalize()
# Requirement:
# An already normalized quaternion shall remain unchanged.
# =============================================================================

def test_normalize_preserves_unit_quaternion():

    q = np.array([1.0, 0.0, 0.0, 0.0])

    q_norm = normalize(q)

    assert np.allclose(
        q,
        q_norm,
        atol=1e-12
    )


# =============================================================================
# TC-003
# Function : conjugate()
# Requirement:
# Quaternion conjugate shall negate only the vector part.
# =============================================================================

def test_quaternion_conjugate():

    q = np.array([1.0, 2.0, 3.0, 4.0])

    expected = np.array([1.0, -2.0, -3.0, -4.0])

    assert np.allclose(
        conjugate(q),
        expected,
        atol=1e-12
    )


# =============================================================================
# TC-004
# Function : multiply()
# Requirement:
# Identity quaternion shall be the multiplicative identity.
# =============================================================================

def test_identity_quaternion_multiplication():

    identity = np.array([1.0, 0.0, 0.0, 0.0])

    q = normalize(
        np.array([0.5, 0.2, -0.3, 0.4])
    )

    result = multiply(identity, q)

    assert np.allclose(
        result,
        q,
        atol=1e-12
    )


# =============================================================================
# TC-005
# Function : multiply()
# Requirement:
# Quaternion multiplied by its conjugate shall produce
# the identity quaternion.
# =============================================================================

def test_quaternion_times_conjugate():

    q = normalize(
        np.array([0.5, 0.2, 0.3, 0.4])
    )

    q_conj = conjugate(q)

    result = multiply(q, q_conj)

    expected = np.array([1.0, 0.0, 0.0, 0.0])

    assert np.allclose(
        result,
        expected,
        atol=1e-12
    )


# =============================================================================
# TC-006
# Function : quaternion_to_dcm()
# Requirement:
# Identity quaternion shall generate the identity DCM.
# =============================================================================

def test_identity_quaternion_to_dcm():

    q = np.array([1.0, 0.0, 0.0, 0.0])

    C = quaternion_to_dcm(q)

    assert np.allclose(
        C,
        np.eye(3),
        atol=1e-12
    )


# =============================================================================
# TC-007
# Function : quaternion_to_dcm()
# Requirement:
# Generated DCM shall be orthogonal.
# =============================================================================

def test_dcm_is_orthogonal():

    q = normalize(
        np.array([0.4, 0.3, 0.2, 0.1])
    )

    C = quaternion_to_dcm(q)

    assert np.allclose(
        C @ C.T,
        np.eye(3),
        atol=1e-12
    )


# =============================================================================
# TC-008
# Function : quaternion_to_dcm()
# Requirement:
# Generated DCM shall have determinant equal to +1.
# =============================================================================

def test_dcm_determinant():

    q = normalize(
        np.array([0.4, 0.3, 0.2, 0.1])
    )

    C = quaternion_to_dcm(q)

    assert np.isclose(
        np.linalg.det(C),
        1.0,
        atol=1e-12
    )


# =============================================================================
# TC-009
# Function : dcm_to_quaternion()
# Requirement:
# Identity DCM shall return the identity quaternion.
# =============================================================================

def test_identity_dcm_to_quaternion():

    C = np.eye(3)

    q = dcm_to_quaternion(C)

    expected = np.array([1.0, 0.0, 0.0, 0.0])

    assert np.allclose(
        q,
        expected,
        atol=1e-12
    )


# =============================================================================
# TC-010
# Function : quaternion_to_dcm(), dcm_to_quaternion()
# Requirement:
# Quaternion -> DCM -> Quaternion shall preserve attitude.
# =============================================================================

def test_round_trip_conversion():

    q = normalize(
        np.array([0.7, 0.2, 0.4, 0.5])
    )

    C = quaternion_to_dcm(q)

    q_new = dcm_to_quaternion(C)

    assert (
        np.allclose(q, q_new, atol=1e-12)
        or
        np.allclose(q, -q_new, atol=1e-12)
    )


# =============================================================================
# TC-011
# Function : multiply()
# Requirement:
# Quaternion multiplication shall be associative.
# =============================================================================

def test_quaternion_associativity():

    q1 = normalize(np.array([1.0, 2.0, 3.0, 4.0]))
    q2 = normalize(np.array([2.0, 1.0, 0.0, 1.0]))
    q3 = normalize(np.array([1.0, 0.5, 2.0, 1.5]))

    left = multiply(
        multiply(q1, q2),
        q3
    )

    right = multiply(
        q1,
        multiply(q2, q3)
    )

    assert np.allclose(
        left,
        right,
        atol=1e-12
    )