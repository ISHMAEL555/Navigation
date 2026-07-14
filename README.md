# Spacecraft Navigation Framework

A high-fidelity Python framework for spacecraft **attitude determination**, **attitude estimation**, and **sensor simulation**.

The objective of this repository is to develop a modular, verifiable, and extensible spacecraft navigation library following aerospace engineering principles. The framework models spacecraft attitude dynamics, realistic sensor measurements, classical attitude determination algorithms, and recursive state estimation techniques.

---

## Features

### Dynamics
- Quaternion mathematics
- Quaternion kinematics
- Spacecraft attitude truth model
- RK4 and Euler integration

### Sensor Models *(In Progress)*
- Gyroscope
- Star Tracker
- Sun Sensor
- Magnetometer
- Earth Horizon Sensor

### Attitude Determination *(Planned)*
- TRIAD
- Davenport's q-Method
- QUEST
- OLAE

### Attitude Estimation *(Planned)*
- Multiplicative Extended Kalman Filter (MEKF)
- Error-State Kalman Filter (ESKF)
- Unscented Kalman Filter (UKF)

### Verification
- Unit testing using PyTest
- Mathematical verification
- Monte Carlo validation *(Planned)*
- Consistency checks *(Planned)*

---

# Repository Structure

```text
Navigation/
│
├── dynamics/
│   ├── quaternion.py
│   ├── attitude_kinematics.py
│   └── truth_model.py
│
├── sensors/
│
├── attitude_determination/
│
├── attitude_estimation/
│
├── simulation/
│
├── tests/
│   ├── test_dynamics/
│   ├── test_sensors/
│   ├── test_attitude_determination/
│   └── test_attitude_estimation/
│
└── docs/
```

---

# Development Workflow

Each module is developed using the following engineering workflow:

```text
Requirements
      ↓
Implementation
      ↓
Unit Testing
      ↓
Verification
      ↓
Integration
```

Every module is verified before it is integrated into the simulation framework.

---

# Current Status

## Dynamics

| Module | Status |
|---------|:------:|
| Quaternion Mathematics | ✅ Verified |
| Attitude Kinematics | ✅ Verified |
| Truth Model | ✅ Verified |

---

## Sensors

| Module | Status |
|---------|:------:|
| Gyroscope | 🚧 |
| Star Tracker | ⏳ |
| Sun Sensor | ⏳ |
| Magnetometer | ⏳ |

---

## Attitude Determination

| Algorithm | Status |
|------------|:------:|
| TRIAD | ⏳ |
| Davenport's q Method | ⏳ |
| QUEST | ⏳ |
| OLAE | ⏳ |

---

## Attitude Estimation

| Algorithm | Status |
|------------|:------:|
| MEKF | ⏳ |
| ESKF | ⏳ |
| UKF | ⏳ |

---

# Verification Philosophy

This repository follows a verification-first development approach.

Every mathematical model is verified using automated unit tests before being integrated into higher-level navigation algorithms.

Verification includes:

- Mathematical property verification
- Numerical consistency checks
- Coordinate transformation validation
- Monte Carlo analysis (planned)
- Statistical consistency checks (planned)

---

# Roadmap

## Phase 1
- [x] Quaternion Mathematics
- [x] Attitude Kinematics
- [x] Truth Model

## Phase 2
- [ ] Gyroscope Model
- [ ] Star Tracker
- [ ] Sun Sensor
- [ ] Magnetometer

## Phase 3
- [ ] TRIAD
- [ ] Davenport's q-Method
- [ ] QUEST
- [ ] OLAE

## Phase 4
- [ ] MEKF
- [ ] ESKF
- [ ] UKF

## Phase 5
- [ ] Monte Carlo Simulation
- [ ] Performance Analysis
- [ ] Sensor Comparison
- [ ] Estimator Benchmarking

---

# References

1. Schaub, H., & Junkins, J. L. *Analytical Mechanics of Space Systems*.
2. Markley, F. L., & Crassidis, J. L. *Fundamentals of Spacecraft Attitude Determination and Control*.
3. Wertz, J. R. *Spacecraft Attitude Determination and Control*.
4. Wie, B. *Space Vehicle Dynamics and Control*.

---

# License

This project is released under the MIT License.