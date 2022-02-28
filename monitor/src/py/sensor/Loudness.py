#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

__all__ = ["Loudness"]

from grove.grove_loudness_sensor import GroveLoudnessSensor

class Loudness(object):
    """
    loudness sensor class
    see https://wiki.seeedstudio.com/Grove-Loudness_Sensor/ 
    """
    
    def __init__(self, channel=0):
        """
        ctor
        :param self: this
        :param channel: the analog channel
        """
        self.sensor = GroveLoudnessSensor(channel)
        
    def read(self):
        """
        read sensor
        :param self: this
        :return: loudness 1 - 1000
        """
        return self.sensor.value