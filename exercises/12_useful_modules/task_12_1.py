#!/usr/bin/python3

# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
def ping_ip_addresses(iplist):
    unresponse_ip = []
    avalible_ip = []
    result_list = []
    for ip in iplist:
        result = subprocess.run(['ping','-c','1',ip])
        if result.returncode == 0:
            avalible_ip.append(ip)
        else:
            unresponse_ip.append(ip)
    result_list.append(avalible_ip)
    result_list.append(unresponse_ip)
    return(tuple(result_list))

if __name__ =="__main__":
    ipl = ['8.8.8.8', '8.8.4.4', '192.168.88.221']
    print(ping_ip_addresses(ipl))

