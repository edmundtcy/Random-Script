import math

def stochastic_model_dividend(s_zero, mu, sigma, T, Z, delta):
    """Returns the value of a stock price at time T given the initial
    stock price s_zero, the drift mu, the volatility sigma, the time
    T, the random variable Z, and the dividend delta."""
    return s_zero * math.exp((mu - delta - sigma**2/2)*T + sigma * math.sqrt(T) * Z)

def expected_value_divident(s_zero, mu, T, delta):
    """Returns the expected value of a stock price at time T given the
    initial stock price s_zero, the drift mu, the volatility sigma,
    the time T, and the dividend delta."""
    return s_zero * math.exp((mu - delta)*T)

def relative_VaR(s_zero, mu, sigma, T, Z, delta, D):
    """Returns the relative value at risk of a stock price at time T
    given the initial stock price s_zero, the drift mu, the volatility
    sigma, the time T, the random variable Z, and the dividend delta."""
    return (expected_value_divident(s_zero, mu, T, delta) - (stochastic_model_dividend(s_zero, mu, sigma, T, Z, delta) + D/50))

def absolute_VaR(s_zero, mu, sigma, T, Z, delta, D):
    """Returns the absolute value at risk of a stock price at time T
    given the initial stock price s_zero, the drift mu, the volatility
    sigma, the time T, the random variable Z, and the dividend delta."""
    return (s_zero - (stochastic_model_dividend(s_zero, mu, sigma, T, Z, delta) + D/50))

def main():
    """Main function."""
    num_shares = 1000000
    s_zero = 10
    mu = 0.15
    sigma = 0.3
    T = 5/250
    Z = -1.645
    D = 0.5
    delta = math.log((s_zero + D)/s_zero)
    print("The worst price of the stock at time T is:", stochastic_model_dividend(s_zero, mu, sigma, T, Z, delta) + D/50)
    print("The expected value of the portfolio is:", num_shares*expected_value_divident(s_zero, mu, T, delta))
    print("The relative value at risk is:", num_shares*relative_VaR(s_zero, mu, sigma, T, Z, delta, D))
    print("The absolute value at risk is:", num_shares*absolute_VaR(s_zero, mu, sigma, T, Z, delta, D))

main()