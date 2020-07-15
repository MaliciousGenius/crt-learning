#! /usr/bin/python3

"""
Загрузка данных в CH
"""

import glob
import os
import pandas as pd
import sqlalchemy as sa

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

def data_to_ch(connect):
    filelist = glob.glob(r'input/*/*.bz2', recursive=True)
    for filename in filelist:
        df_s = pd.read_csv(filename, compression='bz2',sep='\t',dtype='unicode',header=None,names=column_names)
        df_s.to_sql("events", con = connect, if_exists='append', index = False)
        print(df_s.head())

if __name__ == "__main__":
    engine = sa.create_engine('clickhouse://default@192.168.0.155:8123/default', encoding='utf8')
    connect = engine.connect()
    data_to_ch(connect)