#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["Temperature"]


class Temperature(BaseCommand):
    """
    modem temp command
    """

    COMMAND_TEMP = "TEMP"

    def __init__(self):
        """
        Ctor
        :param self: this
        """
        super().__init__(self.COMMAND_TEMP)
