#!/usr/bin/env python3
import os
import sys
import socket
import re
import copy
import pickle
import time
import queue
from datetime import datetime, timezone
import braine_comm_pb2
import logging
import binascii


"""Serial port data visualizer"""
class tcpSerialLink():
    """A simple example class"""
    BYTE_START = 0x5A
    BYTE_END = 0xA5
    BYTE_ESC = 0x7E
    BYTES_TO_ESCAPE = [BYTE_START, BYTE_END, BYTE_ESC]    
    
    def __init__(self, ip_address, port):
        self.__ip_address = ip_address
        self.__port = port

    def getTempFunc(self, channel):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdGetTemperature()
        submessage.tempChannel = channel
        command.cmdGetTemperature.CopyFrom(submessage)
        assert command.HasField("cmdGetTemperature")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response
        
    def getPowerFunc(self, channel):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdGetPower()
        submessage.pwrChannel = channel
        command.cmdGetPower.CopyFrom(submessage)
        assert command.HasField("cmdGetPower")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response
        
    def getStmIdFunc(self):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdGetStmId()
        command.getStmId.CopyFrom(submessage)
        assert command.HasField("getStmId")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response  
    
    def getSwVersionFunc(self):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdGetSwVersion()
        command.getSwVersion.CopyFrom(submessage)
        assert command.HasField("getSwVersion")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response  
    
    def getControlStateFunc(self):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdGetControlState()
        command.cmdGetControlState.CopyFrom(submessage)
        assert command.HasField("cmdGetControlState")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response
    
    def setControlStateFunc(self, controlState):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdControl()
        submessage.control = controlState
        command.cmdControl.CopyFrom(submessage)
        assert command.HasField("cmdControl")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response

    def setDebugCmdFunc(self, DebugCmd):
        command = braine_comm_pb2.Command()
        submessage = braine_comm_pb2.cmdDebug()
        submessage.debugCmd = DebugCmd
        command.debug.CopyFrom(submessage)
        assert command.HasField("debug")
        
        serializedCommand = command.SerializeToString()
        serialized_escaped_command = self.__add_escape(serializedCommand)
        response_data = self.__send_command(serialized_escaped_command)
        response = self.__remove_escape(response_data); 

        return response


    # Function to send a command and read the response
    def __send_command(self, serialized_escaped_command):
	
        # Creating client TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
	
            # Connecting to the specified address and port
            client_socket.connect((self.__ip_address, self.__port))
		
            # Sending the command
            client_socket.sendall(bytes(serialized_escaped_command))
		
            # Reading the response raw data
            response_data = client_socket.recv(4000)
            rx = bytes(response_data);
            print("\nRx : ", binascii.hexlify(rx))
		
        # Returning the parsed response
        return response_data

    # Function to send a command and read the response
    def __add_escape(self, serialized_command):         
        
        serialized_escaped_command = [self.BYTE_START]
        for i in bytes(serialized_command):
            if i in self.BYTES_TO_ESCAPE:
                serialized_escaped_command.append(self.BYTE_ESC)
            serialized_escaped_command.append(i)
        serialized_escaped_command.append(self.BYTE_END)
        #print("\nMessage to send: ", bytes(serialized_escaped_command))
   	
        # Returning the parsed response
        return serialized_escaped_command
    
    # Function to send a command and read the response
    def __remove_escape(self, received_data):  
        self.escape_next = False
        received_escape_removed_data = []
                   
        """Serial port listener"""
        for i in received_data:
            if self.escape_next:
                received_escape_removed_data.append(i)
                self.escape_next = False

            elif i is self.BYTE_START:
                received_escape_removed_data.clear()

            elif i is self.BYTE_ESC:
                self.escape_next = True
                
            elif i is self.BYTE_END:
                self.escape_next = False
                                
            else:
                received_escape_removed_data.append(i)
        
        response = braine_comm_pb2.Response()
        response.ParseFromString(bytes(received_escape_removed_data))
#       rx = bytes(received_escape_removed_data);
#       print("\nResponse : ", binascii.hexlify(rx))
        
        if 'status' == response.WhichOneof('resp_oneof'):
            print("Status response msg:")
        elif 'respStmId' == response.WhichOneof('resp_oneof'):
            print("STM ID response msg:")
        elif 'respSwVersion' == response.WhichOneof('resp_oneof'):
            print("Sw version response msg:")
        elif 'respControlState' == response.WhichOneof('resp_oneof'):
            print("Control state response msg:")
        elif 'cmdGetTemperature' == response.WhichOneof('resp_oneof'):
            print("Get Temperature command response:")
        elif 'cmdGetPower' == response.WhichOneof('resp_oneof'):
            print("Get Power command response:")
            
        print(response)
                     	
        # Returning the parsed response
        return response    
