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
controller_1 = Controller()

# Defining Components
intake1 = Motor(Ports.PORT1)
intake2 = Motor(Ports.PORT2)

matchLoader = Pneumatics(brain.three_wire_port.a)
matchLoaderPos = 0
closet = Pneumatics(brain.three_wire_port.b)
closetPos = 1


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
trackWidth = 330 # The track width of the Drivetrain
wheelBase = 355 # The wheel base of the Drivetrain
units = MM # The units that represent wheelTravel, trackWidth and wheelBase
externalGearRatio = 60/36 # The gear ratio used to compensate drive distances if gearing is used.

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

def onevent_controller_1buttonL2_pressed_0():
    pass

def onevent_controller_1buttonL2_released_0():
    pass

def onevent_controller_1buttonL1_pressed_0():
    pass

def onevent_controller_1buttonL1_released_0():
    pass

def onevent_controller_1buttonR1_pressed_0():
    pass

def onevent_controller_1buttonR1_released_0():
    pass

def onevent_controller_1buttonR2_pressed_0():
    pass

def onevent_controller_1buttonR2_released_0():
    pass

def onevent_controller_1buttonX_pressed_0():
    pass

def onevent_controller_1buttonX_released_0():
    pass

def onevent_controller_1buttonY_pressed_0():
    pass

def onevent_controller_1buttonY_released_0():
    pass

def onevent_controller_1buttonA_pressed_0():
    pass

def onevent_controller_1buttonA_released_0():
    pass

def onevent_controller_1buttonB_pressed_0():
    pass

def onevent_controller_1buttonB_released_0():
    pass
  
def onevent_controller_1buttonUp_pressed_0():
    pass

def onevent_controller_1buttonUp_released_0():
    pass

def onevent_controller_1buttonDown_pressed_0():
    pass

def onevent_controller_1buttonDown_released_0():
    pass

def onevent_controller_1buttonRight_pressed_0():
    pass

def onevent_controller_1buttonRight_released_0():
    pass

def onevent_controller_1buttonLeft_pressed_0():
    pass

def onevent_controller_1buttonLeft_released_0():
    pass


def menu():
    brain.screen.clear_screen()
    brain.screen.set_font(FontType.PROP20)
    brain.screen.set_pen_width(1)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.draw_rectangle(1, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(60, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(120, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(180, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(240, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(300, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(360, 179, 60, 60, Color.WHITE)
    brain.screen.draw_rectangle(420, 179, 59, 60, Color.WHITE)

    brain.screen.draw_rectangle(1, 119, 59, 59, Color.RED)
    brain.screen.draw_rectangle(419, 119, 59, 59, Color.RED)
    brain.screen.set_font(FontType.PROP40)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("Color")
    brain.screen.set_cursor(3, 1)
    brain.screen.print("Position")
    brain.screen.set_font(FontType.PROP40)
    brain.screen.set_cursor(25, 1)
    brain.screen.print("Luminous")
    


def preAuton():
    brain.screen.clear_screen()
    brain.screen.print("Luminous")

def autonomous():
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
        LeftSide.spin((controller_1.axis3.position() + controller_1.axis1.position()) / 8.3, VOLT)
        RightSide.spin((controller_1.axis3.position() - controller_1.axis1.position()) / 8.3, VOLT)
        wait(15, MSEC)


controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonL1.released(onevent_controller_1buttonL1_released_0)
controller_1.buttonL2.pressed(onevent_controller_1buttonL2_pressed_0)
controller_1.buttonL2.released(onevent_controller_1buttonL2_released_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
controller_1.buttonR1.released(onevent_controller_1buttonR1_released_0)
controller_1.buttonR2.pressed(onevent_controller_1buttonR2_pressed_0)
controller_1.buttonR2.released(onevent_controller_1buttonR2_released_0)
controller_1.buttonX.pressed(onevent_controller_1buttonX_pressed_0)
controller_1.buttonX.released(onevent_controller_1buttonX_released_0)
controller_1.buttonY.pressed(onevent_controller_1buttonY_pressed_0)
controller_1.buttonY.released(onevent_controller_1buttonY_released_0)
controller_1.buttonA.pressed(onevent_controller_1buttonA_pressed_0)
controller_1.buttonA.released(onevent_controller_1buttonA_released_0)
controller_1.buttonB.pressed(onevent_controller_1buttonB_pressed_0)
controller_1.buttonB.released(onevent_controller_1buttonB_released_0)
controller_1.buttonUp.pressed(onevent_controller_1buttonUp_pressed_0)
controller_1.buttonUp.released(onevent_controller_1buttonUp_released_0)
controller_1.buttonDown.pressed(onevent_controller_1buttonDown_pressed_0)
controller_1.buttonDown.released(onevent_controller_1buttonDown_released_0)
controller_1.buttonRight.pressed(onevent_controller_1buttonRight_pressed_0)
controller_1.buttonRight.released(onevent_controller_1buttonRight_released_0)
controller_1.buttonLeft.pressed(onevent_controller_1buttonLeft_pressed_0)
controller_1.buttonLeft.released(onevent_controller_1buttonLeft_released_0)

brain.screen.clear_screen()
comp = Competition(user_control, autonomous)