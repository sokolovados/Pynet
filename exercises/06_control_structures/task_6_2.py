#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Input ip : ')
IpForOctets = ip.split('.')
if '255.255.255.255' in ip:
#if int(IpForOctets[0])==255 and int(IpForOctets[1])==255 and int(IpForOctets[2])==255 and int(IpForOctets[3])==255:
    print('This is Local Broadcast address')
elif int(IpForOctets[0])<1 and int(IpForOctets[1])<1 and int(IpForOctets[2])<1 and int(IpForOctets[3])<1:
    print('This is Unassigned address')
elif int(IpForOctets[0])>0 and int(IpForOctets[0])<=223:
    print('This is Unicast address')
elif int(IpForOctets[0]) >= 224 and int(IpForOctets[0])< 239:
    print('Tgis is Multicast address')
else:
    print('This is Unused address')
