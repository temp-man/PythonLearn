# -*- coding: utf-8 -*-

__author__ = "Alexiy"

__date__ = "21.05.2018"

ENCRYPTED_DATA = -1719806279
MAX_PIN = 99999999


def encrypt(pin):
    return hash('{}'.format(pin))


if __name__ == '__main__':
    print 'It can tacks some time'
    messageNotFounded = True
    pin = -1

    while messageNotFounded and pin <= MAX_PIN:
        pin += 1
        messageNotFounded = encrypt(pin) != ENCRYPTED_DATA

    if pin > MAX_PIN:
        print 'Invalid encrypted data: {}'.format(ENCRYPTED_DATA)
    else:
        print 'Pin Code is: {}'.format(pin)
