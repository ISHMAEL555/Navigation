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