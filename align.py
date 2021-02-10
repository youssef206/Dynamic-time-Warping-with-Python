
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)
# generate toy data
x = np.sin(2 * np.pi * 3.1 * np.linspace(0, 1, 150))
x += np.random.rand(x.size)
y = np.sin(2 * np.pi * 3 * np.linspace(0, 1, 120))
y += np.random.rand(y.size)

plt.plot(x, label="query")
plt.plot(y, label="reference")
plt.legend()
plt.show()
#manhatan_distance=lambda x,y: np.abs(x-y)
from dtwalign import dtw
res = dtw(x, y)
print("dtw distance: {}".format(res.distance))


x_warping_path = res.get_warping_path(target="query")
plt.plot(x[x_warping_path], label="aligned query to reference")
plt.plot(y, label="reference")
plt.legend()
plt.show()