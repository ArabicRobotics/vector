# import socket programming library
import socket
# import thread module
from _thread import *
import threading
import time
from clsLog import clsLog
from clsjsoninfoLoader import GlobalInfo
from clsServerRobot import ServerRobot
from enums import enumEventType
from clsServerUtilities import ServerUtilities

print_lock = threading.Lock()

# thread fuction
class SocketServer (object):
    """This class for """ 
    def __init__(self):
        """This initilization for
        """
        try:   
            self.Halt = False   
            self.receivedData = None
            self.ServerRobot = ServerRobot()
            self.c = None
            self.s = None
            self.running = False
            return
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return            
    def __datasetter(self,c):
        """ This Method for      r
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try:
            self.receivedData = c
            print (self.receivedData)
            return True
        except Exception as e:
            print (str(e))
            logger = clsLog()
            logger.error(str(e))
            return False          
    def threaded(self,c):
        try:
            self.c = c
            while True:
                if self.Halt:
                    self.__exit__()
                    return True
                try:
                    try:
                        data = self.c.recv(1024)
                    except socket.error: 
                        print (ex)
                        print_lock.release()
                        print ("connection Lost, Bye")
                        return True
                    except Exception as ex: 
                        print (ex)
                        print_lock.release()
                        print ("connection Lost, Bye")
                        return True
                    if not data:
                        print('Bye')                
                        # lock released on exit
                        print_lock.release()
                        return True   
                    # reverse the given string from client
                    #data = data[::-1]
                    start_new_thread(self.__datasetter, (data,))
                    # send back reversed string to client
                    #self.c.send(data)                
                except Exception as e:
                    print ("error reading from socket."+str(e))
                    return
            
			# connection closed
            self.c.close()
        except KeyboardInterrupt:
            print ("[N]I will Exit the program")
            self.shutDown()     
            GlobalInfo.Halt = True               
    def Start(self):
        """ This Method for  
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try: 
            host = ""        
            # reverse a port on your computer
            # in our case it is 12345 but it
            # can be anything
            port = self.ServerRobot.Port
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         
            self.s.bind((host, port))
              
            # put the socket into listening mode
            self.s.listen(5)
             
            # a forever loop until client wants to exit
            self.running = True
            while True: 
                if self.Halt:                    
                    self.__exit__()
                    return True                
                # establish connection with client
                self.c, addr = self.s.accept()   
                  
                # lock acquired by client
                print_lock.acquire()
                print('Connected to :', addr[0], ':', addr[1])        
                #self.sendToClient("Server_connected",[str(addr[0]),str(addr[1])],enumEventType.Success)
                # Start a new thread and return its identifier
                start_new_thread(self.threaded, (self.c,))
            self.s.close()                    
            print ("Done")
            return True
        except KeyboardInterrupt:
            print ("[N]I will Exit the program")
            self.shutDown()     
            GlobalInfo.Halt = True            
        except Exception as e:
            print ("error while Start the Server Socket , I will exit")
            print (e)
            GlobalInfo.Halt = True
            logger = clsLog()
            logger.error(str(e))
            return False            

    def sendToClient(self,name,value,type=enumEventType.Information):
        """ This Method for   send result of excecution  to client 
        @type  paramName: socket 
        @param paramName :socket handeller
        @type  paramName: name 
        @param paramName : Name of the data
        @type  paramName: string  
        @param paramName : value
        @type  paramName: enumEventType  
        @param paramName : Type of event ( Success, Error, Warning ,...)
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """
        if self.c != None:	
            message =  ServerUtilities.setResult(name,value,type)
            print (message)
            return self.send(message)
    def shutDown(self):
            """ This Method for      
            @type  paramName: Bool
            @param paramName : Description
            @rtype:  Boolean
            @return: True : everything went fine
            False : Something went wrong
            """ 
            try: 
                print ("socket is closing ...")
                self.Halt=True
                time.sleep(0.9)
                if self.running:
                    self.running = False                     
                    return self.__exit__()             
            except Exception as e:
                print ("error on Exit Socket")
                print (e)
                logger = clsLog()
                logger.error(str(e))
                return False
#------------------------------------------------
    def __exit__(self):
            """ This Method for      
            @type  paramName: Bool
            @param paramName : Description
            @rtype:  Boolean
            @return: True : everything went fine
            False : Something went wrong
            """ 
            try: 
                print ("socket is closing ...")
                self.Halt=True
                time.sleep(0.1)
                self.s.close()
                self.s.shutdown(socket.SHUT_WR)
                #self.s.shutdown(socket.SHUT_RDWR)
                #self.s.close()                
                print ("Socket Closed.")
                return True
            except Exception as e:
                print ("error on Exit Socket")
                #self.s.close()
                print (e)
                logger = clsLog()
                logger.error(str(e))
                return e

    def send(self,data ="hi"): 
            """ This Method for   Send data to the client 
            @type  paramName: strign
            @param paramName : data
            @rtype:  Any
            @return: True : everything went fine
            False : Something went wrong
            """ 
            try: 
                self.c.send(data)                
                return True
            except Exception as e:
                print ("Error in Send To Client , Send "+str(e))
                logger = clsLog()
                logger.error(str(e))
                return False
def Main():
    server = SocketServer()
    t = threading.Thread(target=server.Start,name="")
    t.start()
    print (server.sendToClient("Hello","Yes I am Value",enumEventType.Information))
    print ("waiting for 30 seconds ")
    time.sleep(30)
    server.Halt = True
    t.join()
    exit(0)
    print ("Threads Joins .. Done")
    time.sleep(3)
if __name__ == '__main__':
    Main()