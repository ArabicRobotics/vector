import threading
from clsLog import clsLog
from enums import *
from clsjsoninfoLoader import GlobalInfo
from clsRobot import Robot
from enum import Enum    
from clsLog import clsLog
from clsMove import Move
import json
from collections import namedtuple
from clsServerUtilities import ServerUtilities
from clsSocketServer import SocketServer
import time

def case(*args):
	return any((arg == switch.value for arg in args))
class InputCatcher (object):
	"""This class for catch commands and requests by JSON , and do actions and 
	This initilization for get , set and boot , /catch , catch direct command and excecute the command , send the result to client.
	""" 
	def __init__(self,socket):
		"""This initilization for get , define RemoRobo class
		""" 
		try: 
			"""define the remorobo robot object"""
			"""define the socket Object"""
			self.socket= socket
			self.move = Move(self.socket)
			#print "InputCAtcher Got the socket" + str(socket)            
			return
		except Exception as e:
			logger = clsLog()
			logger.error(str(e))
			return

	def catch(self,text =None):
	    """ This Method for Catch input json text and do whatever inside it.
	    @type  paramName: Bool
	    @param paramName : Description
	    @rtype:  Boolean
	    @return: True : everything went fine
	    False : Something went wrong
	    """ 
	    try: 
	        # decode and Do what ever in the json
	        result = self.decode(text)            
	        return result
	    except Exception as e:
	        print ("exception in CAtch "+str(e))
	        logger = clsLog()
	        logger.error(str(e))
	        return False
          
	def decode(self,text =None):
	    """ This Method for  decoding the text came  and Excecuting it.
	    @type  text: String
	    @param text : the incomming text to decode and excecute.
	    @rtype:  Boolean
	    @return: True : everything went fine
	    False : Something went wrong
	    @rtype:  json
	    @return: string : Error exception 
	    """ 
	    try: 
	        # Parse JSON into an object with attributes corresponding to dict keys.
	        #testData ---- Debug ----
	        # text = '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":1}}}' 
	        # example for short Command: 
	        #   text =  '{"op":"command","value":"testConnection"}'
	        command= json.loads(text)
	        if command["op"] =="command":
	            # Excecute command
	            return self.directCommand(command["value"])
	        else:  
	            try:
	                jsonObject = json.loads(text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
	                #print jsonObject.op, jsonObject.device, jsonObject.details.name,jsonObject.details.data.op , jsonObject.details.data.n,jsonObject.details.data.s
	                
	                print ("jsonObject :  "+ str(jsonObject))     
	                #list1 = text.split(self.separator)     
	                # Do the JSon content COMMAND      
	                doResult = self.__do(jsonObject)
	                
	                return doResult
	            except Exception as e:
	                self.socket.sendToClient("nativestring",str(e),enumEventType.Error)
	                print  ("error in Decoder1 : "+str(e))
	                logger = clsLog()
	                logger.error(str(e))
	                return False
	    #except sys.excepthook as s:
	    #    Event("Error in decode" + s)            
	    #    return False
	    except Exception as e:
	        self.socket.sendToClient("nativestring",str(e),enumEventType.Error)
	        print  ("error in Decoder2 : "+str(e))
	        logger = clsLog()
	        logger.error(str(e))
	        return False


	def directCommand(self,command =True):
	        """ This Method for  excecute direct commands to the robots , 
	        available commands : 
	        - checkConnection (Check the connection and )
	        @type  paramName: Bool
	        @param paramName : Description
	        @rtype:  Boolean
	        @return: True : everything went fine
	        False : Something went wrong
	        """ 
	        try: 
	            if "checkConnection" in command :
	                print ("SEND TO CLIENT TESTED! ")
	                return self.socket.sendToClient("directcommand",True,enumEventType.Success)
	            else:
	                #return self.socket.sendToClient("directcommand",True,enumEventType.Success)
	                return self.socket.sendToClient("directcommand","bad Direct Command",enumEventType.Error)
	            return False
	        except Exception as e:
	            self.socket.sendToClient("directcommand",str(e),enumEventType.Error)
	            logger = clsLog()
	            logger.error(str(e))
	            return False

            
            
	def __do(self,jsonObject):
	    """ This Method for  perform the action with json object data  get or set
	    @type  jsonObject: json
	    @param jsonObject : json  object
	    @rtype:  Boolean
	    @return: True : everything went fine
	    False : Something went wrong
	    """ 
	    try: 
	        # comunication Type  0 = Do , 1 = get
	        # robotID , Id  for the robot
	        #Device, Leds,Movement,Camera,....
	        # command type : Raw / programming 
	        #command String ...  
	        print ("Command is from __do : "+str(jsonObject) )
	        print (jsonObject  ) 
	        operation =jsonObject.op
	        device = jsonObject.device
	        print ("robot Object "+ str(device))
	        # filter operations (get , set )        
	        while(switch(operation)):
	            if case(enumComunicationType.get.name): 
	                # parameter operation is get"
	                while(switch(device)):
	                    if case("robot"):
	                        robot = jsonObject.details
	                        #print "[inputCatcher ,__do ] option is get Robot"
	                        return self.getRobot(robot)
	                return   True
	            if case(enumComunicationType.set.name):
	                #operations is Set.
	                while(switch(device)):
	                    if case("robot"):
	                        robot = jsonObject.details
	                        ##print "[inputCatcher ,__do ] option is set Robot"
	                        # set the robot according to the command                            
	                        return self.setRobot(robot)
	                return   True 
	            return    True
	        return True
	    except Exception as e:
	        logger = clsLog()
	        logger.error(str(e))
	        return False 
	def getRobot(self,robot = None):
	        """ This Method for  get the robot and do the task , sent the result to client and return false or true.
	        @type  parameterList: enumRobotAttributes.(Leds/moving/...).value
	        @param parameterList : geting robot data from client robots or server to the lient.
	        @rtype:  Boolean
	        @return: True : everything went fine
	        False : Something went wrong
	        """ 
	        try: 
	        # switching Device or Function 
	            while(switch(robot)):                                
	                if case(enumRobotAttributes.Leds.value):
	                    print ("[inputCatcher ,get ] get Leds ")
	                    return   True
	                if case(enumRobotAttributes.Moving.value):
	                    print ("[inputCatcher ,get ] get Moving")
	                    return True
	                if case(enumRobotAttributes.Chat.value):
	                    print ("Input Robot is Chat")
	                    return True
	                return     True                 
	            print ("Done")
	            return True
	        except Exception as e:
	            self.socket.sendToClient("failed to make getRobot",str(e),enumEventType.Error)
	            logger = clsLog()
	            logger.error(str(e))
	            return False

 
	def setRobot(self,robot =None):
		""" This Method for set some robot values or do some operations according to robot parameters.(robot will send the result automaticly to the client.)
		robot will set Leds , Move currently  
		@type  robot: Robot object. 
		@param robot : Robot and data to set  like :  example 1 Leds : text = '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":1}}}' 
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			# example 1 Leds : text = '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":1}}}' 
			
			#example 2 :move : text = '{"op":"set","device":"robot","details":{"name": "Moving", "data": {"op": "m", "n": 1,"d":1}}}' 
			print ("setRobot start. ")
			print ("Set "+ str(robot.name))
			
			### switch Between id and function 			
			while(switch(robot.name)):    
				#LEDS Robot ######## leds ##################
				if case(enumRobotAttributes.Moving.value.description):
					print ("set Moving " )   
		
					while(switch(robot.data.op)):
						if case("m"): ## move ##
							#print "   Move Motor "
							direction = str(robot.data.d)
							#print "Movement By Char = "+str(robot.data.d)
							duration = 0
							nextStep = None
							try:
								duration = eval(str(robot.data.s))
								#print "duration : "+str(duration)
								if  duration is not None:									 
									nextStep = str(robot.data.nextStep)
									#print "NextStep  : "+str(nextStep)
									#print robot.data.s,robot.data.nextStep,robot.data.d
							except:
								
								print (robot.data.s,robot.data.nextStep,robot.data.d)
							
							#print "I will do move with parameters : Direction : "+str(direction)+ " Duration : "+str(duration)+" nextStep "+ nextStep
							#self.move.drive_off_charger()
							self.move.moveTo(direction,duration*50)
							time.sleep(duration)
							print ("Thanks moving ! ")
							#threadMove = threading.Thread(target= self.move.move,args = (direction,duration,nextStep))
							#self.socket.sendToClient("move","moving to: "+str(direction),enumEventType.Success)
							#threadMove.start()
							return True
						return True
					return  True 
				return True                 			
			return True
		except Exception as e:
			print (e)
			self.socket.sendToClient("failed to make Action",str(e),enumEventType.Error)
	
			logger = clsLog()
			logger.error(str(e))
			return False


	def shutDown(self,robot =None):
		""" This Method for
		@type  paramName: Bool
		@param paramName : Description
		@rtype:  Boolean
		@return: True : everything went fine
		False : Something went wrong
		""" 
		try: 
			#print "shutdown start. "
			#Event("InputCatcher Shutdown End")
			return True
		except Exception as e:
			logger = clsLog()
			logger.error(str(e))

 
def Main():
    socket = SocketServer()
    i = InputCatcher(socket)
    #start_new_thread(socket.Start,())


    #Chat
    #data  = '{"op":"set","device":"robot","details":{"name": "Chat", "data": {"op": "Chat", "n": "Hi","c":"1"}}}'
    #i.catch(data)
    #start_new_thread(i.catch,(data,))



    #leds ##
    #data  = '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":5}}}'

	# Movement ##
    data  = '{"op":"set","device":"robot","details":{"name": "Moving", "data": {"op": "m", "d": "F","s":8, "nextStep": "S"}}}' 
    robot = Robot()
    Robot.getRobot()
    robot.connect()
    time.sleep(5)
    i.catch(data)
    time.sleep(10)
    robot.disconnect()
	


    #Event( "Changing Leds Command will be sent [ Error ) ")
    # change Leds 
    #data  = '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "p", "n": 1,"s":5}}}'

  
    #time.sleep(5)
    
    #Event("Changing Leds Command will set to Dismiss")
    # change Leds 
    #ledData2  = '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":2}}}'
    #i.catch(ledData2)   
    #Event("wait   until Change led again to Idel ...7 ")
    #time.sleep(6)   
    #print "Changing Leds Command will be sent"    
      
    #movement #
    #data  = '{"op":"set","device":"robot","details":{"name": "Moving", "data": {"op": "m", "d": "S","s":1, "nextStep": "S"}}}' 
    #data  = '{"op":"set","device":"robot","details":{"name": "Moving", "data": {"op": "m", "d": "S"}}}' 
    ##
    #i.catch(data)



    #i.catch("0!@#1!@#1!@#0!@#<c,0,0,0>")
if __name__ == '__main__':
    Main()
