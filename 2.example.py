import numpy as np
import matplotlib.pyplot as plt

ts_length = 200
# x_values = [0]  # empty list
a_list = [0, 0.8, 0.98]


def tseries(a):
    x_values = [0]
    for t in range(ts_length):
        e = np.random.randn()
        # e = np.random.uniform(0, 1)
        x = a * x_values[t] + e
        x_values.append(x)
    return x_values


for a in a_list:
    x = tseries(a)
    plt.plot(x, label='a = ' + str(a))

plt.legend()
plt.show()
