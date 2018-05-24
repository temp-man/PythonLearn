# -*- coding: utf-8 -*-

__author__ = "Alexiy"

__date__ = "10.05.2018"

GRAVITY_CONSTANT = 6.67408e-11

PLANET_RADIUS = 6371000.0
PLANET_MASS = 5.972e24


GRAVITY_ACCELERATION = GRAVITY_CONSTANT * PLANET_MASS / PLANET_RADIUS / PLANET_RADIUS


def calculateGravityForce(mass):
    """
    Calculates gravity force for material point on the planet surface
    :param mass: object mass
    :type mass: float
    :return: gravity force
    """
    return GRAVITY_ACCELERATION * mass


if __name__ == '__main__':
    mass = input('Enter object mass: ')
    gravityForce = calculateGravityForce(mass)
    print 'Gravity force for this object is: {}'.format(gravityForce)
