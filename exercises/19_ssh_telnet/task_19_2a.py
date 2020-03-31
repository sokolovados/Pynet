#!/home/vagrant/venv/pyneng-py3-7/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''

import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import *
import sys
import yaml
from sys import argv

def send_config_commands(device, config_commands,verbose=True):
    try:
        print('Connect to {}'.format(device['ip']))
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            result = ssh.send_config_set(config_commands)
            if verbose:
                print(result)
    except (AuthenticationException,NetMikoTimeoutException,SSHException) as error:
        print(error)
commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

with open ('devices.yaml','r') as file:
    file = yaml.safe_load(file)
for diction in file:
    send_config_commands(diction,commands,verbose = False)
 
