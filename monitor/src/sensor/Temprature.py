#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""

__all__ = ["Temprature"]


from py.lib import SHT30


class Temprature(object):
    """
    temprature sensor class
    see https://shop.switchdoc.com/collections/grove/products/sht30-i2c-waterproof-temperature-and-humidity-sensor-with-grove
    """

    def __init__(self, gpioPin=6):
        """
        ctor
        :param self: this
        :param gpioPin: the gpio pin (ic2)
        """
        self.sensor = SHT30.SHT30(gpioPin)

    def read(self):
        """
        read sensor
        :param self: this
        :return: temprature
        """
        return self.sensor.read_temperature()
