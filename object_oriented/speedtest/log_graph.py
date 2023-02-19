import matplotlib.pyplot as plt
import numpy as np

#xdata = list(range(9,21,2))
#ydata = [10 ** i for i in range(9,21,2)]

xdata = [9, 11, 13, 15, 17, 19, 21]
ydata = [5, 20, 118, 250, 3389, 104753, 1181392]

kalvis_xdata = [9, 11, 13, 15, 17, 19, 21, 23]
kalvis_ydata = [6, 32, 145, 712, 3450, 23464, 159196, 1164734]

# compTimes for [9, 11, 13, 15, 17, 19] are [6, 22, 124, 278, 3846, 122361]

# convert y-axis to Logarithmic scale

fig, ax = plt.subplots()

ax.plot(kalvis_xdata, kalvis_ydata, '--go', label="NSturis_dictionary_user.py")

ax.plot(xdata, ydata, '--bo', label = "polimondi.py")

ax.set_yscale('log')

# plt.yscale("log")

# plt.xticks(np.arange(9, 21, 2.0))

ax.set_xticks(list(range(9,25,2)), minor=False)

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
