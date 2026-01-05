import yfinance as yf
import pandas as pd


def acquire_stock_price(ticker_name_index, trade_date_index):
    ticker_list = ['AZN.L', 'BATS.L', 'BHP.L', 'DGE.L', 'HSBA.L', 'RIO.L', 'RKT.L', 'SHEL.L', 'ULVR.L', 'VOD.L']
    ticker_name = ticker_list[ticker_name_index]
    trade_date_list = ['2024-01-17', '2024-02-16', '2024-03-15', '2024-04-17']
    trade_date_later = ['2024-01-18', '2024-02-17', '2024-03-16', '2024-04-18']
    trade_date = trade_date_list[trade_date_index]
    next_trade_date = trade_date_later[trade_date_index]
    ticker = yf.Ticker(ticker_name)
    ticker_historical_price = ticker.history(start=trade_date, end=next_trade_date, interval='1d')
    return ticker_historical_price['Open'].tolist()[0]


def acquire_option_price(ticker_name_index, trade_date_index):
    ticker_list_no_l = ['AZN', 'BATS', 'BHP', 'DGE', 'HSBA', 'RIO', 'RKT', 'SHEL', 'ULVR', 'VOD']
    ticker_name = ticker_list_no_l[ticker_name_index]
    csv_file_name = ticker_name + ' portfolio construction sheet.csv'
    csv_file = pd.read_csv(csv_file_name)
    return csv_file.iloc[trade_date_index + 4, 5]


def acquire_option_middle_strike(ticker_name_index, trade_date_index):
    ticker_list_no_l = ['AZN', 'BATS', 'BHP', 'DGE', 'HSBA', 'RIO', 'RKT', 'SHEL', 'ULVR', 'VOD']
    ticker_name = ticker_list_no_l[ticker_name_index]
    csv_file_name = ticker_name + ' portfolio construction sheet.csv'
    csv_file = pd.read_csv(csv_file_name)
    return csv_file.iloc[trade_date_index + 4, 6]