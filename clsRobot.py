import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
import anki_vector
class Robot (object):
	isInitCamera  = None
	vector =None
	isConnected = None
	isCameraInit = None
	IsStreaming= None
	@staticmethod
	def connect(timeout=10,Force=False):
		try:
			Robot.getRobot()
			if Force ==True:
				Robot.vector.connect(timeout=timeout)
				Robot.isConnected =True
			else:
				if Robot.isConnected ==True:
					return True
				else:
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
	def stop_camera_feed():
		try:
			Robot.vector.camera.close_camera_feed()
			Robot.isInitCamera = False
			return True
		except Exception as e:			
			print ("worning , Cannot init Camera in  Robot  "+ str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
	@staticmethod
	def init_camera_feed():
		try:							
			Robot.vector.camera.init_camera_feed()
			Robot.isInitCamera=True
			return True
		except Exception as e:
			print ("Error , Cannot init Camera in  Robot  "+ str(e))
			logger = clsLog()
			logger.error(str(e))
			return False


	@staticmethod
	def getStreamingStatus():
		try: 
			IsStreaming = Robot.vector.camera.image_streaming_enabled()
			Robot.IsStreaming = IsStreaming
			return IsStreaming
		except Exception as e:
			print ("worning , Cannot init Camera in  Robot  "+ str(e))
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
			Robot.isConnected = None
			logger = clsLog()
			logger.error(str(e))
			return False

	@staticmethod
	def boot():
		try:
			isRunning = True
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
			isRunning = False
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
				Robot.vector = anki_vector.AsyncRobot(args.serial,
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


