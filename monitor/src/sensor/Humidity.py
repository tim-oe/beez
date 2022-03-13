#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
"""
"""
from Temprature import Temprature

__all__ = ["Humitity"]


class Humitity(Temprature):
    """
    humidity sensor class
    see https://shop.switchdoc.com/collections/grove/products/sht30-i2c-waterproof-temperature-and-humidity-sensor-with-grove
    """

    def __init__(self, gpioPin=6):
        """
        ctor
        :param self: this
        :param gpioPin: the gpio pin (ic2)
        """
        super(gpioPin)

    def read(self):
        """
        read sensor
        :param self: this
        :return: humidity
        """
        return self.sensor.read_humidity()
