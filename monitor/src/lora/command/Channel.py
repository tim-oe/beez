#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["Channel"]


class Channel(BaseCommand):
    """
    frequency channel command
    """

    COMMAND_CHANNEL = "CH"
    CHANNEL_ENABLE = "ON"
    CHANNEL_DISABLE = "OFF"

    def __init__(self):
        """
        Ctor read channels
        :param self: this
        """
        super().__init__(self.COMMAND_CHANNEL)

    def __init__(self, channel, enable=True):
        """
        Ctor set channel
        :param self: this
        :param channel: the channel to set
        :param enable: whether to enable, true, or disable false
        """
        super().__init__(
            self.COMMAND_CHANNEL
            + BaseCommand.COMMAND_EQUALS
            + channel
            + BaseCommand.COMMAND_COMMA
            + (self.CHANNEL_ENABLE, self.CHANNEL_DISABLE)[enable]
        )
