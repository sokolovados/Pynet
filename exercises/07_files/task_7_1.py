#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
a = '''
Protocol:           {0:}
Prefix:             {1:}
AD/Metric:          {2:}
Next-Hop:           {3:}
Last Update:        {4:}
Outbound Interface: {5:} 
'''

with open('ospf.txt','r') as ospfout:
    for ospf in ospfout:
        ospf = ospf.split()
        print(a.format('OSPF',ospf[1],ospf[2].strip('[]'),ospf[4].strip(','),ospf[5].strip(','),ospf[6]))
        




#            O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0

    

