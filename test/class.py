import json
from clsLog import clsLog  
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
class MyClass (object):
	def __init__(self, robot,socket = None):
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
if __name__ == "__main__":
	pass