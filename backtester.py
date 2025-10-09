# 이동평균선 교차 전략으로 백테스트 수행

import pandas as pd

def run_backtest(df):
    """단순 이동평균선 교차전략 백테스트"""
    df['signal'] = 0
    df['signal'][df['ma5'] > df['ma20']] = 1
    df['signal'][df['ma5'] < df['ma20']] = -1

    df['position'] = df['signal'].shift(1)
    df['returns'] = df['close'].pct_change()
    df['strategy'] = df['returns'] * df['position']

    df['cumulative_market'] = (1 + df['returns']).cumprod()
    df['cumulative_strategy'] = (1 + df['strategy']).cumprod()

    return df
