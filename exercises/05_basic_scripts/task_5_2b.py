#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

network = argv[1]
mask = network.split('/')[1]
ip = (network.split('/')[0]).split('.')

binmask = '1'*int(mask)+'0'*(32-int(mask))
binmask = [int(binmask[:8],2),\
        int(binmask[8:16],2),\
        int(binmask[16:24],2),\
        int(binmask[24:32],2)]

binip = [bin(int(ip[0]))[2:],\
        bin(int(ip[1]))[2:],\
        bin(int(ip[2]))[2:],\
        bin(int(ip[3]))[2:]]


binip = [('0'*(8-int(binip[0])))+binip[0],\
        ('0'*(8 - int(binip[1])))+binip[1],\
        ('0'*(8-int(binip[2])))+binip[2],\
        ('0'*(8-int(binip[3])))+binip[3]]
binip = (''.join(binip))[:int(mask)] + '0'*(32-int(mask))

net = [int(binip[0:8],2),int(binip[8:16],2),int(binip[16:24],2),int(binip[24:32],2)]

template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:08b} {6:08b} {7:08b} {8:08b}
'''

print(template.format(int(net[0]),int(net[1]),int(net[2]),int(net[3]),('/'+mask),int(binmask[0]),int(binmask[1]),int(binmask[2]),int(binmask[3])))

