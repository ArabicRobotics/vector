#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Hello World

Make Vector say 'Hello World' in this simple Vector SDK example program.
"""
#from clsLog import clsLog
import anki_vector
from clsRobot import Robot
from clsLog import clsLog
class Say (object):
    """This class for """ 
    def __init__(self):
        """This initilization for 
        """ 
        try:
            
            return
        except Exception as e:
            #logger = clsLog()
            print (e)
            #logger.error(str(e))
            return
    def say(self,string ="Hello"):
        """ This Method for
        @type  paramName: Bool
        @param paramName : Description
        @rtype:  Boolean
        @return: True : everything went fine
        False : Something went wrong
        """ 
        try: 
            Robot.getRobot()
            Robot.vector.behavior.say_text(string)
            return True
        except Exception as e:
            print (e)
            logger = clsLog()
            logger.error(str(e))
            return False


def main():
    say = Say()
    Robot.connect()
    say.say("Hello World ! ")
    Robot.disconnect()
if __name__ == "__main__":
    main()