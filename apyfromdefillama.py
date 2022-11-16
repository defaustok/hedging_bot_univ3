from defillama2 import DefiLlama
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style, cm
import datetime as dt
import matplotlib.ticker as mtick
obj = DefiLlama()

 # See https://defillama.com/yields for the meaning of columns.

def import_apy(pair,chain_uni,version_uni):
    obj = DefiLlama()
    df = obj.get_pools_yields()
    cols = ['chain','project','symbol','pool', 'poolMeta']
    is_true = (df.chain == chain_uni) & (df.project == ('uniswap-'+str(version_uni)))
    df = df.loc[is_true, cols]
    df = df[['chain','project','symbol','pool', 'poolMeta']].dropna()
    df['symbol'] = df['symbol']+ ' ' + df['poolMeta']
    df = df[['symbol', 'pool']]
    pool_address = ((df.loc[df['symbol'] == pair, 'pool'])).iloc[0]
    hist_apy = obj.get_pool_hist_apy(pool_address)
    hist_apy = hist_apy[['apy']]
    hist_apy.index = pd.to_datetime(hist_apy.index)
    return hist_apy