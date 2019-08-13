import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
from clsRobot import Robot
class Screen(object):
	def __init__(self,socket=None):
		self.isRunning = False
		self.socket = socket
		return
	def boot(self):
		try:
			self.isRunning = True
			print ("Boot Successfully")
			return True
		except Exception as e:
			print  ("Error on boot"+str(e))
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
			



	def show_Camera(self):		
		print('Show camera')
		Robot.vector.camera.init_camera_feed()
		Robot.vector.vision.enable_display_camera_feed_on_face(True)

	def hide_camera(self):
		print('Close camera')
		Robot.vector.vision.enable_display_camera_feed_on_face(False)
		Robot.vector.camera.close_camera_feed()






if __name__ == "__main__":
	import anki_vector	
	import time
	Robot.connect()

	screen = Screen()
	screen.show_Camera()
	
	time.sleep(20)
	screen.hide_camera()
	print (Robot.disconnect())
	pass