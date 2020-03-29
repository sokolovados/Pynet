#!/usr/bin/python3
#-*- conding: utf-8 -*-

import time
import sqlite3
from tqdm import tqdm

try:
    connect = sqlite3.connect('dhcp_snooping.db')

    with open('dhcp_snooping_schema.sql') as schema:
        schema = schema.read()
        connect.executescript(schema)
    print('Creating database...')
    print('Done!')
    
except:
    print('Database already exist')
    
