# Spacecraft Navigation Verification Framework

A modular Python framework for the development, verification, and validation of spacecraft navigation systems. The framework provides an end-to-end environment for generating reference spacecraft states, simulating onboard navigation sensors, estimating spacecraft states, and quantitatively evaluating navigation performance against known truth.

---

## Motivation

Spacecraft navigation is fundamentally a state estimation problem. A spacecraft has no direct knowledge of its true state and must reconstruct it using imperfect measurements obtained from onboard sensors. Navigation algorithms combine these measurements to estimate quantities such as attitude, angular velocity, position, velocity, and sensor biases.

While numerous navigation algorithms are available in literature, comparatively few open-source projects provide a structured framework for objectively verifying and validating their performance. Most implementations focus on algorithm development, with limited emphasis on performance evaluation, repeatability, statistical analysis, or verification methodologies.

This project aims to bridge that gap by providing a modular verification framework that enables navigation algorithms to be evaluated under controlled simulation conditions using known reference truth.

---

## Philosophy

This framework is built around a single engineering question:

> **Given a spacecraft and its sensors, how accurately can a navigation algorithm reconstruct the true spacecraft state?**

Every component within the framework exists to answer this question.

Rather than treating navigation algorithms as isolated implementations, the framework evaluates complete navigation pipelines by comparing estimated spacecraft states against reference truth generated from physics-based simulations.

The objective is not only to develop navigation algorithms but also to produce quantitative engineering evidence demonstrating their accuracy, robustness, consistency, and computational performance.

---

## Framework Architecture

```text
                     Truth Model
                          │
                          ▼
                Environment Models
                          │
                          ▼
                  Sensor Models
                          │
                          ▼
              Navigation Measurements
                          │
                          ▼
              Navigation Algorithms
          (TRIAD • QUEST • EKF • MEKF • UKF)
                          │
                          ▼
                 Estimated State
                          │
                          ▼
           Verification & Validation
                          │
                          ▼
     Engineering Metrics • Reports • Plots
```

The framework separates the navigation problem into independent modules:

- **Truth Models** generate the reference spacecraft state.
- **Environment Models** simulate external references such as the Sun and Earth's magnetic field.
- **Sensor Models** generate realistic onboard measurements.
- **Navigation Algorithms** reconstruct the spacecraft state from sensor data.
- **Verification** compares estimated states against the known truth using quantitative performance metrics.

---

## Features

### Dynamics

- Spacecraft attitude dynamics
- Quaternion kinematics
- Reference truth model

### Sensor Models

- Gyroscope
- Sun Sensor
- Magnetometer
- Configurable Gaussian measurement noise

### Navigation

- TRIAD
- Davenport's q-Method
- QUEST
- (Planned) EKF
- (Planned) MEKF
- (Planned) UKF

### Verification

- Unit testing
- Integration testing
- Monte Carlo verification framework
- Automated statistical validation
- Performance metrics
- Verification campaigns

---

## Current Status

### Implemented

- Quaternion mathematics
- Spacecraft truth model
- Ideal sensor models
- Gaussian measurement noise
- TRIAD attitude determination
- Davenport's q-Method
- QUEST algorithm
- OLAE
- Comprehensive unit and integration tests

### In Development

- Environment models
- High-fidelity sensor models
- Extended Kalman Filter (EKF)
- Multiplicative Extended Kalman Filter (MEKF)
- Unscented Kalman Filter (UKF)
- Navigation performance campaigns
- Automated verification reports

---

## Roadmap

The framework is being developed incrementally with the following long-term objectives:

- Develop high-fidelity environment models.
- Improve sensor realism through bias, random walk, scale factor, and field-of-view modelling.
- Implement recursive navigation filters for spacecraft state estimation.
- Develop reusable verification campaigns for deterministic and stochastic navigation algorithms.
- Generate automated engineering evidence including plots, statistical analyses, and validation reports.
- Support objective comparison of spacecraft navigation algorithms using standardized performance metrics.

---

## License

This project is released under the MIT License.