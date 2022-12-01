#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

__all__ = ["Modem"]

from curses import baudrate
import serial
import io
import time

from lora.command.BaseCommand import BaseCommand


class Modem(object):
    """
    Seeedstudio lora-e5 grove modem
    see https://wiki.seeedstudio.com/Grove_LoRa_E5_New_Version/
    see https://pyserial.readthedocs.io/en/latest/pyserial.html
    see https://docs.python.org/3/library/io.html
    """

    # LF needed to terminate command
    COMMAND_TERM = "\n"

    def __init__(self, port="/dev/serial0", baud=9600, write_timeout=60, read_delay=0.3):
        """
        ctor
        :param self: this
        :param port: the device serial port name
        :param baud: the baud rate
        :param writeTimeout: the write timeout in seconds
        :param readDelay: the delay to wait afte command
        """
        self.serial_port = serial.Serial(
            port=port, baudrate=baud, timeout=5, write_timeout=write_timeout
        )
        self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serial_port, self.serial_port))
        self.read_delay = read_delay

    def close(self):
        """
        close resources
        """
        self.serial_port.close()

    def send(self, command: BaseCommand) -> str:
        """
        send a command
        :param command: the AT command
        :return: the response if any
        """

        self.sio.write(command.cmd + self.COMMAND_TERM)
        self.sio.flush()
        self.serial_port.flush()
        time.sleep(self.read_delay)

        out: str = ""

        while self.serial_port.inWaiting() > 0:
            out += self.serial_port.read(1).decode()

        return out
