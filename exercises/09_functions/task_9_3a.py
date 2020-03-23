# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_filename):
    dict_of_access = {}
    dict_of_trunk = {}
    result_list = []
    access_vlan = ''
    interface = ''
    trunk_vlan = ''
    with open(config_filename,'r') as config:
        for string in config:
            if 'interface' in string:
                if not access_vlan and not trunk_vlan and interface:
                    dict_of_access[interface] = 1
                interface = (string.split())[1]
                access_vlan = ''
                trunk_vlan = ''
            elif 'access vlan' in string:
                access_vlan  = int(string.split()[3])
                dict_of_access[interface] = access_vlan
            elif 'allowed vlan' in string:
                trunk_vlan = (string.split()[4]).split(',')
                trunk_vlan = [int(vlan) for vlan in trunk_vlan]
                dict_of_trunk[interface]= trunk_vlan
    result_list = [dict_of_access,dict_of_trunk]
    return(tuple(result_list))

print(get_int_vlan_map('config_sw2.txt'))
