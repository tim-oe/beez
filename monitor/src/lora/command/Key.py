#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

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
        super().__init__(
            self.COMMAND_KEY
            + BaseCommand.COMMAND_EQUALS
            + key
            + BaseCommand.COMMAND_COMMA
            + BaseCommand.COMMAND_QUOTE
            + value
            + BaseCommand.COMMAND_QUOTE
        )

    @classmethod
    def networkSession(cls, value):
        """
        :return: create network session key command
        """
        return cls(cls.KEY_NETWORK_SESSION, value)

    @classmethod
    def appSession(cls, value):
        """
        :return: create application session key command
        """
        return cls(cls.KEY_APP_SESSION, value)

    @classmethod
    def app(cls, value):
        """
        :return: create application key command
        """
        return cls(cls.KEY_APP, value)
