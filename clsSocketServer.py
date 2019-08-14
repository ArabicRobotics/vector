# import socket programming library
# import thread module
import threading
import time
from clsLog import clsLog
from clsjsoninfoLoader import GlobalInfo
from clsServerRobot import ServerRobot
from enums import enumEventType
from clsServerUtilities import ServerUtilities
import sys
import socket
import selectors
import types
print_lock = threading.Lock()

class SocketServer (object):
	"""This class for Socket Server handeller """
	def __init__(self):
		"""This initilization for"""
		try:
			self.Halt = False
			self.receivedData = None
			self.ServerRobot = ServerRobot()
			self.sel = selectors.DefaultSelector()
			self.sockets = []
			self.running = False
			return
		except Exception as e:
			pring ("Error in init Server ...")
			print (e)
			logger = clsLog()
			logger.error(str(e))
			return


	def accept_wrapper(self,sock):
		try:
			conn, addr = sock.accept()  # Should be ready to read
			print("accepted connection from", addr)
			conn.setblocking(False)
			data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
			events = selectors.EVENT_READ | selectors.EVENT_WRITE
			self.sel.register(conn, events, data=data)
		except Exception as e:
			print ("Error in Server Accept wrapper  ...")
			print (e)
			logger = clsLog()
			logger.error(str(e))
			return
	def getSocketByIP(self,IP):
		for socket in self.sockets:
			if socket[0][0]==IP:
				return socket

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
	def service_connection(self,key, mask):
		try:
			sock = key.fileobj
			arrItem = [socket,key.data.addr]
			self.sockets.append(arrItem)
			data = key.data
			if mask & selectors.EVENT_READ:
				recv_data = sock.recv(1024)  # Should be ready to read
				if recv_data:
					data.outb += recv_data
					threadSetter = threading.Thread(target = self.__datasetter, args=(recv_data,))
					threadSetter.start()
				else:
					print("closing connection to", data.addr)
					self.sockets.remove(arrItem)
					self.sel.unregister(sock)
					sock.close()
			if mask & selectors.EVENT_WRITE:
				if data.outb:
					print("echoing", repr(data.outb), "to", data.addr)
					sent = sock.send(data.outb)  # Should be ready to write
					data.outb = data.outb[sent:]
		except Exception as e:
			print ("Error in Server service_connection  ...")
			print (e)
			logger = clsLog()
			logger.error(str(e))
			return False

	def sendToClient(self,name,value="clsSocketServer",type=enumEventType.Information,socket=None):
		try:
			message = ServerUtilities.setResult(name,value,type)
			self.send(message,socket)
		except Exception as e:
			print ("Error in Server send To Client  ...")
			print (e)
			logger = clsLog()
			logger.error(str(e))
			return False


	def send(self,message,socket=None):
		try:
			if socket ==None:
				if len(self.sockets) >0:
					self.sockets[len(self.sockets)-1][0].send(message)
				else:
					print ("No Socket To send to")
			socket.send(message)
		except Exception as e:
			print ("Error in Server Send ...")
			print (e)
			logger = clsLog()
			logger.error(str(e))
			return False
	def start(self):
		try:
			host, port = "", self.ServerRobot.Port
			self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.lsock.bind((host, port))
			self.lsock.listen()
			print("listening on", (host, port))
			self.lsock.setblocking(False)
			self.sel.register(self.lsock, selectors.EVENT_READ, data=None)
			self.running = True
			try:
				while True:
					events = self.sel.select(timeout=None)
					for key, mask in events:
						if key.data is None:
							self.accept_wrapper(key.fileobj)
						else:
							self.service_connection(key, mask)
			except KeyboardInterrupt:
				print("caught keyboard interrupt, exiting")
			finally:
				self.shutDown()
		except Exception as e:
			print(str(e))
			logger = clsLog()
			logger.error(str(e))
			return False


	def shutDown(self):
		try:
			
			self.running = False
			self.sel.unregister(self.lsock)
			self.sel.close()		
			self.sockets= []
			print ("Socket Shutdown Successfully..")
		except Exception as e:
			print(str(e))
			logger = clsLog()
			logger.error(str(e))
			return False
if __name__ == "__main__":
	server = SocketServer()
	server.start()





