# pyupbit를 이용해 데이터를 불러오는 역할

import pyupbit
import pandas as pd
from config import COIN, INTERVAL, COUNT

def get_price_data():
    """pyupbit로 시세 데이터 불러오기"""
    df = pyupbit.get_ohlcv(ticker=COIN, interval=INTERVAL, count=COUNT)
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace=True)
    return df
