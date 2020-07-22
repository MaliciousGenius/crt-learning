#! /usr/bin/python3

"""
Создание таблицы в CH
"""
import os

from clickhouse_driver import Client

def create_logs_table(client):
    with open('sql/create_logs_table.sql') as f:
        query = f.read()
        client.execute(query)

def create_prep_table(client):
    with open('sql/create_prep_table.sql') as f:
        query = f.read()
        client.execute(query)

def create_prep_view(client):
    with open('sql/create_prep_view.sql') as f:
        query = f.read()
        client.execute(query)

if __name__ == "__main__":
    CLICKHOUSE_HOST = os.environ.get('CLICKHOUSE_HOST') or 'localhost'
    client = Client(CLICKHOUSE_HOST)
    # create_logs_table(client)
    # create_prep_table(client)
    create_prep_view(client)

