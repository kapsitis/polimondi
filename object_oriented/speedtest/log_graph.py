import matplotlib.pyplot as plt
import numpy as np

#xdata = list(range(9,21,2))
#ydata = [10 ** i for i in range(9,21,2)]

xdata = [9, 11, 13, 15, 17, 19]
ydata = [5, 20, 118, 250, 3389, 104753]
# ydata = [6, 22, 124, 278, 3846, 122361]
#        [6, 39, 314, 2065]
# [9, 11, 13, 15, 17, 19]
# kalvis_ydata = [8, 41, 312, 2108, 14254, 115610]
# kalvis_ydata = [7, 34, 218, 1394, 9161, 71750]
kalvis_ydata =  [7, 35, 220, 1422, 9852, 71829]

# compTimes for [9, 11, 13, 15, 17, 19] are [6, 22, 124, 278, 3846, 122361]

# convert y-axis to Logarithmic scale

fig, ax = plt.subplots()

ax.plot(xdata, ydata, '--bo', label = "Marta")

ax.plot(xdata, kalvis_ydata, '--go', label="Kalvis")

ax.set_yscale('log')

# plt.yscale("log")

# plt.xticks(np.arange(9, 21, 2.0))

ax.set_xticks(list(range(9,21,2)), minor=False)

ax.yaxis.get_major_locator().set_params(numticks=99)
ax.yaxis.get_minor_locator().set_params(numticks=99, subs=[.25, .5, .75])

# plt.plot(xdata, ydata, '--bo')
plt.grid(color='0.90')
plt.legend()
ax.set_ylabel('milliseconds')
ax.set_xlabel('n - the number of sides')


plt.title('Enumerating Magic n-Polyiamonds')

# fig.savefig('speedtest.png', dpi = 100)

plt.show()
