#! /usr/bin/python3

"""
Создание таблицы в CH
"""
from clickhouse_driver import Client

def create_table(client):
    with open('sql/create_events_table.sql') as f:
        query = f.read()
        client.execute(query)

if __name__ == "__main__":
    client = Client('clickhouse')
    create_table(client)
