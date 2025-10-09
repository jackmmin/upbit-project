# 공통 함수들 (로그 출력, 시각화 등)

import matplotlib.pyplot as plt

def plot_backtest(df):
    """전략 누적수익률 시각화"""
    plt.figure(figsize=(12,6))
    plt.plot(df['date'], df['cumulative_market'], label='Market', linestyle='--')
    plt.plot(df['date'], df['cumulative_strategy'], label='Strategy')
    plt.legend()
    plt.title("Backtest Result")
    plt.show()
