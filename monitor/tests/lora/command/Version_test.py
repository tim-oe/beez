#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

import unittest
from lora.command.Version import Version

from tests.lora.command.BaseTestCommand import BaseTestCommand

class TestVersion(BaseTestCommand):    
    def test(self):
        self.validate(cmd=Version(), pattern='\+VER: 4\.0\.11')
