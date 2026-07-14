import numpy as np

from dynamics.truth_model import TruthModel
from sensors.vector.magnetometer import Magnetometer


# =============================================================================
# TC-001
# Requirement:
# Magnetometer shall initialize with the specified reference vector and noise.
# =============================================================================

def test_magnetometer_initialization():

    reference = np.array([0.0, 1.0, 0.0])
    noise_std = 0.001

    sensor = Magnetometer(
        reference_vector=reference,
        noise_std=noise_std
    )

    assert np.allclose(
        sensor.reference_vector,
        reference,
        atol=1e-12
    )

    assert np.isclose(
        sensor.noise_std,
        noise_std,
        atol=1e-12
    )


# =============================================================================
# TC-002
# Requirement:
# Identity attitude shall return the reference vector.
# =============================================================================

def test_identity_attitude():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    sensor = Magnetometer(
        reference_vector=np.array([0.0, 1.0, 0.0]),
        noise_std=0.0
    )

    measurement = sensor.measure(truth)

    assert np.allclose(
        measurement,
        np.array([0.0, 1.0, 0.0]),
        atol=1e-12
    )


# =============================================================================
# TC-003
# Requirement:
# Measured vector shall remain normalized.
# =============================================================================

def test_measurement_normalized():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    sensor = Magnetometer(
        reference_vector=np.array([0.0, 1.0, 0.0]),
        noise_std=0.01
    )

    measurement = sensor.measure(truth)

    assert np.isclose(
        np.linalg.norm(measurement),
        1.0,
        atol=1e-12
    )


# =============================================================================
# TC-004
# Requirement:
# Measurement shall be a 3-element vector.
# =============================================================================

def test_measurement_dimension():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    sensor = Magnetometer(
        reference_vector=np.array([0.0, 1.0, 0.0])
    )

    measurement = sensor.measure(truth)

    assert measurement.shape == (3,)


# =============================================================================
# TC-005
# Requirement:
# Zero-noise measurements shall be repeatable.
# =============================================================================

def test_repeatability_without_noise():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    sensor = Magnetometer(
        reference_vector=np.array([0.3, 0.4, 0.5]),
        noise_std=0.0
    )

    m1 = sensor.measure(truth)
    m2 = sensor.measure(truth)

    assert np.allclose(
        m1,
        m2,
        atol=1e-12
    )


# =============================================================================
# TC-006
# Requirement:
# Measurements shall remain finite.
# =============================================================================

def test_measurements_are_finite():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    sensor = Magnetometer(
        reference_vector=np.array([0.0, 1.0, 0.0]),
        noise_std=0.01
    )

    for _ in range(100):

        measurement = sensor.measure(truth)

        assert np.all(np.isfinite(measurement))