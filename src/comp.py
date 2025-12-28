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

# Defining Components
intake1 = Motor(Ports.PORT1)
intake2 = Motor(Ports.PORT2)

matchLoader = Pneumatics(brain.three_wire_port.a)
matchLoaderPos = 1
closet = Pneumatics(brain.three_wire_port.b)
closetPos = 0


# Defining Drivetrain
L1 = Motor(Ports.PORT11)
L2 = Motor(Ports.PORT12)
L3 = Motor(Ports.PORT13)
R1 = Motor(Ports.PORT18)
R2 = Motor(Ports.PORT19)
R3 = Motor(Ports.PORT20)

LeftSide = MotorGroup(L1,L2 ,L3, False)
RightSide = MotorGroup(R1,R2 ,R3, True)

wheelTravel = 220 # The circumference of the driven wheels.
trackWidth = 200 # The track width of the Drivetrain
wheelBase = 100 # The wheel base of the Drivetrain
units = MM # The units that represent wheelTravel, trackWidth and wheelBase
externalGearRatio = 60/36 # he gear ratio used to compensate drive distances if gearing is used.

dt = DriveTrain(LeftSide, RightSide, wheelTravel, trackWidth, wheelBase, units, externalGearRatio)

def intake():
    intake1.spin(FORWARD, 100, PERCENT, False)
    intake2.spin(REVERSE, 30, PERCENT, False)

def intakeStop():
    closetOpen()
    intake1.stop
    intake2.stop

def midGoal():
    closetClose()
    intake1.spin(FORWARD, 100, PERCENT, False)
    intake2.spin(REVERSE, 30, PERCENT, False)

def highGoal():
    closetOpen()
    intake1.spin(FORWARD, 100, PERCENT, False)
    intake2.spin(FORWARD, 100, PERCENT, False)


def lowGoal():
    intake1.spin(REVERSE, 100, PERCENT, False)
    intake2.spin(REVERSE, 100, PERCENT, False)

def matchLoaderOpen():
    if not matchLoaderPos:
        matchLoader.open

def matchLoaderClose():
    if matchLoaderPos:
        matchLoader.close

def matchLoaderToggle():
    if matchLoaderPos:
        matchLoaderClose()
    else:
        matchLoaderOpen()

def closetOpen():
    if not closetPos:
        closet.open

def closetClose():
    if closetPos:
        closet.close



def preAuton():
    brain.screen.clear_screen()
    brain.screen.print("Luminous")

def auton1():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    
    matchLoaderOpen()
    dt.drive_for(FORWARD, 200, MM)
    intake()
    wait(300, MSEC)
    dt.drive_for(REVERSE, 200, MM)
    intakeStop()
    matchLoaderClose()
    dt.drive_for(REVERSE, 1200, MM)
    highGoal()
    wait(400, MSEC)

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")

    while True:
        LeftSide.set_velocity((controller.axis3.position() + controller.axis1.position()), PERCENT)
        RightSide.set_velocity((controller.axis3.position() - controller.axis1.position()), PERCENT)
        controller.buttonR1.pressed(intake)
        controller.buttonR2.pressed(highGoal)
        controller.buttonL1.pressed(midGoal)
        controller.buttonL2.pressed(lowGoal)
        controller.buttonR1.released(intakeStop)
        controller.buttonR2.released(intakeStop)
        controller.buttonL1.released(intakeStop)
        controller.buttonL2.released(intakeStop)
        controller.buttonA.pressed(matchLoaderToggle)
        wait(15, MSEC)

        
        

comp = Competition(user_control, auton1)
preAuton()

