import numpy as np
import matplotlib.pyplot as plt
#just generating some random data

def mock(length = 10**5, sigma = 10, start = 10000):
    ## sigma is a standard deviation
    ## start is a starting point for abs(stoch process) (current price)
    step = start
    synthetic = []
    for i in range(length):
        synthetic.append(step)
        step = abs(np.random.normal(start, sigma))
        start = step
    return synthetic

def mock_plot(synthetic_data):
    plt.figure(figsize=(10,3))
    plt.title('Synthetic data')
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.plot(synthetic_data)
    plt.show()

mock_plot(mock())
