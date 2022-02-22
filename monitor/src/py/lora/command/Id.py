#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from BaseCommand import BaseCommand

__all__ = ["Id"]


class Id(BaseCommand):
    """
    lora id command
    """

    COMMAND_ID = "ID"
    ID_DEV_ADDR = "DevAddr"  # abp
    ID_DEV_EUI = "DevEui"  # otaa
    ID_APP_EUI = "AppEui"  # otaa

    def __init__(self):
        """
        Ctor read all id fields
        :param self: this
        """
        super.__init__(self.COMMAND_ID)

    def __init__(self, id):
        """
        Ctor read id
        :param self: this
        :param id: the id field name
        """
        super.__init__(self.COMMAND_ID + BaseCommand.COMMAND_EQUALS + id)

    def __init__(self, id, value):
        """
        Ctor set id field
        :param self: this
        :param id: the id field name
        :param value: the value to set
        """
        super.__init__(
            self.COMMAND_ID
            + BaseCommand.COMMAND_EQUALS
            + id
            + BaseCommand.COMMAND_COMMA
            + BaseCommand.COMMAND_QUOTE
            + value
            + BaseCommand.COMMAND_QUOTE
        )

    @staticmethod
    def devAddr(value):
        """
        :return: create devAddr id command
        """
        return Id(Id.ID_DEV_ADDR, value)

    @staticmethod
    def devEui(value):
        """
        :return: create devEui id command
        """
        return Id(Id.ID_DEV_EUI, value)

    @staticmethod
    def appEui(value):
        """
        :return: create appEui id command
        """
        return Id(Id.ID_APP_EUI, value)
