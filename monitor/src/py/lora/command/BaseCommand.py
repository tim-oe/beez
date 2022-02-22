#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

__all__ = ["BaseCommand"]


class BaseCommand(object):
    """
    base AT command class for Lora-E5
    See https://files.seeedstudio.com/products/317990687/res/LoRa-E5%20AT%20Command%20Specification_V1.0%20.pdf
    """

    COMMAND_PREFIX = "AT+"
    LORA_PREFIX = "LW="
    COMMAND_EQUALS = "="
    COMMAND_QUOTE = '"'
    COMMAND_COMMA = ","

    def __init__(self, cmd):
        """
        Ctor
        :param self: this
        :param cmd: the complete at command (not including AT prefix)
        """
        self.cmd = self.COMMAND_PREFIX + cmd

    @property
    def command(self):
        """
        command property getter
        :param self: this
        :return: the full comand string
        """
        return self.cmd
