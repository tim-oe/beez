#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from src.lora.command.Version import Version
from tests.lora.command.BaseTestCommand import BaseTestCommand


class TestVersion(BaseTestCommand):
    def test(self):
        self.validate(
            cmd=Version(), pattern="\+" + Version.COMMAND_VERSiON + ": 4\.0\.11"
        )
