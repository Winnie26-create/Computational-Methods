import math
import numpy as np
import acuire_stock_and_option_price


def generate_correlated_random_number(random_frame1, random_frame2, ticker_name, rho_value, total_time=1 / 3,
                                      intervals=250):
    dt = total_time / intervals
    w1_list = random_frame1[ticker_name]
    independent_w_list = random_frame2[ticker_name]
    w2_list = rho_value * w1_list + math.sqrt(1 - rho_value ** 2) * independent_w_list
    w1_list = w1_list * math.sqrt(dt)
    w2_list = w2_list * math.sqrt(dt)
    return [w1_list, w2_list]


# parameter_list: [kappa, theta, sigma, rho, v0]
# brown_motion_list: 上面那个函数算出来的基于相关系数rho的随机数
# T: 期权到期时间（本案例中为4/12=1/3年）
# intervals: 模拟过程中想要划分的区间数量
def generate_volatility_list(parameter_list, brown_motion_list, T=1 / 3, intervals=250):
    kappa = parameter_list[0]
    theta = parameter_list[1]
    sigma = parameter_list[2]
    v0 = parameter_list[4]
    dW_list = brown_motion_list[1]
    volatility_list = [v0]
    dt = T / intervals
    current_v = v0
    for i in range(intervals):
        new_v = abs(current_v + kappa * (theta - current_v) * dt + sigma * np.sqrt(current_v) * dW_list[i])
        volatility_list.append(new_v)
        current_v = new_v
    return volatility_list


# r: 无风险利率
# S0: 模拟开始时标的资产价格
def generate_stock_price_list(r, S0, brown_motion_list, volatility_list, T=1 / 3, intervals=250):
    dW_list = brown_motion_list[0]
    dt = T / intervals
    stock_price_list = [S0]
    current_S = S0
    for i in range(intervals):
        new_S = current_S + r * current_S * dt + np.sqrt(volatility_list[i]) * current_S * dW_list[i]
        stock_price_list.append(new_S)
        current_S = new_S
    return stock_price_list


def heston_simulation(parameter_list, brown_motion_list, r, S0, T=1 / 3, intervals=250):
    volatility_list = generate_volatility_list(parameter_list, brown_motion_list, T, intervals)
    stock_price_list = generate_stock_price_list(r, S0, brown_motion_list, volatility_list, T, intervals)
    return stock_price_list


def calculate_option_income(stock_price_list, strike):
    strike = float(strike)
    if stock_price_list[-1] > strike:
        return stock_price_list[-1] - strike
    else:
        return 0


def calculate_option_return(stock_price_list, ticker_index, trade_date_index):
    option_price = float(acuire_stock_and_option_price.acquire_option_price(ticker_index, trade_date_index))
    option_strike = acuire_stock_and_option_price.acquire_option_middle_strike(ticker_index, trade_date_index)
    option_income = calculate_option_income(stock_price_list, option_strike)
    return (option_income / option_price) - 1
