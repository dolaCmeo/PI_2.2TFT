# coding=utf-8
import wiringpi

__author__ = 'dolacmeo'
__project__ = 'raspberryPi3B+ 2.2TFT Keys'
__doc__ = 'SKU_398437'

# L Button for GPIO17
# R Button for GPIO4
# Circle Button for GPIO23
# Square Button for GPIO22
# Trigon Button for GPIO24
# X Button for GPIO5

# BackLight for GPIO27
# IR for GPIO26

gpios = [False for x in range(40)]

wiringpi.wiringPiSetupGpio()


def pressed(n):
    if not bool(gpios[int(n)]) and not wiringpi.digitalRead(int(n)):
        gpios[int(n)] = True
        return True
    return False


def released(n):
    if bool(gpios[int(n)]) and wiringpi.digitalRead(int(n)):
        gpios[int(n)] = False
        return True
    return False


def switch(n):
    if bool(gpios[int(n)]) and wiringpi.digitalRead(int(n)):
        gpios[int(n)] = False
    return gpios[int(n)]


def set_in(n):
    wiringpi.pinMode(n, 1)


def set_out(n):
    wiringpi.pinMode(n, 0)


if __name__ == '__main__':
    pass
