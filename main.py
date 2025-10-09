from data_loader import get_price_data
from indicators import add_moving_averages
from backtester import run_backtest
from utils import plot_backtest

def main():
    df = get_price_data()
    df = add_moving_averages(df)
    df = run_backtest(df)
    plot_backtest(df)

if __name__ == "__main__":
    main()
