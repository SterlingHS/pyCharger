import wpilib
import Constants

class ShoulderSystem():
    def __init__():
        shoulder_encoder = wpilib.Encoder(Constants.ENCODER_SHOULDER_A, Constants.ENCODER_SHOULDER_B, False, wpilib.Encoder.EncodingType.k4X)
        shoulderMotor1 = wpilib.Talon(Constants.SHOULDER_MOTOR_ONE)
        shoulderMotor2 = wpilib.Talon(Constants.SHOULDER_MOTOR_TWO)
        shoulderMotorGroup = wpilib.MotorControllerGroup(shoulderMotor1, shoulderMotor2)

        shoulderMotorGroup.setInverted(True)

      