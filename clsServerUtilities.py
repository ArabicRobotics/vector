from clsLog import clsLog
from clsUtilities import jsonFormatter 
import json
from enums import enumEventType

class ServerUtilities (object):
    """This class for """ 
    def __init__(self):
        """This initilization for 
        """ 
        try: 
            self.formatter = jsonFormatter('',);
            return
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return
        return True

    @staticmethod
    def setOneMessage(name="",content=""):
        """ This Method for  
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try:      
            #requestId = 
            formatter = jsonFormatter('',)           
            formatter.Insert(name,content)
            '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":5}}}'
            result =   json.dumps (formatter.Json)
            return result
        except Exception as e:
            print (str(e))
            logger = clsLog()
            logger.error(str(e))
            return False    

    @staticmethod
    def setResult(name,value,type=enumEventType.Information):
            """ This Method for  
    
    
            @type  paramName: Bool
            @param paramName : Description
            @rtype:  Boolean
            @return: True : everything went fine
            False : Something went wrong
            """ 
            try: 
                #requestId = 
                formatter = jsonFormatter('',)           
                formatter.Insert(name,value)
                formatter.Insert("type",type.name)
                #formatter.Insert("type","info")
                '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":5}}}'
                result =   json.dumps (formatter.Json)
                return result
            except Exception as e:
                logger = clsLog()
                logger.error(str(e))
                return False
    @staticmethod
    def setMessage(message="",source="ServerRobot",distenation="log",content=""):
        """ This Method for  
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try: 
            string =""        
            #requestId = 
            formatter = jsonFormatter('',)           
            #string = "'{'message:'"+message+",'source:'"+source+"'}'"
            formatter.Insert("message",message)
            formatter.Insert("source",source)
            formatter.Insert("distenation",distenation)
            formatter.Insert("content",content)
            '{"op":"set","device":"robot","details":{"name": "Leds", "data": {"op": "c", "n": 1,"s":5}}}'
            result =   json.dumps (formatter.Json)
            return result
        except Exception as e:
            print (str(e))
            logger = clsLog()
            logger.error(str(e))
            return False
if __name__ == "__main__":
    server =  ServerUtilities()
    #print server.setMessage("This is test ","the test file ")
    print (server.setResult("Result name ","result value ",enumEventType.Error))

   
    
