import json
from clsLog import clsLog
from enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
import anki_vector


class Animation (object):
    def __init__(self, AsyncRobot=anki_vector.AsyncRobot(), socket=None):
        try:
            self.robot = AsyncRobot
            self.isRunning = False
            self.socket = socket
            return
        except Exception as e:
            print("Error on init "+str(e))
            logger = clsLog()
            logger.error(str(e))
            return
    def play(self,animation ='anim_turn_left_01'):
        try:
            self.robot.anim.play_animation(animation)
            return True
        except Exception as e:
            print("Error on play animation "+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False
    def listAnimation(self,play = 10):
        try:
            anim_names = self.robot.anim.anim_list
            i = 0
            for anim_name in anim_names:
                if play==True:
                    self.play(anim_name)
                    i = i +1
                if i>play:
                    return True
                print(anim_name)
        except Exception as e:
            print("Exception while List Animations: "+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False

    def boot(self):
        try:
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
    robot.robot.connect(timeout=20)
    robot.listAnimation(10)
    print(robot.play('anim_keepaway_idleliftdown_01'))

 
    robot.robot.disconnect()


if __name__ == "__main__":

    main()
