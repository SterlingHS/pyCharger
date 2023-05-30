import wpilib
import RobotContainer

class Robot(wpilib.TimedRobot):
    def RobotInit(self):
        global robotContainer
        robotContainer = RobotContainer() #Need to Make Robot Container
        self.timer = wpilib.Timer()

    def AutonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        robotContainer.configureButtonBindings()#Need to Create

    def teleopPeriodic(self):
        pass
        
if __name__ == "__main__":
    wpilib.run(Robot)