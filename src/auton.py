# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       auton.py                                                      #
# 	Author:       Doruk                                                        #
# 	Created:      12/27/2025, 12:45:10 AM                                      #
# 	Description:  Vex V5 Push Back 92331A                                      #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math
import time

brain = Brain()
controller = Controller()

# Defining Drivetrain
L1 = Motor(Ports.PORT11)
L2 = Motor(Ports.PORT12)
L3 = Motor(Ports.PORT13)
R1 = Motor(Ports.PORT18)
R2 = Motor(Ports.PORT19)
R3 = Motor(Ports.PORT20)

LeftSide = MotorGroup(L1,L2 ,L3, False)
RightSide = MotorGroup(R1,R2 ,R3, True)

'''


         ┌───────────────────────┐
        ┌─┐                     ┌─┐
        │ │                     │ │ ─ ─ ─ 
        └─┘                     └─┘     ▲
         │                       │      │
        ┌─┐                     ┌─┐     │
        │ │                     │ │     │   wheelBase = 100mm
        └─┘                     └─┘     │
         │                       │      │
        ┌─┐                     ┌─┐     ▼
        │ │                     │ │ ─ ─ ─ 
        └─┘                     └─┘        
         └───────────────────────┘
         |                       |
         |                       |
         |                       |
         |◄─────────────────────►|
            trackWidth = 200mm
'''

wheelTravel = 220 # The circumference of the driven wheels.
trackWidth = 200 # The track width of the Drivetrain
wheelBase = 100 # The wheel base of the Drivetrain
externalGearRatio = 1 # The gear ratio used to compensate drive distances if gearing is used.
units = MM # The units that represent wheelTravel, trackWidth and wheelBase
rpm_max = 200 * externalGearRatio # The maximum revolutions per minute of the drive motors.
v_max = (rpm_max * wheelTravel/10) / 60 # The maximum linear velocity of the drivetrain.
a = v_max / 0.25 # The maximum linear acceleration of the drivetrain.
s_acc = (v_max**2) / (2 * a)
s_dec = (v_max**2) / (2 * a)
s_min = s_acc + s_dec # The minimum distance required to reach maximum velocity.
v_max_cm_per_sec = (rpm_max * wheelTravel/10) / 60.0 


def move(target_distance_cm):
    
    if target_distance_cm <= s_min:
        v_reach = math.sqrt(a * target_distance_cm / 2.0)
        t_acc = v_reach / a
        t_total = 2 * t_acc
        apply_triangular_profile(v_reach, t_acc, t_total)
    else:
        t_acc = v_max_cm_per_sec / a
        s_const = target_distance_cm - s_min
        t_const = s_const / v_max_cm_per_sec
        t_total = 2 * t_acc + t_const
        apply_trapezoidal_profile(v_max_cm_per_sec, t_acc, t_const, t_total)

def apply_trapezoidal_profile(v_max, t_acc, t_const, t_total):
    start_time = time.time()
    while True:
        t = time.time() - start_time
        if t >= t_total:
            LeftSide.stop()
            RightSide.stop()
            break
        
        if t < t_acc:
            speed = (v_max / t_acc) * t

        elif t < t_acc + t_const:
            speed = v_max

        else:
            t_dec_start = t_acc + t_const
            speed = v_max - (v_max / t_acc) * (t - t_dec_start)
        

        pwm = speed / v_max_cm_per_sec * 100  
        if pwm > 100:
            pwm = 100
        LeftSide.spin(FORWARD, pwm, PERCENT)
        RightSide.spin(FORWARD, pwm, PERCENT)

        

def apply_triangular_profile(v_reach, t_acc, t_total):
    start_time = time.time()
    while True:
        t = time.time() - start_time
        if t >= t_total:
            LeftSide.stop()
            RightSide.stop()
            break
        
        if t < t_acc:
            speed = (v_reach / t_acc) * t
        else:
            speed = v_reach - (v_reach / t_acc) * (t - t_acc)
        
        pwm = speed / v_max_cm_per_sec * 100
        if pwm > 100:
            pwm = 100
        LeftSide.spin(FORWARD, pwm, PERCENT)
        RightSide.spin(FORWARD, pwm, PERCENT)

def turn(angle_degrees):
    turn_circumference = math.pi * trackWidth
    distance_per_wheel = (angle_degrees / 360.0) * turn_circumference
    if angle_degrees > 0:
        LeftSide.spin(FORWARD, 50, PERCENT)
        RightSide.spin(REVERSE, 50, PERCENT)
    else:
        LeftSide.spin(REVERSE, 50, PERCENT)
        RightSide.spin(FORWARD, 50, PERCENT)
    
    time_needed = abs(distance_per_wheel) / v_max_cm_per_sec
    wait(time_needed * 1000, MSEC)
    
    LeftSide.stop()
    RightSide.stop()


def autonomus():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")

    move(100)
    wait(20, MSEC)
    turn(180)
    wait(20, MSEC)
    move(200)
    wait(20, MSEC)
    turn(-180)
    wait(20, MSEC)
    move(150)
    wait(20, MSEC)
    turn(180)
    wait(20, MSEC)
    move(50)

    

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")

    while True:
        LeftSide.set_velocity((controller.axis3.position() + controller.axis1.position()), PERCENT)
        RightSide.set_velocity((controller.axis3.position() - controller.axis1.position()), PERCENT)
        wait(15, MSEC)

        
        
comp = Competition(user_control, autonomus)