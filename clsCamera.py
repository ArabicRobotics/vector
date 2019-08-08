import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
from PIL import Image

class Camera (object):
	# globals: 
	isInit = None
	IsStreaming= None
	def __init__(self, robot,socket=None):
		try:
			self.robot = robot
			self.isRunning = False
			self.socket = socket
			return
		except Exception as e:
			print  ("Error on init "+str(e))
			logger = clsLog()
			logger.error(str(e))
			return 

	def boot(self):
		try:
			self.IsStreaming = self.getStreamingStatus()
			self.isRunning = True
			print ("Boot Successfully")
			return True
		except Exception as e:
			print  ("Error on boot"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False


	def init_camera_feed(self):
		try:				
			self.robot.camera.init_camera_feed()
			Camera.isInit=True
			return True
		except Exception as e:
			print ("Error , Cannot init Camera in  ClasCamera  "+ str(e))
			logger = clsLog()
			logger.error(str(e))
			return False


#region 
################# Class Main Functions

	def getlatest_image(self,fileName=None):
		"""  if fileName is not None then it will save the Image to the file name abd back it.   """
		try:
			if Camera.isInit != True:
				self.init_camera_feed()	
			image = self.robot.camera.latest_image
			#print (image)
			if fileName!= None:
				innerImage = image.raw_image
				innerImage.save(fileName)
			return image
		except Exception as e:
			print ("Error , Cannot getImage from class:  Camera "+ str(e))
			logger = clsLog()
			logger.error(str(e))
			return False

	

##### end Class Main Functions 
#endregion 






	def shutDown(self):
		try:
			try:
				if Camera.isInit ==True:
					self.stop_camera_feed()
			except Exception as e:
				print ("worning , Cannot close  Camera in ClasCamera  "+ str(e))
			self.isRunning = False
			return True
		except Exception as e:
			print  ("Error on shutdown"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False

	def stop_camera_feed(self):
		try:
			self.robot.camera.close_camera_feed()
			Camera.isInit = False
			return True
		except Exception as e:			
			print ("worning , Cannot init Camera in  ClasCamera  "+ str(e))
			logger = clsLog()
			logger.error(str(e))
			return False



	def getStreamingStatus(self):
		try: 
			self.IsStreaming = self.robot.camera.image_streaming_enabled()
			return self.IsStreaming
		except Exception as e:
			print ("worning , Cannot init Camera in  ClasCamera  "+ str(e))
			logger = clsLog()
			logger.error(str(e))
			return False


def main():
	import anki_vector	
	import time
	import numpy
	import scipy.misc
	from PIL import Image
	args = anki_vector.util.parse_command_args()
	robot = anki_vector.Robot(args.serial)
	print ("I will try to Connect ")
	print (robot.connect(timeout=10))
	camera = Camera(robot)
	camera.boot()
	img = camera.getlatest_image("hi.jpg")

	camera.shutDown()
	robot.disconnect()


if __name__ == "__main__":
	main()