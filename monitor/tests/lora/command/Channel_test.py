#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from src.lora.command.Channel import Channel
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestChannel(BaseTestCommand):
    def testRead(self):
        self.validate(cmd=Channel(), pattern="\+" + Channel.COMMAND_CHANNEL + ": \d+;")

    def testEnable(self):
        channel: int = 1
        self.validate(
            cmd=Channel(channel=channel, enable=True),
            pattern="(?i)\+"
            + Channel.COMMAND_CHANNEL
            + ": "
            + Channel.COMMAND_CHANNEL
            + str(channel)
            + " "
            + Channel.CHANNEL_ENABLE,
        )


    def testDisable(self):
        channel: int = 1
        self.validate(
            cmd=Channel(channel=channel, enable=False),
            pattern="(?i)\+"
            + Channel.COMMAND_CHANNEL
            + ": "
            + Channel.COMMAND_CHANNEL
            + str(channel)
            + " "
            + Channel.CHANNEL_DISABLE,
        )
