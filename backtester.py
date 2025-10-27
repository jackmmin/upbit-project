# 이동평균선 교차 전략으로 백테스트 수행

import pandas as pd

def run_backtest(df):
    """단순 이동평균선 골든크로스 전략 백테스트"""
    # 안전한 할당, 롱 전용(현물) 예시, 수수료 반영
    fee = 0.05 # 업비트 KRW 지정가, 시장가 수수료

    # 이동평균선 계산
    df['ma5'] = df['close'].rolling(window=5).mean()
    df['ma20'] = df['close'].rolling(window=20).mean()
    df['ma60'] = df['close'].rolling(window=60).mean()

    # 골든크로스 조건 설정
    # 조건: 5일선 > 20일선 > 60일선 일 때 매수 신호 발생
    # 3️⃣ 매수/매도 신호 설정
    df['signal'] = 0
    # 매수: 5 > 20 > 60
    df.loc[(df['ma5'] > df['ma20']) & (df['ma20'] > df['ma60']), 'signal'] = 1
    # 매도: 단기 < 장기 (추세 붕괴)
    df.loc[df['ma5'] < df['ma60'], 'signal'] = 0
    # 포지션 설정 (다음 캔들에 반영)
    df['position'] = df['signal'].shift(1).fillna(0)
    # 수익률 및 전략 계산
    df['returns'] = df['close'].pct_change().fillna(0)
    df['trade'] = df['position'].diff().abs().fillna(0)
    df['strategy'] = (df['returns'] * df['position'] - df['trade'] * fee).fillna(0) # 전략의 실제 기간별 수익률을 계산
    # 누적 수익률 계산
    df['cumulative_market'] = (1 + df['returns']).cumprod() # 시장 누적 수익률(지수화)을 계산
    df['cumulative_strategy'] = (1 + df['strategy']).cumprod() # 전략 누적 수익률 계산

    return df
