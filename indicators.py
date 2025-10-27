# 이동평균선 계산 및 지표 관련 로직

from config import MA_PERIODS

def add_moving_averages(df):
    """
    여러 기간의 이동평균선 컬럼 추가
    ex) MA_PERIODS = [5, 20] 이면 5일선, 20일선 추가

    이동평균선 이전의 수치는 NaN으로 표시
    ex1) ma5 = 데이터 4개까지 NaN
    ex2) ma20 = 데이터 19개까지 NaN
    """
    for period in MA_PERIODS:
        df[f"ma{period}"] = df['close'].rolling(window=period).mean()
    return df
