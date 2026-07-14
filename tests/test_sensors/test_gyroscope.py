import numpy as np

from dynamics.truth_model import TruthModel
from sensors.gyroscope import Gyroscope


# =============================================================================
# TC-001
# Requirement:
# Gyroscope shall initialize with the specified bias and noise.
# =============================================================================

def test_gyroscope_initialization():

    bias = np.deg2rad([0.01, 0.02, 0.03])
    noise_std = np.deg2rad(0.005)

    gyro = Gyroscope(
        bias=bias,
        noise_std=noise_std
    )

    assert np.allclose(
        gyro.bias,
        bias,
        atol=1e-12
    )

    assert np.isclose(
        gyro.noise_std,
        noise_std,
        atol=1e-12
    )


# =============================================================================
# TC-002
# Requirement:
# Zero bias and zero noise shall return the true angular velocity.
# =============================================================================

def test_ideal_gyroscope():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.deg2rad([1.0, 2.0, 3.0])
    )

    gyro = Gyroscope()

    measurement = gyro.measure(truth)

    assert np.allclose(
        measurement,
        truth.get_angular_velocity(),
        atol=1e-12
    )


# =============================================================================
# TC-003
# Requirement:
# Constant bias shall be added to the measurement.
# =============================================================================

def test_constant_bias():

    omega = np.deg2rad([1.0, 2.0, 3.0])

    bias = np.deg2rad([0.1, 0.2, 0.3])

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        omega
    )

    gyro = Gyroscope(
        bias=bias,
        noise_std=0.0
    )

    measurement = gyro.measure(truth)

    assert np.allclose(
        measurement,
        omega + bias,
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

    gyro = Gyroscope()

    measurement = gyro.measure(truth)

    assert measurement.shape == (3,)


# =============================================================================
# TC-005
# Requirement:
# Noise shall have approximately zero mean.
# =============================================================================

def test_noise_mean():

    np.random.seed(42)

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    gyro = Gyroscope(
        noise_std=0.01
    )

    samples = np.array([
        gyro.measure(truth)
        for _ in range(10000)
    ])

    mean = np.mean(samples, axis=0)

    assert np.allclose(
        mean,
        np.zeros(3),
        atol=5e-4
    )


# =============================================================================
# TC-006
# Requirement:
# Noise standard deviation shall match the specified value.
# =============================================================================

def test_noise_standard_deviation():

    np.random.seed(42)

    sigma = 0.01

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    gyro = Gyroscope(
        noise_std=sigma
    )

    samples = np.array([
        gyro.measure(truth)
        for _ in range(10000)
    ])

    std = np.std(samples, axis=0)

    assert np.allclose(
        std,
        sigma,
        atol=5e-4
    )


# =============================================================================
# TC-007
# Requirement:
# Gyroscope shall correctly measure zero angular velocity.
# =============================================================================

def test_zero_angular_velocity():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.zeros(3)
    )

    gyro = Gyroscope()

    measurement = gyro.measure(truth)

    assert np.allclose(
        measurement,
        np.zeros(3),
        atol=1e-12
    )


# =============================================================================
# TC-008
# Requirement:
# Successive measurements shall be finite.
# =============================================================================

def test_measurements_are_finite():

    truth = TruthModel(
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.deg2rad([1.0, 2.0, 3.0])
    )

    gyro = Gyroscope(
        noise_std=0.01
    )

    for _ in range(100):

        measurement = gyro.measure(truth)

        assert np.all(np.isfinite(measurement))