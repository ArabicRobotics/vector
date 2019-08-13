from clsLog import clsLog
import anki_vector
from clsInputCapture import InputCatcher
from clsSocketServer import SocketServer
import threading
from clsjsoninfoLoader import GlobalInfo
import time
from clsRobot import Robot
class Loop (object):
    """This class for """ 
    def __init__(self):
        """This initilization for 
        """ 
        try:
            self.server = SocketServer()
            self.inputCatcher = None
            self.robot = Robot()
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
            self.threadServer = threading.Thread(target=self.server.Start)
            self.threadServer.start()
            time.sleep(2)
            if self.server.running:
                self.inputCatcher = InputCatcher(self.server)
                self.robot = Robot()
                Robot.getRobot()
                #self.threadLoop = threading.Thread(target=self.loop)
                #self.threadLoop.start()
                self.loop()
            else:
                print ("init error : Server is not running.. main will exit ")
                self.shutDown()
            return True
        except Exception as e:
            print ("Error in Main loop")
            print (e)
            logger = clsLog()
            logger.error(str(e))
            self.shutDown()
            return False
    def loop(self):
        try: 
            print ("mainLoop Function")
            data = None
            while GlobalInfo.Halt !=True:
                #print ("Mainloop")
                if self.server.receivedData != None:  
                    self.robot.connect()
                    print ("Data is :")
                    data = self.server.receivedData
                    print (self.server.receivedData)
                    #self.server.sendToClient("Data",str(self.server.receivedData))
                    self.inputCatcher.catch(data)
                    self.server.receivedData = None
                    data = None
                
            return True
        except Exception as e:
            print ("Error in main loop :")
            print(e)
            logger = clsLog()
            logger.error(str(e))
            self.shutDown()
            return False
        except KeyboardInterrupt:
            self.shutDown() 
    def shutDown(self):
        try:
            # Run your commands
            # Disconnect from Vector
            GlobalInfo.Halt = True
            self.robot.disconnect()
            self.server.shutDown()
            
        except Exception as e:
            logger = clsLog()
            logger.error(str(e)) 
            return False
def main():
	
    loop=  Loop()
    print ("Program END ! ")

if __name__ == "__main__":
    main()

