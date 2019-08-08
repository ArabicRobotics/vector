import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
import anki_vector
class Robot (object):
	cameraIsInit  = None
	vector =None
	isConnected = None
	@staticmethod
	def connect(timeout=10):
		try:
			Robot.getRobot()
			Robot.vector.connect(timeout=timeout)
			Robot.isConnected= True
			print (" Connected ! ")
			return True
		except Exception as e:
			print  ("Error on Connect :( "+str(e))
			Robot.isConnected = False
			logger = clsLog()
			logger.error(str(e))
			return False
	@staticmethod
	def disconnect():
		try:
			print (" get the robot for disconnect ")
			print (Robot.getRobot())
			Robot.vector.disconnect()
			Robot.isConnected= False
			print ("Disconnected  Successfully")
			return True
		except Exception as e:
			print  ("Error on disconnection "+str(e))
			Robot.isConnected = True
			logger = clsLog()
			logger.error(str(e))
			return False

	@staticmethod
	def boot():
		try:
			self.isRunning = True
			print ("Boot Successfully")
			return True
		except Exception as e:
			print  ("Error on boot"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
	@staticmethod
	def shutDown():
		try:
			self.isRunning = False
			return True
		except Exception as e:
			print  ("Error on shutdown"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
	@staticmethod
	def getRobot():
		try:
			if Robot.vector ==None:
				args = anki_vector.util.parse_command_args()    
				Robot.vector = anki_vector.Robot(args.serial,
enable_audio_feed=True,default_logging=True,
                           enable_custom_object_detection=True,
                           enable_nav_map_feed=True)
				return True
			else:
				return True
		except Exception as e:
			print  ("Error on get Robot"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False


def main():
	vector = Robot.getRobot()
	if vector:
		print ("Vector I got ")
	else: 
		print("Errrrror ")

	Robot.connect()

	Robot.disconnect()
if __name__ == "__main__":

	main()


