# VEX V5RC Team 92331A — Luminous ("Apollo")

![VEX V5](https://img.shields.io/badge/Competition-VEX%20V5RC-red?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-C%2B%2B%20%2F%20Python-blue?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-PROS%20%2F%20VEXcode-orange?style=for-the-badge)

Official robot software repository for **Team 92331A (Luminous)** and our competition robot **"Apollo"**, competing in the **VEX V5 Robotics Competition (V5RC)**.

---

## Overview

This repository contains the control software, autonomous routines, and subsystem abstractions engineered for **Apollo**. The codebase is designed for modularity, deterministic autonomous execution, and responsive teleoperated control.

## Hardware & Subsystems

| Subsystem | Actuators / Sensors | Description |
| :--- | :--- | :--- |
| **Drivetrain** | `[e.g., 6-Motor 11W, 450 RPM, 3.25" Omni]` | `[Tank / Arcade]` drive with `[IMU / Tracking Wheels]` |
| **Intake / Conveyor** | `[e.g., 11W Smart Motor + Optical Sensor]` | High-speed game element acquisition and sorting |
| **Scoring Mechanism** | `[e.g., Lady Brown / Clamp / Catapult]` | `[PID / Macro]`-controlled scoring mechanism |
| **Pneumatics** | `[e.g., Double-acting solenoids]` | Mogo clamp, doinker, and mechanism actuation |

## Software Architecture & Features

* **Framework:** `[PROS 4 / VEXcode Pro V5 / LemLib / EZ-Template]`
* **Odometry & Localization:** `[2-Wheel + IMU Odometry / Dead-reckoning with IMU heading correction]`
* **Motion Control:**
  * Custom lateral and angular **PID controllers** with slew rate limiting.
  * `[Boomerang / Pure Pursuit / Motion Profiling]` for smooth trajectory tracking.
* **Autonomous Selector:** On-brain GUI / controller selector supporting `[Red/Blue Left, Right, and Programming Skills]` routines.
* **Driver Assist Macros:** Automated `[scoring angles / color sorting / anti-jam logic]` during the 1:45 driver control period.

## Project Structure

```text
92331A/
├── include/           # Header files, hardware port definitions, and PID constants
├── src/
│   ├── main.cpp       # Competition template (initialize, autonomous, opcontrol)
│   ├── subsystems/    # Drivetrain, intake, clamp, and mechanism controllers
│   └── autons/        # Match autonomous and Programming Skills routines
└── Makefile / project # Build configuration
