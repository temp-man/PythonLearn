# -*- coding: utf-8 -*-

__author__ = "Alexiy"

__date__ = "10.05.2018"

from math import pi

SPHERE_VOLUME_FACTOR = 4.0 / 3.0
LIGHT_SPEED_IN_VACUUM = 299792458.0
PLANCK_ENERGY_DENSITY = 4.59e113

SQR_LIGHT_SPEED_IN_VACUUM = LIGHT_SPEED_IN_VACUUM * LIGHT_SPEED_IN_VACUUM


def calculateEnergy(mass):
    """
    Calculates object energy by mass
    :param mass: object mass
    :type mass: float
    :return: energy
    :rtype: float
    """
    return mass * SQR_LIGHT_SPEED_IN_VACUUM


def calculateSphereVolume(radius):
    """
    Calculate sphere volume by radius
    :param radius: sphere radius
    :type radius: sphere radius
    :return: sphere volume
    :rtype: float
    """
    return SPHERE_VOLUME_FACTOR * pi * radius * radius * radius


if __name__ == '__main__':
    mass = input('Enter object mass: ')
    radius = input('Enter object radius: ')
    objectEnergy = calculateEnergy(mass)
    objectVolume = calculateSphereVolume(radius)

    if objectEnergy / objectVolume <= PLANCK_ENERGY_DENSITY:
        print 'This object can be real'
    else:
        print 'This object can not be real'
