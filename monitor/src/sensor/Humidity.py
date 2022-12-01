#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""


__all__ = ["Humidity"]


from sensor.Temprature import Temprature


class Humidity(Temprature):
    """
    humidity sensor class
    see https://shop.switchdoc.com/collections/grove/products/sht30-i2c-waterproof-temperature-and-humidity-sensor-with-grove
    """

    def __init__(self, gpio_pin=6):
        """
        ctor
        :param self: this
        :param gpioPin: the gpio pin (ic2)
        """
        super().__init__(gpio_pin)

    def read(self):
        """
        read sensor
        :param self: this
        :return: humidity
        """
        return self.sensor.read_humidity()
