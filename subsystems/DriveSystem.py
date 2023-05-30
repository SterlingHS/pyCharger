import Constants
import wpilib
import wpilib.drive


class DriveSystem():
    leftFront = wpilib.Talon(Constants.DRIVETRAIN_LEFT_FRONT)
    leftRear = wpilib.Talon(Constants.DRIVETRAIN_LEFT_BACK)
    rightFront = wpilib.Talon(Constants.DRIVETRAIN_RIGHT_BACK)
    rightRear = wpilib.Talon(Constants.DRIVETRAIN_RIGHT_BACK)
    mLeft = wpilib.MotorControllerGroup(leftFront, leftRear)
    mRight = wpilib.MotorControllerGroup(rightFront, rightRear)
    mDrive = wpilib.drive.DifferentialDrive(mLeft, mRight)

    #PUT IN NAVX DEVICE: NEEDS AHRS FROM KAUAILABS

    def __init__(self):
        self.leftRear.setInverted(True)
        self.leftFront.setInverted(True)
        self.rightRear.setInverted(False)
        self.rightFront.setInverted(False)
        

    def periodic():
        pass

    def simulationPeriodic():
        pass

    def arcademDrive(self, xSpeed, zRotation):
        self.mDrive.arcadeDrive(-xSpeed, -zRotation)
        self.leftRear.setVoltage(self.mDrive.arcadeDrive)

    def stop(self):
        self.leftFront.stopMotor()
        self.rightFront.stopMotor()
        self.leftRear.stopMotor()
        self.rightRear.stopMotor()
    
   