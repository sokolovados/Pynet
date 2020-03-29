#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import re
from pprint import pprint
from task_17_2 import parse_sh_cdp_neighbors
import yaml

def generate_topology_from_cdp(list_of_files,save_to_filename=None):
    '''
    генерирует словарь связей cdp из нескольких файлов
    При передаче второго аргумента - записывает в yaml файл
    '''
    multi_out_cdp = {}
    for cdp_neigh in list_of_files:
        cdp_neigh = open(cdp_neigh,'r').read()
        multi_out_cdp.update(parse_sh_cdp_neighbors(cdp_neigh))
    if save_to_filename:
        with open(save_to_filename,'w') as out_yaml_file:
            yaml.dump(multi_out_cdp,out_yaml_file)

    return(multi_out_cdp)
    

if __name__ == '__main__':
    list_of_file =['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt','sh_cdp_n_r4.txt','sh_cdp_n_r5.txt','sh_cdp_n_r6.txt']
    pprint(generate_topology_from_cdp(list_of_file,'topology.yaml'))
