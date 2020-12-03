# coding=utf-8
import os
import fcntl
import struct
import psutil
import socket
import requests

__author__ = 'dolacmeo'
__project__ = 'raspberryPi3B+ 2.2TFT Pi-info'
__doc__ = 'RaspberryPi'


server_list = [
    ('www.10010.com', 80),
    ('www.baidu.com', 443),
    ('www.gov.cn', 443)
]


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


def get_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))[20:24])


def isNetOK(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False


def isOnline():
    try:
        ok = all([isNetOK(x) for x in server_list])
        if ok:
            return requests.get("http://ip.taobao.com/outGetIpInfo?ip=myip&accessKey=alibaba-inc"
                                ).json().get('data', {}).get('ip', 'UNKNOWN')
    except Exception as e:
        pass
    return "OFFLINE!"


IsOnline = isOnline()


def device_info():
    cpu = psutil.cpu_percent() * 0.01
    ram = psutil.virtual_memory().percent * 0.01
    disk = psutil.disk_usage("/").percent * 0.01
    cpu_temp = getCPUtemperature()
    return cpu, ram, disk, cpu_temp, IsOnline


if __name__ == '__main__':
    pass
