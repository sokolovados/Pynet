#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def  parse_cdp_neighbors(command_output):
    
    
    device_name = (command_output.split('>')[0]).strip('\n')
    command_list_in = (command_output.split('\n'))
    command_list = [element for element in command_list_in if element and len(element.split())  >7  and (element.split()[3]).isdigit()]
    command_list = [i.split() for i in command_list]
    result_dict = {(device_name,local_inf+local_inf2):(remote_dev,remote_inf+remote_inf2) for remote_dev,local_inf,local_inf2,*_,remote_inf,remote_inf2  in command_list}
    return(result_dict)

#f = (open('sh_cdp_n_r2.txt')).read()
#print(parse_cdp_neighbors(f))


