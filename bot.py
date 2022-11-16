import os
from binance.client import Client
from datetime import datetime, timedelta
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sn
from binance_getprice import *
from apyfromdefillama import *
import mplfinance as mpf
from decouple import config
api_key = config('api_key')
api_secret = config('api_secret')
client = Client(api_key, api_secret)

btc = get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, '10 Nov, 2022', '15 Nov, 2022')
apy = import_apy('WETH-USDC 0.3%','Arbitrum','v3')
new = btc.join(apy, how = 'left').ffill()
new = new[['Open', 'apy']]
new