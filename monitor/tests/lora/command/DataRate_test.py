#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from src.lora.command.DataRate import DataRate
from src.lora.command.Mode import Mode
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestChannel(BaseTestCommand):
    def testRead(self):
        # needs to not be in test mode
        self.modem.send(Mode.otaa())
        self.validate(
            cmd=DataRate.read(), pattern="\+" + DataRate.COMMAND_DATA_RATE + ": .*"
        )

    def testUs(self):
        # needs to not be in test mode
        self.modem.send(Mode.abp())
        self.validate(
            cmd=DataRate.us(),
            pattern="\+" + DataRate.COMMAND_DATA_RATE + ": " + DataRate.DATA_RATE_US,
        )
