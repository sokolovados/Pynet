#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

network = input('Введите ip-сеть в формате x.x.x.x/x: ')
template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}

Mask:
{4}
{5:<8} {6:<8} {7:<8} {8:<8}
{5:08b} {6:08b} {7:08b} {8:08b}
'''
mask = network.split('/')[1]
net = (network.split('/')[0]).split('.')
binmask = '1'*int(mask)+'0'*(32-int(mask))
binmask = [int(binmask[:8],2),int(binmask[8:16],2),int(binmask[16:24],2),int(binmask[24:32],2)]


print(template.format(int(net[0]),int(net[1]),int(net[2]),int(net[3]),('/'+mask),int(binmask[0]),int(binmask[1]),int(binmask[2]),int(binmask[3])))











