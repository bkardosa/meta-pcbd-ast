import os
import sys
import copy
import pickle
import time
import queue
from datetime import datetime, timezone
from SerialLink import tcpSerialLink
import logging

class BraineCommTest():
    def __init__(self, ip_address, port, level):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=level) # log level
        self.SL = tcpSerialLink(ip_address, port)
        
    def getStmIdFunc(self):
        self.SL.getStmIdFunc()
    
    def getSwVersionFunc(self):
        self.SL.getSwVersionFunc()
        
    def getControlStateFunc(self):
        self.SL.getControlStateFunc()
    
    def setControlStateFunc(self, controlState):
        self.SL.setControlStateFunc(controlState)
        
    def getTempFunc(self, channel):        
    	self.SL.getTempFunc(channel)
    	
    def getPowerFunc(self, channel):
    	self.SL.getPowerFunc(channel)
    	
    def setDebugCmdFunc(self, DebugCmd):
    	self.SL.setDebugCmdFunc(DebugCmd)
    	

    	
