import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
ticker_list = ['AZN.L', 'BATS.L', 'BHP.L', 'DGE.L', 'HSBA.L', 'RIO.L', 'RKT.L', 'SHEL.L', 'ULVR.L', 'VOD.L']
ticker_list_no_l = ['AZN', 'BATS', 'BHP', 'DGE', 'HSBA', 'RIO', 'RKT', 'SHEL', 'ULVR', 'VOD']
complete_return_list = []


def calculate_stock_return(price_list):
    return_list = []
    for i in range(1, len(price_list)):
        return_list.append((price_list[i]/price_list[i-1] - 1))
    return return_list


def fit_missing_stock_price(complete_date_list, incomplete_date_list, incomplete_stock_price):
    missing_date_list = []
    for i in range(len(complete_date_list)):
        date = complete_date_list[i]
        if date not in incomplete_date_list:
            missing_date_list.append(i)
    output_list = incomplete_stock_price
    for missing_date in missing_date_list:
        missing_price = 0.5 * (incomplete_stock_price[missing_date-1] + incomplete_stock_price[missing_date])
        output_list = output_list[:missing_date] + [missing_price] + output_list[missing_date:]
    return output_list


index = 0
ticker = yf.Ticker(ticker_list[index])
ticker_historical = ticker.history(start='2022-12-30', end='2023-12-31', interval='1d')
complete_trading_date = ticker_historical.index.tolist()
for index in range(len(ticker_list)):
    ticker = yf.Ticker(ticker_list[index])
    ticker_historical = ticker.history(start='2022-12-30', end='2023-12-31', interval='1d')
    ticker_open_frame = ticker_historical.iloc[:, 1]
    incomplete_ticker_open_list = ticker_open_frame.tolist()
    incomplete_trading_date_list = ticker_open_frame.index
    ticker_open_list = fit_missing_stock_price(complete_trading_date, incomplete_trading_date_list, incomplete_ticker_open_list)
    ticker_return_list = calculate_stock_return(ticker_open_list)
    complete_return_list.append(ticker_return_list)
covariance_matrix = np.corrcoef(np.array(complete_return_list))
sns.heatmap(covariance_matrix, annot=True, xticklabels=ticker_list_no_l, yticklabels=ticker_list_no_l)
plt.title('Correlation of Stock Returns, Year 2023')
plt.show()
# 随机数生成环节
mean_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def generate_random_num():
    random_number_data1 = np.random.multivariate_normal(mean_vector, covariance_matrix, 250)
    random_data_1 = pd.DataFrame(random_number_data1)
    random_number_data2 = np.random.multivariate_normal(mean_vector, covariance_matrix, 250)
    random_data_2 = pd.DataFrame(random_number_data2)
    random_data_2.columns = ticker_list
    random_data_1.columns = ticker_list
    return [random_data_1, random_data_2]