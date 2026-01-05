import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import stock_price_simulation
import acuire_stock_and_option_price
import covariance_mat

parameter_set = pd.read_csv('parameter.csv')
ticker_list_l = ['AZN.L', 'BATS.L', 'BHP.L', 'DGE.L', 'HSBA.L', 'RIO.L', 'RKT.L', 'SHEL.L', 'ULVR.L', 'VOD.L']
risk_free_list = [0.054, 0.0545, 0.0541, 0.0544]


def option_monte_carlo_one_simulation(ticker_index, trade_date_index):
    parameter_list = parameter_set.iloc[ticker_index].tolist()[1:6]
    rho_value = parameter_list[3]
    risk_free_rate = risk_free_list[trade_date_index]
    ticker_name_l = ticker_list_l[ticker_index]
    random_data_list = covariance_mat.generate_random_num()
    random_data_1 = random_data_list[0]
    random_data_2 = random_data_list[1]
    brown_motion_list = stock_price_simulation.generate_correlated_random_number(random_data_1, random_data_2,
                                                                                 ticker_name_l, rho_value)
    initial_stock_price = acuire_stock_and_option_price.acquire_stock_price(ticker_index, trade_date_index)
    stock_price_path = stock_price_simulation.heston_simulation(parameter_list, brown_motion_list, risk_free_rate,
                                                                initial_stock_price)
    option_return = stock_price_simulation.calculate_option_return(stock_price_path, ticker_index, trade_date_index)
    return option_return


def multiple_options_multiple_simulations(simulation_times, trade_date_index):
    complete_return_dataframe = []
    for i in range(simulation_times):
        option_return_this_time = []
        for j in range(len(ticker_list_l)):
            option_return = option_monte_carlo_one_simulation(j, trade_date_index)
            option_return_this_time.append(option_return)
        complete_return_dataframe.append(option_return_this_time)
        print(i)
    return complete_return_dataframe


def generate_return_vector_and_covariance_matrix(simulation_times, trade_date_index):
    return_dataframe = multiple_options_multiple_simulations(simulation_times, trade_date_index)
    return_dataframe = pd.DataFrame(return_dataframe).T
    covariance_matrix = np.cov(return_dataframe)
    average_return_list = []
    for i in range(10):
        option_return_performance = return_dataframe.iloc[i]
        average_return_list.append(np.mean(option_return_performance))
    return [covariance_matrix, average_return_list]


def stock_price_monte_carlo_one_simulation(ticker_index, trade_date_index):
    parameter_list = parameter_set.iloc[ticker_index].tolist()[1:6]
    rho_value = parameter_list[3]
    risk_free_rate = risk_free_list[trade_date_index]
    ticker_name_l = ticker_list_l[ticker_index]
    random_data_list = covariance_mat.generate_random_num()
    random_data_1 = random_data_list[0]
    random_data_2 = random_data_list[1]
    brown_motion_list = stock_price_simulation.generate_correlated_random_number(random_data_1, random_data_2,
                                                                                 ticker_name_l, rho_value)
    initial_stock_price = acuire_stock_and_option_price.acquire_stock_price(ticker_index, trade_date_index)
    stock_price_path = stock_price_simulation.heston_simulation(parameter_list, brown_motion_list, risk_free_rate,
                                                                initial_stock_price)
    return stock_price_path


for i in range(5):
    stock_path = stock_price_monte_carlo_one_simulation(0, 0)
    t_list = np.linspace(0, len(stock_path) - 1, len(stock_path))
    plt.plot(t_list, stock_path)
plt.ylabel('Stock Price')
plt.xlabel('T')
plt.title('Stock_price_over_time')
plt.show()

for i in range(4):
    output_list = generate_return_vector_and_covariance_matrix(500, i)
    output_covariance_mat = pd.DataFrame(output_list[0])
    print(output_covariance_mat)
    output_covariance_mat.columns = ticker_list_l
    output_covariance_mat.to_csv('covariance_matrix_at_month' + str(i + 1) + '.csv')
    output_average_return = pd.DataFrame(output_list[1]).T
    output_average_return.columns = ticker_list_l
    output_average_return.to_csv('return_vector_at_month' + str(i + 1) + '.csv')
