# import numpy as np
# import datetime
#
# data = [-214, +423, +536, -643, +255, +26, -357, -868, -359, +810]
#
# window_size = 7  # n sequential samples
# stride = 1  # overlap with last sample i.e [ 1, 2, 3, 4] next [2, 3, 4, 5]
#
# window_avg = [np.average(data[i:i+window_size]) for i in range(0, len(data), stride)
#               if i+window_size <= len(data)]
#
# date_avg = [data[i] for i in range(0, len(data), stride)
#              if i+window_size <= len(data)]
#
# print('data length : %s' % str(len(data)))
#
# print('date_avg : %s date_length : %s' % (str(date_avg), str(len(date_avg))))
#
# print('window_avg : %s window_length : %s' % (str(window_avg), str(len(window_avg))))

import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt


def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    sma = np.convolve(values, weights, 'valid')
    return sma


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 5, 1, 8, 2, 1, 6, 1, 9, 2]

b = movingaverage(y, 4)

plt.plot(x, b)
plt.show()