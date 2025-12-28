# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Lumin                                                        #
# 	Created:      2/19/2025, 11:27:12 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

brain = Brain()

L1 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
L2 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
L3 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)
R1 = Motor(Ports.PORT18, GearSetting.RATIO_18_1, True)
R2 = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
R3 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
intake = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)
FishMech = Motor(Ports.PORT15, GearSetting.RATIO_36_1, False)

mogoClamp = DigitalOut(brain.three_wire_port.b)
arm = DigitalOut(brain.three_wire_port.a)
climb = DigitalOut(brain.three_wire_port.h)
controller_1 = Controller(PRIMARY)
isClamped = True
isArmOpen = False
isClimbOpen = False
isFishmegOpen = False

wheelToWheelDistance = 14.5
wheelRadius = 3.25
cmPerDegrees = wheelRadius * 2.54 * math.pi / 360 * 5 / 3


def drive(SpeedLeft, SpeedRight):
    L1.spin(FORWARD, SpeedLeft, VOLT)
    L2.spin(FORWARD, SpeedLeft, VOLT)
    L3.spin(FORWARD, SpeedLeft, VOLT)
    R1.spin(FORWARD, SpeedRight, VOLT)
    R2.spin(FORWARD, SpeedRight, VOLT)
    R3.spin(FORWARD, SpeedRight, VOLT)

def turnRight(deg, rpm):
    global wheelToWheelDistance, cmPerDegrees
    value = deg * wheelToWheelDistance * math.pi / 360 / cmPerDegrees * 2.54
    L1.spin_for(FORWARD, value, DEGREES, rpm, RPM, False)
    L2.spin_for(FORWARD, value, DEGREES, rpm, RPM, False)
    L3.spin_for(FORWARD, value, DEGREES, rpm, RPM, False)
    R1.spin_for(REVERSE, value, DEGREES, rpm, RPM, False)
    R2.spin_for(REVERSE, value, DEGREES, rpm, RPM, False)
    R3.spin_for(REVERSE, value, DEGREES, rpm, RPM, True) 

def turnLeft(deg, rpm):
    global wheelToWheelDistance, cmPerDegrees
    value = deg * wheelToWheelDistance * math.pi / 360 / cmPerDegrees * 2.54
    L1.spin_for(REVERSE, value, DEGREES, rpm, RPM, False)
    L2.spin_for(REVERSE, value, DEGREES, rpm, RPM, False)
    L3.spin_for(REVERSE, value, DEGREES, rpm, RPM, False)
    R1.spin_for(FORWARD, value, DEGREES, rpm, RPM, False)
    R2.spin_for(FORWARD, value, DEGREES, rpm, RPM, False)
    R3.spin_for(FORWARD, value, DEGREES, rpm, RPM, True) 

def moveBackward(distance, rpm):
    global cmPerDegrees
    deg = distance / cmPerDegrees
    L1.spin_for(REVERSE, deg, DEGREES, rpm, RPM, False)
    L2.spin_for(REVERSE, deg, DEGREES, rpm, RPM, False)
    L3.spin_for(REVERSE, deg, DEGREES, rpm, RPM, False)
    R1.spin_for(REVERSE, deg, DEGREES, rpm, RPM, False)
    R2.spin_for(REVERSE, deg, DEGREES, rpm, RPM, False)
    R3.spin_for(REVERSE, deg, DEGREES, rpm, RPM, True)

def moveForward(distance, rpm):
    global cmPerDegrees
    deg = distance / cmPerDegrees
    L1.spin_for(FORWARD, deg, DEGREES, rpm, RPM, False)
    L2.spin_for(FORWARD, deg, DEGREES, rpm, RPM, False)
    L3.spin_for(FORWARD, deg, DEGREES, rpm, RPM, False)
    R1.spin_for(FORWARD, deg, DEGREES, rpm, RPM, False)
    R2.spin_for(FORWARD, deg, DEGREES, rpm, RPM, False)
    R3.spin_for(FORWARD, deg, DEGREES, rpm, RPM, True) 
def moveStop():
    L1.stop()
    L2.stop()
    L3.stop()
    R1.stop()
    R2.stop()
    R3.stop()

def clampMogo():
    mogoClamp.set(False)

def unClampMogo():
    mogoClamp.set(True) 

def onevent_controller_1buttonL2_pressed_0():
    global isArmOpen
    if isArmOpen:
        arm.set(False)
        isArmOpen = False
    else:
        arm.set(True)
        isArmOpen = True
    

def onevent_controller_1buttonL1_pressed_0():
    global isClamped
    if isClamped:
        unClampMogo()
        isClamped = False
    else:
        clampMogo()
        isClamped = True

def onevent_controller_1buttonR1_pressed_0():
    intake.spin(FORWARD, 200)

def onevent_controller_1buttonR1_released_0():
    intake.stop()

def onevent_controller_1buttonR2_pressed_0():
    intake.spin(REVERSE, 200)

def onevent_controller_1buttonR2_released_0():
    intake.stop()

def onevent_controller_1buttonX_pressed_0():
    FishMech.spin_to_position(200, DEGREES, 100, RPM)

def onevent_controller_1buttonX_released_0():
    FishMech.spin_to_position(-10, DEGREES, 100, RPM)

def onevent_controller_1buttonUp_pressed_0():
    global isClimbOpen
    if isClimbOpen:
        climb.set(False)
        isClimbOpen = False
    else:
        climb.set(True)
        isClimbOpen = True 

def onevent_controller_1buttonRight_pressed_0():
    global isFishmegOpen
    if isFishmegOpen:
        FishMech.spin_to_position(-20, DEGREES , 100, RPM)
        isFishmegOpen = False
    else:
        FishMech.spin_to_position(180, DEGREES , 100, RPM)
        isFishmegOpen = True


def kirmizisaggarantee():
    unClampMogo()
    moveBackward(22.08*2.54, 70)
    wait(200, MSEC)
    turnLeft(32, 50)
    wait(200, MSEC)
    moveBackward(20.33*2.54, 70)
    clampMogo()
    wait(200, MSEC)
    intake.spin(FORWARD, 200)
    wait(200, MSEC)
    turnLeft(50, 70)
    wait(200, MSEC)
    moveForward(17.48*2.54, 70)
    wait(200, MSEC)
    turnLeft(190, 70)
    wait(200, MSEC)
    moveForward(35.13*2.54, 70)
    wait(200, MSEC)

def kirmizisagyedek():
    unClampMogo()
    FishMech.reset_position()
    FishMech.spin_to_position(-15, DEGREES, 70, RPM)
    moveBackward(22.08*2.54, 70)
    wait(200, MSEC)
    turnLeft(32, 50)
    wait(200, MSEC)
    moveBackward(20.33*2.54, 70)
    clampMogo()
    wait(200, MSEC)
    intake.spin(FORWARD, 200)
    wait(200, MSEC)
    turnLeft(50, 70)
    wait(200, MSEC)
    moveForward(10,70)
    moveBackward(10,70)
    moveForward(18.48*2.54, 70)
    wait(200, MSEC)
    turnLeft(200, 70)
    wait(1000,MSEC)
    moveForward(10,70)
    moveBackward(10,70)
    wait(200, MSEC)
    moveForward(30.13*2.54, 50)
    wait(200, MSEC)



    



def autonomous():
    brain.screen.clear_screen()
    # place automonous code here
    kirmizisagyedek()
    

def user_control():
    brain.screen.clear_screen()
    intake.stop()
    FishMech.reset_position()
    FishMech.spin_to_position(-20, DEGREES, 70, RPM)
    # place driver control in this while loop
    while True:
        SpeedLeft = (controller_1.axis3.position() + controller_1.axis1.position()) / 8.3
        SpeedRight = (controller_1.axis3.position() - controller_1.axis1.position()) / 8.3
        drive(SpeedLeft, SpeedRight)
        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
controller_1.buttonX.released(onevent_controller_1buttonX_released_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonR1.released(onevent_controller_1buttonR1_released_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
controller_1.buttonR2.released(onevent_controller_1buttonR2_released_0)
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
controller_1.buttonRight.pressed(onevent_controller_1buttonRight_pressed_0)

wait(15, MSEC)

# actions to do when the program starts
brain.screen.clear_screen()
