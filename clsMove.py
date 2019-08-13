import json
from clsLog import clsLog  
import time
from  enums import *
from clsUtilities import *
from clsjsoninfoLoader import GlobalInfo
import anki_vector
from clsRobot import Robot
from anki_vector.util import degrees, distance_mm, speed_mmps

def case(*args):
	return any((arg == switch.value for arg in args))
class Move (object):
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
	def drive_off_charger(self):
		try:
			if Robot.isConnected:
				Robot.vector.behavior.drive_off_charger()
				return True
			else :
				print("Robot is not Connected")
				return False
		except Exception as e:
			print  ("Error on drive off charger "+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
	def move(self,destance=200,speed=50):
		try:
			print ("Moving....")
			if Robot.isConnected:
				Robot.vector.behavior.drive_straight(distance_mm(destance), speed_mmps(speed))
				print ("Moving Done")
				return True
			else:
				print("Robot is not Connected")
				return False
		except Exception as e:
			print  ("Error on move"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False

	def moveTo(self,direction="F",duration=1):
		try:
			print ("Moving....")
			
			while(switch(direction)):
				if case("F"):
					print ("Moving forward")
					self.move(duration)
					return
				if case("B"):
					print ("Moving Backward")
					self.move(-1*duration)
					return
				if case("L"):
					print ("Turning Left")
					self.turn()
					return
				if case("R"):
					print ("turning Right")
					self.turn(-90)
					return
			return True
		except Exception as e:
			print  ("Error on move"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
	def turn(self,degree = 90):
		try:
			print("Turn Vector in place...")
			if Robot.isConnected:
				Robot.vector.behavior.turn_in_place(degrees(degree))
				print ("Turning  Done")
				return True
			else :
				print("Robot is not Connected")
				return False
		except Exception as e:
			print  ("Error on move"+str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
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
	Robot.getRobot()
	Robot.connect()
	
	move = Move()
	move.drive_off_charger()
	time.sleep(3)                  
	#move.turn(-90)
	move.moveTo("F",1)
	time.sleep(10)
	#move.move() 
	Robot.disconnect()
	pass