# -*- coding: utf-8 -*-

__author__ = "Alexiy"

__date__ = "06.05.2018"

YES = 'yes'

predictions = [
    'WW91J2xsIGhhdmUgYSBnb29kIGRheQ==',
    'VGhlIGFuc3dlciBpcyA0Mg==',
    'SWdub3JlIHRoaXMgcHJlZGljYXRpb24=',
    'T3JhY2xlIGlzIG9uIHZhY2F0aW9u',
    'VHJ1dGggaXMgc29tZXdoZXJlLCBidXQgbm90IGhlcmU=',
    'MiArIDIgPSA0LCBidXQgaXQgaXMgbm90IGV4YWN0bHk=',
    'TGV0IGl0IGJlLi4u',
    'QW5kIHRoaXMgdG9vIHdpbGwgcGFzcw=='
]


if __name__ == '__main__':
    import os
    import random
    import base64

    print 'Hi! {}'.format(os.environ.get('USERNAME'))

    shouldContinue = True
    while shouldContinue:
        print base64.decodestring(random.choice(predictions))
        print
        inputString = raw_input('Make next predication (yes)? ')
        shouldContinue = YES in inputString.lower()
