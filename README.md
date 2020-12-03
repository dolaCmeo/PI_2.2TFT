# 2.2TFT-LCD (SKU_398437) Driver
![SKU_398437](https://github.com/dolaCmeo/PI_2.2TFT/raw/main/infos/CNC-IMG-8177.jpg)

## Product introduction

### [Introduction]
High PPI 2.2 inch TFT Display Shield for Raspberry Pi 3B/2B/B+/A+ 
With 6 Keyboards and Remote IR; 
It's fit to raspberry pi 3 model B 2B/B+/A+; 
with 6 customized button, with IR function. 
you can customize your button function for your application.

### [Features]
+ Demensions: 65mm x 56.5mm, it's a standard raspberry pi HAT expansion size;
+ Resolution: 320 x 240, 2.2 inch, High PPI display screen;
+ With 6 keyboards;
+ With IR function;
+ Support official Raspberry pi case

### [Link]
<raspberrypiwiki.com/index.php/2.2_inch_TFT_Display_SKU:398437>

## Driver
> **Used Python2 by dolacmeo**

### LIBs
+ `/LIB/tft22` TFT driver
+ `/LIB/keys` keys driver

### DEMO

#### Setup LCD
**Use the shell script (Recommend)**
Please refer to [Ugeek LCD user manual](http://raspberrypiwiki.com/Ugeek_LCD_user_manual) (NEW!)

    sudo rpi-update
    git clone https://github.com/geekworm-com/22LCD-script.git
    cd 22LCD-script
    chmod +x screen_setup.sh
    sudo ./screen_setup.sh
or

    sudo rpi-update
    wget https://raw.githubusercontent.com/geekworm-com/22LCD-script/master/screen_setup.sh
    chmod +x screen_setup.sh
    sudo ./screen_setup.sh

#### Setup Buttons
**How to DIY the six button**
Log in Raspberry by ssh and install related python and software

    $sudo apt-get update
    $sudo apt-get install libudev-dev
    $sudo apt-get install python-pip
    $sudo pip install wiringpi
    $sudo pip install python-uinput
    $sudo pip install wiringpi
    $sudo pip install Pillow
    $sudo pip install requests

#### Start!

1. Download


2. RUN

    `python demo.py`

3. PI Infos

    1. CPU
    2. RAM
    3. DISK
    4. TEMP
    5. LAN
    6. WLAN
    7. PUBLIC IP

4. KEYs

    + ◀ / ▶ :  Change screen
    + 🔴 : Backlight
    + 🟥 : NONE
    + 🔺 : NONE
    + ❌ : QUIT (display "STOP")

5. For DEV

```
L Button for GPIO17
R Button for GPIO4
Circle Button for GPIO23
Square Button for GPIO22
Trigon Button for GPIO24
X Button for GPIO5

BackLight for GPIO27
IR for GPIO26
```
