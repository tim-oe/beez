#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand

__all__ = ["LoraVersion"]


class LoraVersion(BaseCommand):
    """
    LORA Version command
    """

    COMMAND_VERSION = BaseCommand.LORA_PREFIX + "VER"

    def __init__(self):
        """
        Ctor
        :param self: this
        """
        super().__init__(self.COMMAND_VERSION)
