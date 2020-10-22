"""###########################
One figure - pandas
###########################"""
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data generation
# x = np.arange(10)
# y1 = np.linspace(3, 5, 10)
# y2 = np.linspace(2, 6, 10)
# d2 = pd.DataFrame().assign(X=x, Y1=y1, Y2=y2)
#
# # Magic here
# fig = plt.figure()
# plt.legend()
#
# d2.plot(kind='scatter', x='X', y='Y1', label='lab_Y1', color='r', ax=fig.gca())
# d2.plot(kind='scatter', x='X', y='Y2', label='lab_Y2', color='b', ax=fig.gca())

"""###########################
One figure - classic
###########################"""
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data generation
# x = np.arange(10)
# y1 = np.linspace(3, 5, 10)
# y2 = np.linspace(2, 6, 10)
#
# # Magic here
# ax = plt.subplot()
#
# ax.scatter(x, y1, label="lab1")
# ax.scatter(x, y2, label="lab2")
# ax.legend()

"""###########################
Two figures - classic
###########################"""
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data generation
# x = np.arange(10)
# y1 = np.linspace(3, 5, 10)
# y2 = np.linspace(2, 6, 10)
#
# # 1 way
# plt.subplot(2, 1, 1)
# plt.plot(x, y1)
# plt.ylabel('y1')
#
# plt.subplot(2, 1, 2)
# plt.plot(x, y2)
# plt.ylabel('y2')
#
# plt.show()
#
#
# # 2 way
# fig, (ax1, ax2) = plt.subplots(2, 1)
#
# ax1.plot(x, y1)
# ax1.set_ylabel('y1')
#
# ax2.plot(x, y2)
# ax2.set_ylabel('y2')