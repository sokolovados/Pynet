#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
template = '{0:<8}  {1} {2:>8}'
vlan_out = {}
vlan_list = []

with open('CAM_table.txt','r') as mac_table:
    for string in mac_table:
        if 'DYNAMIC' in string:
            string = string.split()
            vlan_out[string[0]] = string
            vlan_list.append(int(string[0]))
        else:
            continue
    vlan_list.sort()
vlan  = input('Input VLAN: ')
if vlan_out.get(vlan) is not None:
    print(template.format(vlan_out[str(vlan)][0],vlan_out[str(vlan)][1],vlan_out[str(vlan)][3]))
else:
    print('Invalid VLAN')
