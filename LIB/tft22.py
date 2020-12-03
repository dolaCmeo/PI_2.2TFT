# coding=utf-8
import os
import struct
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter

__author__ = 'dolacmeo'
__project__ = 'raspberryPi3B+ 2.2TFT LCD'
__doc__ = 'SKU_398437'

TFT_LCD = r'/dev/fb1'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
fonts_dir = os.path.join(BASE_PATH, 'fonts')


def load_font(filename, size=20):
    return ImageFont.truetype(os.path.join(fonts_dir, filename), size)


fonts = {
    'en_font': load_font('StarseedPro.ttf'),
    # 'cn_font': load_font('siyuan.ttf'),
}


def is_chinese(string):
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def make_img(bg, works=None):
    img = Image.open(bg)
    draw = ImageDraw.Draw(img)
    if works:
        for do in works:
            if do[0] == 'text':
                if do[1].get('font') is None:
                    do[1]['font'] = 'en_font'
                    # do[1]['font'] = 'cn_font' if is_chinese(do[1]['text']) else 'en_font'
                if do[1]['font'] in fonts.keys():
                    do[1]['font'] = fonts[do[1]['font']]
                draw.text(**do[1])
            elif do[0] == 'line':
                draw.line(**do[1])
    return img


def display(img):
    w, h = img.size
    rotate = w < h

    def write_bin(f, pixel_list):
        for pix in pixel_list:
            r = (pix[0] >> 3) & 0x1F
            g = (pix[1] >> 2) & 0x3F
            b = (pix[2] >> 3) & 0x1F
            f.write(struct.pack('H', (r << 11) + (g << 5) + b))
        f.close()
    if rotate:
        # img = img.transpose(Image.ROTATE_90)
        # img = img.transpose(Image.ROTATE_180)
        img = img.transpose(Image.ROTATE_270)
    img = img.resize((320, 240), Image.ANTIALIAS)
    write_bin(open(TFT_LCD, 'wb'), list(img.getdata()))
    pass


if __name__ == '__main__':
    pass
