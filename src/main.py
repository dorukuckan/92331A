# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Doruk                                                        #
# 	Created:      12/27/2025, 12:45:10 AM                                      #
# 	Description:  Vex V5 Push Back 92331A                                      #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller = Controller()

# Defining Motors

L1 = Motor(Ports.PORT11)
L2 = Motor(Ports.PORT12)
L3 = Motor(Ports.PORT13)
R1 = Motor(Ports.PORT18)
R2 = Motor(Ports.PORT19)
R3 = Motor(Ports.PORT20)

LeftSide = MotorGroup(L1,L2 ,L3)
RightSide = MotorGroup(R1,R2 ,R3)

intake1 = Motor(Ports.PORT1)
intake2 = Motor(Ports.PORT2)


# Defining auton 
def forwardDist(cm, wait):
    LeftSide.spin_for(FORWARD, cm/25.9, TURNS, False)
    RightSide.spin_for(FORWARD, cm/25.9, TURNS, wait)

def backwardDist(cm, wait):
    LeftSide.spin_for(REVERSE, cm/25.9, TURNS, False)
    RightSide.spin_for(FORWARD, cm/25.9, TURNS, wait)

def forwardSec(s, wait):
    LeftSide.spin_for(FORWARD, s, SECONDS, False)
    RightSide.spin_for(REVERSE, s, SECONDS, wait)

def backwardSec(s, wait):
    LeftSide.spin_for(REVERSE, s, SECONDS, False)
    RightSide.spin_for(FORWARD, s, SECONDS, wait)

def turnLeft(degrees, wait):
    LeftSide.spin_for(REVERSE, degrees, TURNS, False)
    RightSide.spin_for(REVERSE, degrees, TURNS, wait)

def turnRight(degrees, wait):
    LeftSide.spin_for(FORWARD, degrees, TURNS, False)
    RightSide.spin_for(FORWARD, degrees, TURNS, wait)

# usage lowerIntake(FORWARD/REVERSE, TRUE/FALSE, "speed in %")
def lowerIntake(direction, state: bool, speed: int):
    if state == True :
        intake1.spin(direction, speed, PERCENT, False)
    if state == False :
        intake1.stop

# usage upperIntake(FORWARD/REVERSE, TRUE/FALSE, "speed in %")
def upperIntake(direction, state: bool, speed: int):
    if state == True :
        intake2.spin(direction, speed, PERCENT, False)
    if state == False :
        intake2.stop


def preAuton():
    brain.screen.clear_screen()
    brain.screen.print("Luminous")

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")

    forwardDist(20, True)
    turnRight(90, True)
    wait(20, MSEC)
    forwardDist(20, True)
    turnRight(90, True)
    wait(20, MSEC)
    forwardDist(20, True)
    turnRight(90, True)
    wait(20, MSEC)
    forwardDist(20, True)
    turnRight(90, True)
    wait(20, MSEC)

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")


    while True:
        LeftSide.set_velocity((controller.axis3.position() + controller.axis1.position()), PERCENT)
        RightSide.set_velocity((controller.axis3.position() - controller.axis1.position()), PERCENT)
        wait(20, MSEC)

comp = Competition(user_control, autonomous)
preAuton()
