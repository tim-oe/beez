#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

import unittest

from lora.command.BaseCommand import BaseCommand
from lora.Modem import Modem


class BaseTestCommand(unittest.TestCase):
    # can't use __init__
    # https://techoverflow.net/2020/04/21/how-to-fix-python-unittest-__init__-takes-1-positional-argument-but-2-were-given/
    def setUp(self):
        self.modem = Modem()

    def tearDown(self):
        self.modem.close()

    def validate(self, cmd: BaseCommand, pattern: str):

        print( "\n>>> " + cmd.cmd)

        resp: str = self.modem.send(cmd)

        print( "<<< " + resp.strip())

        self.assertRegex(resp.strip(), pattern)
