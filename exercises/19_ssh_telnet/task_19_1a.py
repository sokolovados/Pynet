#!/home/vagrant/venv/pyneng-py3-7/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import *
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
except (AuthenticationException) as error:
    print(error)
    sys.exit()
