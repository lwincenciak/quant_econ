import numpy as np
import matplotlib.pyplot as plt

ts_length = 200
# x_values = [0]  # empty list
a_list = [0, 0.95, 0.98]
colors = ['#0055DD', '#009933', '#BB0022']


def tseries(a):
    x_values = []
    x = 0
    for t in range(ts_length + 1):
        e = np.random.randn()
        x = a * x + e
        x_values.append(x)
    return x_values


fig = plt.figure(figsize=(12, 6))
plt.xlim(0, ts_length)
# plt.ylim(3.35, 3.65)

plt.rcParams.update({'font.size': 14})

i = 0
for a in a_list:
    x = tseries(a)
    plt.plot(x, linewidth=1.2, color=colors[i], label='$\\alpha = $' + str(a))
    i += 1

plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)
plt.xlabel('Time [t]')
plt.ylabel('')
plt.title('Time series for different autoregressive parameter\n$x_t = \\alpha x_{t-1} + \\varepsilon_t$')
plt.legend()
plt.show()
fig.savefig("tseries.pdf", bbox_inches='tight')
