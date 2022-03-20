#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["Id"]


class Id(BaseCommand):
    """
    lora id command
    """

    COMMAND_ID = "ID"
    ID_DEV_ADDR = "DevAddr"  # abp
    ID_DEV_EUI = "DevEui"  # otaa
    ID_APP_EUI = "AppEui"  # otaa

    def __init__(self, id=None, value=None):
        """
        Ctor read id
        :param self: this
        :param id: the id field name
        """
        if id is None:
            super().__init__(self.COMMAND_ID)
        elif value is None:
            super().__init__(self.COMMAND_ID + BaseCommand.COMMAND_EQUALS + id)
        else:
            super().__init__(
                self.COMMAND_ID
                + BaseCommand.COMMAND_EQUALS
                + id
                + BaseCommand.COMMAND_COMMA
                + BaseCommand.COMMAND_QUOTE
                + value
                + BaseCommand.COMMAND_QUOTE
            )

    @classmethod
    def devAddr(cls, value):
        """
        :return: create devAddr id command
        """
        return cls(cls.ID_DEV_ADDR, value)

    @classmethod
    def devEui(cls, value):
        """
        :return: create devEui id command
        """
        return cls(cls.ID_DEV_EUI, value)

    @classmethod
    def appEui(cls, value):
        """
        :return: create appEui id command
        """
        return cls(cls.ID_APP_EUI, value)
