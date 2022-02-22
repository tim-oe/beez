#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from BaseCommand import BaseCommand

__all__ = ["Version"]


class Version(BaseCommand):
    """
    Firmware version command
    """

    COMMAND_VERSiON = "VER"

    def __init__(self):
        """
        Ctor
        :param self: this
        """
        super.__init__(self.COMMAND_VERSiON)
