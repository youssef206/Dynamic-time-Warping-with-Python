
import numpy as np
import matplotlib.pyplot as plt

# generate toy data
x = [1,2,6,4,8]

y = [4,8,6,7,0]






from dtwalign import dtw
res = dtw(x, y)

print("dtw distance: {}".format(res.distance))


x_warping_path = res.get_warping_path(target="query")
plt.plot(x[x_warping_path], label="aligned query to reference")
plt.plot(y, label="reference")
plt.legend()
plt.ylim(-1, 3)