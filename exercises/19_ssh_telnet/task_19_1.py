#!/home/vagrant/venv/pyneng-py3-7/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import getpass
from netmiko import ConnectHandler
import time
import sys
import yaml

command =  'sh ip int br\n'

with open('devices.yaml') as devices :
    templates = yaml.safe_load(devices)
    for devices in templates:
        print('Connection to device {}'.format(devices['ip']))
        with ConnectHandler(**devices) as ssh:
            ssh.enable()

            result = ssh.send_command(command)
            print(result)
