#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["Message"]


class Message(BaseCommand):
    """
    message command class
    """

    COMMAND_MESSAGE = "MSG"

    def __init__(self, msg):
        """
        Ctor
        :param self: this
        :param msg: the message
        """
        super().__init__(
            self.COMMAND_MESSAGE
            + BaseCommand.COMMAND_EQUALS
            + BaseCommand.COMMAND_QUOTE
            + msg
            + BaseCommand.COMMAND_QUOTE
        )
