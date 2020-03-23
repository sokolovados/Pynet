#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input('Input ip : ')
IpForOctets = ip.split('.')

ipcorrect = False
if len(IpForOctets)==4:
    for ipaddress in IpForOctets:
        if ipaddress.isdigit() and int(ipaddress)>=0 and int(ipaddress)<=255:
            ipcorrect = True
        else:
            ipcorrect = False

if ipcorrect:
    if int(IpForOctets[0])==255 and int(IpForOctets[1])==255 and int(IpForOctets[2])==255 and int(IpForOctets[3])==255:
        print('This is Local Broadcast address')
    elif int(IpForOctets[0])<1 and int(IpForOctets[1])<1 and int(IpForOctets[2])<1 and int(IpForOctets[3])<1:
        print('This is Unassigned address')
    elif int(IpForOctets[0])>0 and int(IpForOctets[0])<=223:
        print('This is Unicast address')
    elif int(IpForOctets[0]) >= 224 and int(IpForOctets[0])< 239:
        print('Tgis is Multicast address')

            
else:
    print("Invalid Address")
