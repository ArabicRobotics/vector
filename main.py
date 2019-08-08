from clsLog import clsLog
import anki_vector
from clsSay import Say
class Loop (object):
    """This class for """ 
    def __init__(self,robot):
        """This initilization for 
        """ 
        try:
            self.robot = robot
            self.say = Say(self.robot)
            self.init()
            return
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return
    def init(self):
        """ This Method for  
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try: 
            self.robot.connect()
            self.say.say("Welcome to the World ! ")
            return True
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return False
    def shutDown(self):
        try:
			# Run your commands
            self.robot.anim.play_animation_trigger("GreetAfterLongTime")
			# Disconnect from Vector
            self.robot.disconnect()
        except Exception as e:
            logger = clsLog()
            logger.error(str(e)) 
            return False
def main():
	

    print (vector.status._status)
if __name__ == "__main__":
    main()

