#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ipcorrect = False
ip = input('Input ip : ')
while not ipcorrect:
    
    IpForOctets = ip.split('.')


    if len(IpForOctets)==4:
        for ipaddress in IpForOctets:
            if ipaddress.isdigit() and int(ipaddress)>=0 and int(ipaddress)<=255:
                ipcorrect = True
            else:
                ipcorrect = False
                ip=input('Invalid address, Try again: ') 
                break
    else:
        ipcorrect = False
        ip=input('Invalid address, Try again: ') 

if ipcorrect:
    if int(IpForOctets[0])==255 and int(IpForOctets[1])==255 and int(IpForOctets[2])==255 and int(IpForOctets[3])==255:
        print('This is Local Broadcast address')
    elif int(IpForOctets[0])<1 and int(IpForOctets[1])<1 and int(IpForOctets[2])<1 and int(IpForOctets[3])<1:
        print('This is Unassigned address')
    elif int(IpForOctets[0])>0 and int(IpForOctets[0])<=223:
        print('This is Unicast address')
    elif int(IpForOctets[0]) >= 224 and int(IpForOctets[0])< 239:
        print('Tgis is Multicast address')

                
        
