import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
from PIL import Image
from clsRobot import Robot
class Camera (object):
	# globals: 
	Robot.isInit = None
	IsStreaming= None
	def __init__(self,socket=None):
		try:			
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
			Robot.getRobot()
			Robot.connect()
			self.isRunning = True
			print ("Boot Successfully")
			return True
		except Exception as e:
			print  ("Error on boot"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False





#region 
################# Class Main Functions
	def getlatest_image(self,fileName=None):
		"""  if fileName is not None then it will save the Image to the file name abd back it.   """
		try:
			print("init Camera to Get lastst Image")
			Robot.init_camera_feed()	
			image = Robot.vector.camera.latest_image
			#print (image)
			if fileName!= None:
				innerImage = image.raw_image
				innerImage.save(fileName)
			print("get las")
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
				pass
			except Exception as e:
				print ("worning , Cannot close  Camera in ClasCamera  "+ str(e))
			self.isRunning = False
			return True
		except Exception as e:
			print  ("Error on shutdown"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False




def main():
	import anki_vector	
	import time
	import numpy
	import scipy.misc
	from PIL import Image

	camera = Camera()
	camera.boot()
	print("I will get the latest Image")
	img = camera.getlatest_image("hi.jpg")
	print("get the latest Image.. passed")

	camera.shutDown()
	Robot.disconnect()


if __name__ == "__main__":
	main()