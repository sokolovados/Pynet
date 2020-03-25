#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.

    result_list.append(unresponse_ip)
    result_list.append(unresponse_ip)

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''

def convert_ranges_to_ip_list(ipranges):
    result_dict = []
    for ip_range in ipranges:
        ip_range = ip_range.split('-')
        if len(ip_range) == 1:
            result_dict.append(''.join(ip_range))
            continue
        else:
            for ip_ranges in range(int(((ip_range[0]).split('.'))[-1]),int(((ip_range[1]).split('.'))[-1])+1):
                result_dict.append('{}.{}.{}.{}'.format(ip_range[0].split('.')[0],\
                                                        ip_range[0].split('.')[1],\
                                                        ip_range[0].split('.')[2],\
                                                        ip_ranges))
    return(result_dict)



print(convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']))
