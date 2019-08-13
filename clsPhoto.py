import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
import anki_vector	
from clsRobot import Robot
class Photo (object):
	def __init__(self,socket = None):
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
			self.isRunning = True
			print ("Boot Successfully")
			return True
		except Exception as e:
			print  ("Error on boot"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False

	def getImage(self,id=None , photoInfo=None):
		try:			
			for photo_info in Robot.vector.photos.photo_info:
				print(f"Opening photo {photo_info.photo_id}")
				photo = Robot.vector.photos.get_photo(photo_info.photo_id)
				if photo_info.photo_id ==id:
					return photo
				if photo_info == photoInfo:
					return photo
			return False
		except Exception as e:
			print ("error on Get Image "+str(e))	
			return False

	def takePhoto(self,fileName=None):
		try : 
			print ("start take photo ")
			image = Robot.vector.camera.capture_single_image()
			print ("print Image  :" )
			print (image)
			print ("End Print Image ")
			if fileName !=None:
				innerImage = image.raw_image
				innerImage.save(fileName)
			print ("takephoto Done ! ")
			return image
		except Exception as e:
			print  ("Error on Take photo"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False

	def shutDown(self):
		try:
			self.isRunning = False
			return True
		except Exception as e:
			print  ("Error on shutdown"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False

if __name__ == "__main__":
	import time
	photo = Photo()
	photo.boot()
	print (Robot.connect())

	photo.takePhoto("save.jpg")
	time.sleep(1)
	Robot.disconnect()
