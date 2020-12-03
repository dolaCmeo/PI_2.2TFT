# coding=utf-8
import os
import time
import atexit
from LIB import *

__author__ = 'dolacmeo'
__project__ = ''
__doc__ = ''

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
static_info = {
    'lan': pi_infos.get_ip('lo'),
    'wifi': pi_infos.get_ip('wlan0'),
    'www': pi_infos.isOnline()
}
start = time.time()


def get_info(k):
    global start
    if (time.time() - start) > 300:
        if k == 'lan':
            static_info['lan'] = pi_infos.get_ip('lo')
        elif k == 'wifi':
            static_info['wifi'] = pi_infos.get_ip('wlan0')
        elif k == 'www':
            static_info['www'] = pi_infos.isOnline()
        start = time.time()
    return static_info.get(k)


def gen_img(infos):
    def percent_end(percent):
        return 100 + (120 * percent)

    data = {
        'bg': os.path.join(BASE_PATH, 'bg.png'),
        'works': [
            ['text', dict(xy=(47, 10), text=str(infos[0] * 100) + "%", fill='#FFF', font='en_font')],
            ['line', dict(xy=[(100, 20), (230, 20)], fill='#FFF', width=20)],
            ['line', dict(xy=[(100, 20), (percent_end(infos[0]), 20)], fill='#00FF00', width=20)],

            ['text', dict(xy=(47, 50), text=str(infos[1] * 100) + "%", fill='#FFF', font='en_font')],
            ['line', dict(xy=[(100, 62), (230, 62)], fill='#FFF', width=20)],
            ['line', dict(xy=[(100, 62), (percent_end(infos[1]), 62)], fill='#00FF00', width=20)],

            ['text', dict(xy=(47, 90), text=str(infos[2] * 100) + "%", fill='#FFF', font='en_font')],
            ['line', dict(xy=[(100, 104), (230, 104)], fill='#FFF', width=20)],
            ['line', dict(xy=[(100, 104), (percent_end(infos[2]), 104)], fill='#00FF00', width=20)],

            ['text', dict(xy=(47, 135), text='TEMP: ' + infos[3], fill='#FFF', font='en_font')],
            ['text', dict(xy=(47, 174), text='LAN : ' + get_info('lan'), fill='#FFF', font='en_font')],
            ['text', dict(xy=(47, 216), text='WIFI: ' + get_info('wifi'), fill='#FFF', font='en_font')],
            ['text', dict(xy=(47, 260), text='WWW : ' + get_info('www'), fill='#FFF', font='en_font')],
        ]
    }

    return tft22.make_img(**data)


pages = [
    None,
    {'bg': os.path.join(BASE_PATH, 'images', 'dola_sc2.jpg')},
    {'bg': os.path.join(BASE_PATH, 'images', 'giraffe.bmp')},
    {'bg': os.path.join(BASE_PATH, 'images', 'lambo.bmp')},
    {'bg': os.path.join(BASE_PATH, 'images', 'radioP.bmp')},
]


def main():
    count = 0
    page = 0
    BackLight = True
    print "STRAT!!!"
    while True:

        if count == 5:
            count = 0
            if page == 0:
                tft22.display(gen_img(pi_infos.device_info()))

        if keys.pressed(17):
            print 'L button pressed'
            page -= 1
        if keys.pressed(4):
            print 'R button pressed'
            page += 1

        if page < 0:
            page += len(pages)
        elif page >= len(pages):
            page -= len(pages)

        if keys.released(17):
            print 'L button released'
            if page > 0:
                tft22.display(tft22.make_img(**pages[page]))
        if keys.released(4):
            print 'R button released'
            if page > 0:
                tft22.display(tft22.make_img(**pages[page]))

        if keys.pressed(23):
            print 'Circle button pressed'
        if keys.released(23):
            print 'Circle button released'
            BackLight = not BackLight
            if BackLight:
                keys.set_out(27)
            else:
                keys.set_in(27)
        if keys.pressed(22):
            print 'Square button pressed'
        if keys.released(22):
            print 'Square button released'
        if keys.pressed(24):
            print 'Trigon button pressed'
        if keys.released(24):
            print 'Trigon button released'
        if keys.pressed(5):
            print 'X button pressed'
        if keys.released(5):
            print 'X button released'
            break

        count += 1
        time.sleep(.02)


@atexit.register
def clean():
    tft22.display(tft22.make_img(**{'bg': os.path.join(BASE_PATH, 'images', 'stopP.bmp')}))
    print 'bye~'


if __name__ == '__main__':
    main()
    pass
