#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from BaseCommand import BaseCommand

__all__ = ["Join"]


class Join(BaseCommand):
    """
    join lora network command
    """

    COMMAND_JOIN = "JOIN"
    JOIN_FORCE = "FORCE"

    def __init__(self, force=False):
        """
        Ctor
        :param self: this
        :param force: whether to force, true, or not false
        """
        super.__init__(
            self.COMMAND_JOIN
            + (BaseCommand.COMMAND_EQUALS + self.JOIN_FORCE, "")[force]
        )
