#! /usr/bin/python3

"""
Создание таблиц в CH
"""

import os
from clickhouse_driver import Client

def create_events_table(client):
    with open('sql/create_events_table.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

def create_clks_view(client):
    with open('sql/create_clks_view.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

if __name__ == "__main__":
    CLICKHOUSE_HOST = os.environ.get('CLICKHOUSE_HOST') or 'localhost'
    client = Client(CLICKHOUSE_HOST)
    create_events_table(client)
    create_clks_view(client)
