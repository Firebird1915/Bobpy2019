import wpilib
import ctre

class Lift:

    lift_motor1 = ctre.WPI_TalonSRX(1) #Change these numbers
    lift_motor2 = ctre.WPI_TalonSRX(2)

    #Speed modifier so it isn't too fast
    SPEED = .8
    DEADZONE = .2

    #Required but not used
    def __init__(self):
        pass

    #Tells the motor to move based on a given value
    def move(self, value):
        #Changes amount based on speed modifier
        if math.fabs(value) < self.DEADZONE:
            value = 0
        else:
            value = value - ((value / math.fabs(value)) * self.DEADZONE)

        if (value > 0 and self.limitSwitchB.get() == 1):
            value = 0
        # if (value < 0 and self.limitSwitchT.get() == 1):
        #     value = 0
        self.lift_motor1.set(value * self.SPEED)
        self.lift_motor2.set(value * -self.SPEED)

    #Also required, don't know what it does
    def execute(self):
            pass
