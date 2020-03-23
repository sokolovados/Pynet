# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    dict_of_access = {}
    dict_of_trunk = {}
    result_list = []
    with open(config_filename,'r') as config:
        for string in config:
            if 'interface' in string:
                interface = (string.split())[1]
            elif 'access vlan' in string:
                access_vlan  = int(string.split()[3])
                dict_of_access[interface] = access_vlan
            elif 'allowed vlan' in string:
                trunk_vlan = (string.split()[4]).split(',')
                trunk_vlan = [int(vlan) for vlan in trunk_vlan]
                dict_of_trunk[interface]= trunk_vlan
    result_list = [dict_of_access,dict_of_trunk]
    return(tuple(result_list))



