from clsLog import clsLog
from clsjsoninfoLoader import GlobalInfo
class ServerRobot (object):
    def __init__(self):
        self.config = GlobalInfo.Config
        self.loadSettings()
    def loadSettings(self):
        try:
            ServerConfig = GlobalInfo.Config["ServerRobot"]
            self.IP =str(ServerConfig["ip"])
            self.Port = eval(str(ServerConfig["port"]))    
            return True
        except Exception as e:
            print (e)
            logger = clsLog()
            logger.error(str(e))
            return False


def main():
    server = ServerRobot()
    print (server.IP)

if __name__ == '__main__':
    main()