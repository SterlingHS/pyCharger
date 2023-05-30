import wpilib
import Constants
from subsystems.DriveSystem import *
from subsystems.ArmSystem import *
from subsystems.ShoulderSystem import *


class RobotContainer():
    driverController = wpilib.XboxController(Constants.MAIN_JOYDRIVER_USB_PORT)

    m_drivesystem = DriveSystem()
    m_armsystem = ArmSystem()
    m_shouldersystem = ShoulderSystem()

    
    def __init__():
        pass

    def configureButtonBindings():
        pass

    def getAutonomousCommand():
        pass

    def update_smartboard():
        wpilib.SmartDashboard.putNumber()