#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["Mode"]


class Mode(BaseCommand):
    """
    LORA work mode command
    """

    COMMAND_MODE = "MODE"
    MODE_TEST = "TEST"
    MODE_OTAA = "LWOTAA"
    MODE_ABP = "LWABP"

    def __init__(self, mode):
        """
        Ctor
        :param self: this
        :param mode: the work mode
        """
        super().__init__(self.COMMAND_MODE + BaseCommand.COMMAND_EQUALS + mode)

    @staticmethod
    def otaa():
        """
        :return: create otaa mode command
        """
        return Mode(Mode.MODE_OTAA)

    @staticmethod
    def abp():
        """
        :return: create abp mode command
        """
        return Mode(Mode.MODE_ABP)

    @staticmethod
    def test():
        """
        :return: create test mode command
        """
        return Mode(Mode.MODE_TEST)
