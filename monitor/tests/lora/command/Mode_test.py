#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from src.lora.command.Mode import Mode
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestMode(BaseTestCommand):
    def testRead(self):
        self.validate(
            cmd=Mode(),
            pattern="\+"
            + Mode.COMMAND_MODE
            + ": ("
            + Mode.MODE_OTAA
            + "|"
            + Mode.MODE_ABP
            + "|"
            + Mode.MODE_TEST
            + ")",
        )

    def testOtaa(self):
        self.validate(
            cmd=Mode.otaa(), pattern="\+" + Mode.COMMAND_MODE + ": " + Mode.MODE_OTAA
        )

    def testAbp(self):
        self.validate(
            cmd=Mode.abp(), pattern="\+" + Mode.COMMAND_MODE + ": " + Mode.MODE_ABP
        )

    def testTest(self):
        self.validate(
            cmd=Mode.test(), pattern="\+" + Mode.COMMAND_MODE + ": " + Mode.MODE_TEST
        )
