#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

from lora.command.BaseCommand import BaseCommand
from lora.command.Version import Version

__all__ = ["LoraVersion"]


class LoraVersion(BaseCommand):
    """
    LORA Version command
    """

    COMMAND_VERSION = (
        BaseCommand.LORA_PREFIX + BaseCommand.COMMAND_EQUALS + Version.COMMAND_VERSiON
    )

    def __init__(self):
        """
        Ctor
        :param self: this
        """
        super().__init__(self.COMMAND_VERSION)
