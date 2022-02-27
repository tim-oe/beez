#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

__all__ = ["Modem"]

import serial
import io
import time

from py.lora.command.BaseCommand import BaseCommand

class Modem(object):
    """
    Seeedstudio lora-e5 grove modem
    see https://wiki.seeedstudio.com/Grove_LoRa_E5_New_Version/
    see https://pyserial.readthedocs.io/en/latest/pyserial.html
    see https://docs.python.org/3/library/io.html 
    """

    def __init__(self, 
                 port='/dev/serial0',
                 baud=9600,
                 writeTimeout=60,
                 readDelay=0.3):
        """
        ctor
        :param self: this
        :param port: the device serial port name
        :param baud: the baud rate
        :param writeTimeout: the write timeout in seconds
        :param readDelay: the delay to wait afte command
        """
        self.serialPort = serial.Serial(port, baud, writeTimeout)
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serialPort, self.serialPort))
        self.readDelay = readDelay
        
    def send(self, command: BaseCommand) -> str:
        """
        send a command
        :param command: the AT command
        :return: the response if any
        """
        self.sio.write(command.cmd)
        self.sio.flush()
        self.serialPort.flush()
        time.sleep(self.readDelay) 
        
        out: str = ''
    
        while self.serialPort.inWaiting() > 0:
            out += self.serialPort.read(1).decode()
       
        return out
    