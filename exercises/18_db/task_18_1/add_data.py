#!/usr/bin/python3
#-*- coding: utf-8 -*-
import time
import sqlite3
from pprint import pprint
import yaml
from tqdm import tqdm
import re
def connect(db_name):
    'создаем подключение к бд'
    connection = sqlite3.connect(db_name)
    
    return connection

def write_to_db(connection,query,datalist,table):
    'записывает данные в бд '
    print('Записываю данныe в таблицу '+ table )
    with connection:
        for data in datalist:
            try:
                connection.execute(query,data)
            except sqlite3.IntegrityError as error:
                print('При записи данных ', data ,' возникла ошибка ', error)
                continue
        
            else:
                for i in tqdm(range(len(data))):
                    time.sleep(0.1)
                connection.commit()
                print('Запись данных ',data,' прошла успешно')
                
        else:
            pass


def dhcp_snoop_out_parse(filename_list):
    device_name = ''
    match = []
    result = []
    resulted = []
    regex = re.compile('(?P<mac>\S+) +(?P<ip>(?:\d+\.)+\d+) +\d+ + \S+ +(?P<vlan>\d+) +(?P<intf>\S+\d*\/*\d*)')
    for file in filename_list:
        device_name = file.strip('.txt').split('_')[0]
        file = open(file, 'r').read()
        match = regex.findall(file)
        match = [list(tuples) for tuples in match]
        [lists.append(device_name) for lists in match]
        match =[tuple(lists) for lists in match]
        result.append(match)
        resulted = [value for i in result for value in i]
    return resulted

if __name__ == '__main__':
    datalist =[]
    with open('switches.yml') as sw_file:
        sw_file = yaml.safe_load(sw_file)
        datalist = [(key,item) for masterkey in sw_file.keys() for key,item in sw_file[masterkey].items()]
    
    write_to_db(connect('dhcp_snooping.db'),\
                        'insert into switches values (?,?)',\
                        datalist,\
                        'switches')

    write_to_db(connect('dhcp_snooping.db'),\

                        'insert into dhcp values (?,?,?,?,?)',\
                        dhcp_snoop_out_parse(\
                        ['sw1_dhcp_snooping.txt',\
                        'sw2_dhcp_snooping.txt',\
                        'sw3_dhcp_snooping.txt']),\
                        'dhcp')
