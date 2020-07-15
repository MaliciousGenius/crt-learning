#! /usr/bin/python3

"""
Загрузка данных в CH
"""

import os
import gc
import glob
import time

import pandas as pd
import pandahouse as ph

filelist = glob.glob(r'input/*/*.bz2', recursive=True)

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

if __name__ == "__main__":

    print(len(filelist))
    count=1
    for filename in filelist:
        print('--------')
        print(filename)
        df = pd.read_csv(filename, compression='bz2', sep='\t', dtype='unicode', header=None, names=column_names)
        ph.to_clickhouse(df, 'logs', index=False, chunksize=20000, connection=ch_conn_str)
        df.info(verbose=False)
        print (str(count))
        count=count+1
        gc.collect()
        time.sleep(5)
