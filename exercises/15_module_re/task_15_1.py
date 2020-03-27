# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
def get_ip_from_cfg(filename):
    file = open(filename,'r').read()
    result = re.finditer(r'(\S+) + '
                         r'([\d.]+) +'
                         r'\w+ +\w+ +'
                         r'(up|donw|administratively down) +'
                         r'(up|down)',file)
for match in result:
    print(match)
    groups.append(match.groups())
    return(groups)
print(get_ip_from_cfg('config_r1.txt'))
