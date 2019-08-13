import json
import time
from clsLog import clsLog
from enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
import anki_vector
from clsRobot import Robot

class Animation (object):
    def __init__(self, socket=None):
        try:
            self.isRunning = False
            self.socket = socket
            return
        except Exception as e:
            print("Error on init "+str(e))
            logger = clsLog()
            logger.error(str(e))
            return
    def play(self,animation ='anim_blackjack_speech_tts_01',sleep=3):
        try:
            Robot.getRobot()
            Robot.vector.behavior.drive_off_charger()
            Robot.vector.anim.play_animation(animation)
            time.sleep(sleep)
            return True
        except Exception as e:
            print("Error on play animation "+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False
    def listAnimation(self,play = None):
        try:
            Robot.getRobot()
            anim_names = Robot.vector.anim.anim_list
            i = 0
            for anim_name in anim_names:
                if play!=None:
                    print ("Play "+str(anim_name))
                    self.play(anim_name)
                    
                    i = i +1
                    if i>play-1:
                        return True
                print(anim_name)
        except Exception as e:
            print("Exception while List Animations: "+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False

    def boot(self):
        try:
            Robot.connect()
            self.isRunning = True
            print("Boot Successfully")
            return True
        except Exception as e:
            print("Error on boot"+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False

    def shutDown(self):
        try:
            self.isRunning = False
            return True
        except Exception as e:
            print("Error on shutdown"+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False


def main():
	
	
    robot = Animation()
    Robot.connect()
    robot.listAnimation(10)
    print(robot.play('anim_keepaway_idleliftdown_01'))

 
    Robot.disconnect()


if __name__ == "__main__":

    main()
