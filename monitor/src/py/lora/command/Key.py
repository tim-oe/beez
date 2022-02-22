#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from BaseCommand import BaseCommand

__all__ = ["Key"]


class Key(BaseCommand):
    """
    LoRaWAN related AES-128 keys command
    """

    COMMAND_KEY = "KEY"
    KEY_NETWORK_SESSION = "NWKSKEY"  # network session
    KEY_APP_SESSION = "APPSKEY"  # app session
    KEY_APP = "APPKEY"  # app ky

    def __init__(self, key, value):
        """
        Ctor set key feild
        :param self: this
        :param key: the key field name
        :param value: the value to set
        """
        super.__init__(
            self.COMMAND_KEY
            + BaseCommand.COMMAND_EQUALS
            + id
            + BaseCommand.COMMAND_COMMA
            + BaseCommand.COMMAND_QUOTE
            + value
            + BaseCommand.COMMAND_QUOTE
        )

    @staticmethod
    def networkSession(value):
        """
        :return: create network session key command
        """
        return Key(Key.KEY_NETWORK_SESSION, value)

    @staticmethod
    def appSession(value):
        """
        :return: create application session key command
        """
        return Key(Key.KEY_APP_SESSION, value)

    @staticmethod
    def app(value):
        """
        :return: create application key command
        """
        return Key(Key.KEY_APP, value)
