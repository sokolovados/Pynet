#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re

def get_ints_without_description(filename):
    regex= 'interface +(?P<interface>\S+\d+\/?\d*\S*)|(?P<descr> description.+)'
    resultlist = []
    interface = ''
    with open(filename,'r') as file:
        for string in file:
            match = re.search(regex,string)
            if match:
                if match.lastgroup == 'interface':
                    if interface:
                        resultlist.append(interface)
                        interface = match.group(match.lastgroup)
                    else:
                        interface = match.group(match.lastgroup)
                elif match.lastgroup == 'descr':
                    interface = ''
                    continue
            else:
                continue
        else:
            if interface:
                resultlist.append(interface)

    return(resultlist)

print(get_ints_without_description('config_r1.txt'))
