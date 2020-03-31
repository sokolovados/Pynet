#!/home/vagrant/venv/pyneng-py3-7/bin/python3

# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import *
from paramiko.ssh_exception import SSHException
import time
import sys
import yaml

command =  'sh ip int br\n'
try:
    with open('devices.yaml') as devices :
        templates = yaml.safe_load(devices)
        for devices in templates:
            print('Connection to device {}'.format(devices['ip']))
            with ConnectHandler(**devices) as ssh:
                ssh.enable()
                result = ssh.send_command(command)
                print(result)
except (AuthenticationException,NetMikoTimeoutException,SSHException) as error:
    print(error)

