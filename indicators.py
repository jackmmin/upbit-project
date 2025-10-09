# 이동평균선 계산 및 지표 관련 로직

from config import MA_PERIODS

def add_moving_averages(df):
    """여러 기간의 이동평균선 컬럼 추가"""
    for period in MA_PERIODS:
        df[f"ma{period}"] = df['close'].rolling(window=period).mean()
    return df
