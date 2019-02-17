import wpilib
import ctre
import math

class Drive:
    ################################################
    #Handles actual driving and dealing with inputs#
    ################################################

    #The motor wont run unless the controller outputs above this
    DEADZONE = .1
    driveSPEED = .8

    #Establishes the motors from robot.py in this class
    motor_l1 = ctre.WPI_TalonSRX(3)
    motor_l2 = ctre.WPI_TalonSRX(4)
    motor_l3 = ctre.WPI_TalonSRX(5)

    motor_r1 = ctre.WPI_TalonSRX(6)
    motor_r2 = ctre.WPI_TalonSRX(7)
    motor_r3 = ctre.WPI_TalonSRX(8)

    #Establishes double solenoids for gear shifting
    doubleS = wpilib.DoubleSolenoid
    doubleS2 = wpilib.DoubleSolenoid

    #Required but not used
    def __init__(self):
        pass

    #Drives the robot using a tank drive
    def move(self, left, right):
        #Sets controller outputs to 0 if they are in the deadzone
        if math.fabs(left) < self.DEADZONE:
            left = 0

        if math.fabs(right) < self.DEADZONE:
            right = 0

        #Runs the motors at the values provided post-deadzone
        self.motor_l1.set(-left * self.driveSPEED)
        self.motor_l2.set(-left * self.driveSPEED)
        self.motor_l3.set(-left * self.driveSPEED)

        #Right side is negative so both sides spin the same way
        self.motor_r1.set(right * self.driveSPEED)
        self.motor_r2.set(right * self.driveSPEED)
        self.motor_r3.set(right * self.driveSPEED)

    def shift(self, direction):
        if (direction == 1):
            self.doubleS.set(2)
            self.doubleS2.set(2)
        else:
            self.doubleS.set(1)
            self.doubleS2.set(1)

    #Required but not used
    def execute(self):
            pass
