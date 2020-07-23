#! /usr/bin/python3

"""
Загрузка данных в CH
"""

import os
import gc
import glob

import multiprocessing as mp
import pandas as pd
import pandahouse as ph

files = glob.glob(r'input/*/*.bz2', recursive=True)

ch_conn_str = {
    'host': 'http://' + os.environ.get('CLICKHOUSE_HOST') + ':8123/',
    'database': 'default',
    'password': ''
}

column_names = [
    'id',
    'type',
    'datetime',
    'date',
    'server',
    'ipAddress',
    'ipProxy',
    'country',
    'language',
    'searchType',
    'programType',
    'adType',
    'adDisplayType',
    'idFeed',
    'idAdvertiser',
    'idCampaign',
    'idGroup',
    'idAd',
    'idPublisher',
    'idSite',
    'idChannel',
    'idDomain',
    'idGroupSite',
    'idGroupSiteChannel',
    'position',
    'keywords',
    'freeKeywords',
    'destinationUrl',
    'refererUrl',
    'userAgent',
    'browser',
    'status',
    'fraudCause',
    'spent',
    'adminRevenue',
    'pubRevenue',
    'idSearchType',
    'idConversion',
    'conversionValue',
    'idCategory',
    'capping',
    'budget',
    'displayUrl',
    'misc1',
    'misc2',
    'misc3',
    'vars',
    'subId',
    'deviceType',
    'os',
    'vendor',
    'device',
    'carrier',
    'idGroupChannelType',
    'ns',
    'httpReferer',
    'source'
]

def loader(file):
    print('Загружаю:' + file)
    df = pd.read_csv(file, compression='bz2', sep='\t', dtype='unicode', header=None, names=column_names)
    ph.to_clickhouse(df, 'events', index=False, chunksize=20000, connection=ch_conn_str)
    gc.collect()

if __name__ == "__main__":
    pool = mp.Pool()
    pool.map_async(loader, files)
    pool.close()
    pool.join()
