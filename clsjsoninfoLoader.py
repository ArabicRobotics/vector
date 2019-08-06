import json
import os
import sys
from clsLog import clsLog  
from enums import enumConfigFile,enumExcecutionMood
from clsUtilities import *

def case(*args):
    return any((arg == switch.value for arg in args))

class Settings:
    ## global Class to load and get data to and from json files ....

    @staticmethod
    def loadFile(fileName):
        """ return the data which inside json file in the configuration directory as json 
        
        @rType: bool/json
        @return if everything is okay then return the data in the file as json , 
        False if something went wrong
        """        
        try: 
            dir_path = os.path.dirname(os.path.realpath(__file__))
            ##print "path = "+dir_path
            with open(dir_path+"/configurations/"+str(fileName),"r") as file:
                configurationfileData = file.read()
                ##print "config data =" +str(configurationfileData)
                file.close()
                ##print "file closed"
            return json.loads(configurationfileData)
            # values ###
        except Exception as e:
            print  ("exception on load file"+str(e))
            logger = clsLog()
            logger.error(str(e))
            return False
    #DatabaseConfig
    # Set variable in the config file.    
    # 
    # 
    #  
    @staticmethod
    def DumpFile(FileName="file.json",data=""):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            if not os.path.exists(FileName):
                open(dir_path+"/configurations/"+str(FileName),"w+")
                
            with open(dir_path+"/configurations/"+str(FileName),"w") as file:
                d = json.dumps(data)
                file.write(d)
                file.close()
            
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return False
        return True


class GlobalInfo(object):    
    Config={}
    Halt=False
    session =None
    connectionString=None
    Config = Settings.loadFile(enumConfigFile.value(enumConfigFile.configuration))
    ExcecutionMood= enumExcecutionMood.ByVal(int(Config["core"]["ExcecutionMood"]))
    """0=debug , 1 = test , 2 = Live"""
    Input = int(Config["Globals"]["Input"])
    """1 = Keyboard , 2 = Live,  3 Speech"""
    Output = int(Config["Globals"]["Output"])
    """output is the way of  output  , : 1= Console , 2 = robot speech , 3 - computer speech
    """
    @staticmethod
    def Set(section,variable,newDasta,FileName="myInfo.json"):
        """
        Set variable in the config file. (Case sensitive)

        :param section: root Section  like : Robot , Local, Database \n
        :param variable: Variable to set data \n
        :param newData: New Data to set\n
        :return: True = done , False There is Exception and logged. \n
        """
        sectionFound = False
        variableFound = False
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(dir_path+"/configurations/"+FileName,"r") as file:
                configFile = file.read()
                file.close()
            data = json.loads(configFile)
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return False

        for s in data:
            if s == section:
                sectionFound = True
                for v in data[section]:
                    if v == variable:
                        data[section][variable]=newData
                        variableFound = True

        
        if not sectionFound:
            data.update({""+section+"":{
                ""+variable+"":""+newData+""
            }})
        if not variableFound:
            data[section][variable]=newData
        try:
            with open(dir_path+"/configurations/"+FileName,"w") as file:
                d = json.dumps(data)
                file.write(d)
                file.close()
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return False
        return True


    @staticmethod
    def Set3(section,subSection,variable,newData,FileName="myInfo.json"):
        """
        Set variable in the config file. (Case sensitive)

        :param section: root Section  like : Robot , Local, Database \n
        :param variable: Variable to set data \n
        :param newData: New Data to set\n
        :return: True = done , False There is Exception and logged / . \n
        """
        sectionFound = False
        subSectionFound = False
        variableFound = False

        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(dir_path+"/configurations/"+FileName,"r") as file:
                configFile = file.read()
            data = json.loads(configFile)
            file.close()
            """ Check for exxist ---------- FW-----
        for s in data:
            if s == section:
                sectionFound = True
                for subs in data[section]:
                    if subs == subSection:
                        subSectionFound = True
                        for v in subs:
                            if v == variable:
                                data[section][subSection][variable]=newData
                                variableFound = True"""
            data[section][subSection][variable]=newData    
            with open(dir_path+"/configurations/"+FileName,"w") as file:
                d = json.dumps(data)
                file.write(d)        
        except Exception as e:
            logger = clsLog()
            logger.error(str(e))
            return False


    @staticmethod
    def Reload(Filename = enumConfigFile.configuration):
        """ Say text with sencent.

        @type  Filename: enumConfigFile
        @param Filename: file to reset values (Currently profile , Config file,Relatives)
        @rtype: Boolean
        @return: True if said complete , False and logged if not..
        """
        while switch(Filename):         
            if case(enumConfigFile.configuration):
                GlobalInfo.Config = Settings.loadFile(enumConfigFile.configuration)
                GlobalInfo.Input = int(GlobalInfo.Config["Globals"]["Input"])
                """1 = Keyboard , 2 = Live,  3 Speech"""
                GlobalInfo.Output = int(GlobalInfo.Config["Globals"]["Output"])
                """output is the way of  output  , : 1= Console , 2 = robot speech , 3 - computer speech
                """
                ##print GlobalInfo.Config
                break          
            return True
    

if __name__ == '__main__':
    info = GlobalInfo()
    info.Reload(enumConfigFile.configuration)
    print ("Test Load Configurations !!! ")
    print (info.Config["robotPaths"]["photos"])
    print ("[i]Done!")