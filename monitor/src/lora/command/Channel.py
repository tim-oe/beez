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

    def __init__(self, channel=-1, enable=True):
        """
        Ctor set channel
        :param self: this
        :param channel: the channel to set
        :param enable: whether to enable, true, or disable false
        """

        _cmd: str
        if channel >= 0:
            _cmd = (
                self.COMMAND_CHANNEL
                + BaseCommand.COMMAND_EQUALS
                + str(channel)
                + BaseCommand.COMMAND_COMMA
                + (self.CHANNEL_DISABLE, self.CHANNEL_ENABLE)[enable]
            )
        else:
            _cmd = self.COMMAND_CHANNEL

        super().__init__(_cmd)
