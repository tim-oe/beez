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

    def __init__(self, band: str = None):
        """
        Ctor set band
        :param self: this
        :param band: the band plan name
        """
        _cmd: str
        if band is None:
            _cmd = (
                self.COMMAND_DATA_RATE
                + BaseCommand.COMMAND_EQUALS
                + self.DATA_RATE_SCHEME
            )
        else:
            _cmd = self.COMMAND_DATA_RATE + BaseCommand.COMMAND_EQUALS + band

        super().__init__(_cmd)

    @classmethod
    def read(cls):
        """
        :return: create read data rate command
        """
        return cls()

    @classmethod
    def us(cls):
        """
        :return: create us data rate command
        """
        return cls(DataRate.DATA_RATE_US)
