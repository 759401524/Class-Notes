import numpy as np
import matplotlib.pyplot
import pandas
import sklearn
print('success')
a1 = np.arange(10)
a2 = np.arange(9).reshape(3, 3)
a3 = np.arange(10).reshape(2, -1)
a41 = np.arange(10).reshape(2, -1)
a42 = np.repeat(1, 10).reshape(2, -1)
b4 = np.vstack(a41, a42)
a51 = np.arange(10).reshape(2, -1)
a52 = np.repeat(1, 10).reshape(2, -1)
b5 = np.hstack(a51, a52)
a6 = np.max(np.arange(9).reshape(3, 3), axis=1)
