import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
class Screen(object):
	def __init__(self, robot,socket=None):
		self.robot = robot
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
		self.robot.camera.init_camera_feed()
		self.robot.vision.enable_display_camera_feed_on_face(True)

	def hide_camera(self):
	    print('Close camera')
	    self.robot.vision.enable_display_camera_feed_on_face(False)
	    self.robot.camera.close_camera_feed()
if __name__ == "__main__":
	import anki_vector	
	import time
	args = anki_vector.util.parse_command_args()
	robot = anki_vector.Robot(args.serial)
	print (robot.connect())

	screen = Screen(robot)
	screen.boot()
	screen.show_Camera()
	time.sleep(10)
	screen.hide_camera()
	print (robot.disconnect())
	pass