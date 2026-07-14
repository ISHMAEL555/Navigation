<div align="center">

# Navigation

### A Modular Spacecraft Attitude Navigation Framework

*Design • Simulation • Verification • Validation*

---

**Developing a modular spacecraft attitude navigation framework for spacecraft attitude dynamics, sensor modelling, attitude determination, state estimation, and verification using aerospace software engineering practices.**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-success)
![Tests](https://img.shields.io/badge/Tests-PyTest-green)
![License](https://img.shields.io/badge/License-MIT-orange)

</div>

---

# Overview

Modern spacecraft rely on robust navigation software to determine and estimate their attitude using measurements from onboard sensors. Developing such software requires far more than implementing estimation algorithms—it requires mathematically consistent dynamics, realistic sensor models, modular software architecture, systematic verification, and statistical performance evaluation.

This repository is an engineering project focused on developing a **modular spacecraft attitude navigation framework** from first principles. The framework integrates spacecraft attitude dynamics, sensor modelling, classical attitude determination algorithms, and future state estimation techniques within a verification-driven software architecture.

Unlike standalone implementations of individual algorithms, this project emphasizes **complete system integration**. Every component is independently developed, verified, and then integrated into a unified navigation pipeline capable of supporting future Monte Carlo campaigns, realistic sensor modelling, and recursive state estimation.

---

# Project Objectives

The long-term objective of this project is to build a reusable spacecraft attitude navigation framework that supports:

- Spacecraft attitude dynamics simulation
- Modular spacecraft sensor models
- Classical attitude determination algorithms
- Recursive state estimation algorithms
- Monte Carlo verification campaigns
- Performance benchmarking
- Software verification and validation

The project is designed to follow engineering practices commonly adopted in spacecraft Guidance, Navigation and Control (GNC) software development.

---

# Current Features

## Spacecraft Dynamics

- Quaternion Mathematics
- Quaternion Kinematics
- Truth Model
- Euler Integration
- Runge–Kutta 4 Integration

---

## Sensor Models

### Rate Sensors

- ✅ Gyroscope

### Vector Sensors

- ✅ Sun Sensor
- ✅ Magnetometer

### Absolute Sensors

- 🚧 Star Tracker *(Planned)*

---

## Attitude Determination

Implemented algorithms include

- ✅ TRIAD
- ✅ QUEST
- ✅ Davenport's q-Method
- ✅ OLAE

---

## Verification

- ✅ Unit Testing
- ✅ Integration Testing
- 🚧 Monte Carlo Verification *(In Progress)*

---

# Engineering Philosophy

The primary objective of this repository is **engineering reliability rather than algorithm implementation alone**.

Every module is developed using a structured verification workflow:

```text
Requirements
      │
      ▼
Mathematical Model
      │
      ▼
Software Implementation
      │
      ▼
Unit Verification
      │
      ▼
Integration Verification
      │
      ▼
Monte Carlo Verification
      │
      ▼
Performance Assessment
```

Each software component is independently verified before integration into the navigation framework. This development methodology promotes modularity, traceability, maintainability, and mathematical correctness throughout the project.

---

> **"Correct algorithms are important. Verified algorithms are essential."**

# Software Architecture

The framework is designed using a modular software architecture in which every subsystem has a single well-defined responsibility. Rather than implementing navigation algorithms as standalone scripts, the project separates spacecraft dynamics, sensor modelling, attitude determination, simulation, and verification into independent software components.

This modular approach allows individual components to be developed, verified, and extended without affecting the remainder of the navigation framework.

```text
                                    Navigation Framework

┌──────────────────────────────────────────────────────────────────────────────┐
│                              Spacecraft Truth Model                          │
│                                                                              │
│   • Quaternion Propagation                                                   │
│   • Attitude Kinematics                                                      │
│   • True Angular Velocity                                                    │
│   • True Direction Cosine Matrix                                             │
└──────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       │
                    ┌──────────────────┴──────────────────┐
                    │                                     │
                    ▼                                     ▼

        ┌───────────────────────┐          ┌────────────────────────┐
        │     Rate Sensors       │          │     Vector Sensors      │
        │                        │          │                         │
        │ • Gyroscope            │          │ • Sun Sensor           │
        │                        │          │ • Magnetometer         │
        │                        │          │ • Earth Sensor (Planned)│
        └───────────────────────┘          └────────────────────────┘
                    │                                     │
                    └──────────────────┬──────────────────┘
                                       │
                                       ▼
                         ┌──────────────────────────┐
                         │      Sensor Manager      │
                         │                          │
                         │ Measurement Collection   │
                         │ Sensor Synchronization   │
                         │ Data Packaging           │
                         └──────────────────────────┘
                                       │
                                       ▼
                    Body Vectors (V_B)
                    Reference Vectors (V_N)
                    Sensor Weights (w)
                                       │
                                       ▼
             ┌────────────────────────────────────────────┐
             │      Attitude Determination Algorithms      │
             │                                            │
             │  • TRIAD                                  │
             │  • QUEST                                  │
             │  • Davenport's q-Method                   │
             │  • OLAE                                   │
             └────────────────────────────────────────────┘
                                       │
                                       ▼
                         Estimated Spacecraft Attitude
                                       │
                                       ▼
                    ┌─────────────────────────────────┐
                    │ Verification & Performance       │
                    │                                 │
                    │ • Unit Testing                  │
                    │ • Integration Testing           │
                    │ • Monte Carlo Campaigns         │
                    │ • Statistical Analysis          │
                    └─────────────────────────────────┘
```

---

# Navigation Pipeline

The complete navigation workflow implemented in this repository is illustrated below.

```text
True Spacecraft Dynamics
            │
            ▼
Quaternion Propagation
            │
            ▼
Truth Attitude
            │
            ▼
────────────────────────────────────────────────────────────
                 Spacecraft Sensor Models
────────────────────────────────────────────────────────────
            │
            ├────────────► Gyroscope
            │
            ├────────────► Sun Sensor
            │
            └────────────► Magnetometer
            │
            ▼
Measured Sensor Data
            │
            ▼
Sensor Manager
            │
            ▼
Vector Observation Generation

      V_B        V_N        w

            │
            ▼
────────────────────────────────────────────────────────────
          Attitude Determination Algorithms
────────────────────────────────────────────────────────────

TRIAD

QUEST

Davenport's q-Method

OLAE

            │
            ▼
Estimated Attitude
            │
            ▼
Attitude Error Analysis
            │
            ▼
Verification & Validation
```

---

# Software Design Principles

The framework has been developed around several software engineering principles commonly adopted in aerospace software development.

### Modular Design

Every subsystem has a clearly defined responsibility. Dynamics, sensor models, navigation algorithms, simulations, and verification tools are implemented independently to minimize coupling and improve maintainability.

### Verification-Driven Development

Each software module is verified through dedicated unit tests before being integrated into higher-level simulations. This approach enables early detection of implementation errors and provides confidence in mathematical correctness.

### Separation of Concerns

Simulation logic, sensor modelling, dynamics propagation, and navigation algorithms remain independent. Algorithms operate only on measurement data and are not coupled to individual sensor implementations.

### Extensibility

The architecture is designed to support future expansion, including additional spacecraft sensors, recursive state estimation algorithms, environmental models, disturbance torques, and hardware-in-the-loop verification without requiring major architectural changes.

### Reusability

Reusable modules reduce duplicated implementations and simplify future algorithm development. Sensor models, truth models, and simulation infrastructure can be shared across multiple navigation algorithms and verification campaigns.

---

# Design Philosophy

This repository is not intended to be a collection of independent attitude determination algorithms. Instead, it is being developed as an integrated spacecraft navigation framework where each software component contributes to a complete Guidance, Navigation and Control (GNC) simulation environment.

The long-term objective is to provide a reusable platform for developing, testing, verifying, and benchmarking spacecraft navigation algorithms under realistic operating conditions.