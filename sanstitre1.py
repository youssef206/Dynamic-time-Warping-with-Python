import numpy as np
import matplotlib.pyplot as plt
from dtw import *
import numpy as np
import matplotlib.pyplot as plt


test=[1,3,4,9,8,2,1,7,3]
ref=[1,6,2,3,0,9,4,3,6,3]

manhatan_distance = abs(test-ref)

res = dtw(test,tref,manhatan_distance)

print(res)
