#Required libraries for the code to run
import wpilib
import ctre
import math
import magicbot
import logging


#Dashboard functionality
from wpilib.smartdashboard import SmartDashboard

# #Components go here
from components.drive import Drive
from components.lift import Lift
#from components.collection import Collection

class Bob(magicbot.MagicRobot):

    # lift = Lift
    # collection = Collection

    def createObjects(self):

        drive = Drive
        lift = Lift
        #collection = Collection

        self.compressor = wpilib.Compressor()

        #Establishing Dashboard
        self.HUD = wpilib.SmartDashboard

        self.limitSwitchIn = wpilib.DigitalInput(0)


        #Left motors
        self.motor_l1 = ctre.WPI_TalonSRX(8)
        self.motor_l2 = ctre.WPI_TalonSRX(9)
        self.motor_l3 = ctre.WPI_TalonSRX(10)

        #Right motors
        self.motor_r1 = ctre.WPI_TalonSRX(2)
        self.motor_r2 = ctre.WPI_TalonSRX(3)
        self.motor_r3 = ctre.WPI_TalonSRX(4)

        #Lift motors
        self.lift_motor1 = ctre.WPI_TalonSRX(1)
        self.lift_motor2 = ctre.WPI_TalonSRX(7)

        #Collection motors
        self.collection_motor = ctre.WPI_TalonSRX(11)

        self.climbing_motor1 = ctre.WPI_TalonSRX(5)
        self.climbing_motor2 = ctre.WPI_TalonSRX(12)

        #DoubleSolenoids
        self.doubleS = wpilib.DoubleSolenoid(0,1)
        self.doubleS2 = wpilib.DoubleSolenoid(2,3)

        #Controllers
        self.stick = wpilib.Joystick(0)
        self.stick2 = wpilib.Joystick(1)

def teleopPeriodic(self):

        #Tells robot to use tank drive system with 2 axis
        if(math.fabs(self.stick.getRawAxis(1)) > .1 or math.fabs(self.stick.getRawAxis(5)) > .1
                or self.stick.getRawButton(1) == 1):
            self.drive.move(self.stick.getRawAxis(1), self.stick.getRawAxis(5))
        if self.stick.getRawButton(5)== 1:
            self.drive.shift(1)
        elif self.stick.getRawButton(4) == 1:
            self.drive.shift(-1)

        self.lift.move(self.stick2.getRawAxis(1))

    #Tells the motor to move based on a sensor input or button
        if self.stick2.getRawButon(1):
            self.collection_motor.start()
        elif self.LimitSwitchIn.get():
            self.collection_motor.stop()
        if(self.stick2.getRawButton(1) == 1):
            self.collection_motor.move(1)

        elif (self.stick2.getRawButton(2) == 1):
            self.collection_motor.move(-1)

        else:
            self.collection_motor.move(0)

        #Values to dashboard for testing
        self.HUD.putNumber("Left Value:", ((int)(self.stick.getRawAxis(1) * 100)) / 100.0)
        self.HUD.putNumber("Right Value:", ((int)(self.stick.getRawAxis(5) * 100)) / 100.0)


if __name__ == "__main__" :
    wpilib.run(Bob)
