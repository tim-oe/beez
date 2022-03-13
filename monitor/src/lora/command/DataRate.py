#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["DataRate"]


class DataRate(BaseCommand):
    """
    Data Rate command class, used to set band frequency plan
    see https://www.thethingsnetwork.org/docs/lorawan/frequency-plans/
    """

    COMMAND_DATA_RATE = "DR"
    DATA_RATE_US = "US915"
    DATA_RATE_SCHEME = "SCHEME"

    def __init__(self):
        """
        Ctor read band
        :param self: this
        """
        super().__init__(
            self.COMMAND_DATA_RATE + BaseCommand.COMMAND_EQUALS + self.DATA_RATE_SCHEME
        )

    def __init__(self, band):
        """
        Ctor set band
        :param self: this
        :param band: the band plan name
        """
        super().__init__(self.COMMAND_DATA_RATE + BaseCommand.COMMAND_EQUALS + band)
