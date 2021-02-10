# les différentes importations

import numpy as np
import matplotlib.pyplot as plt

from dtw import dtw


np.random.seed(1234)

test=np.sin(2 * np.pi * 3.1 * np.linspace(0, 1, 101))
test+= np.random.rand(test.size)
ref=np.sin(2 * np.pi * 3 * np.linspace(0, 1, 120))
ref += np.random.rand(ref.size)

# état initial des signaux
plt.plot(test, label="test")
plt.plot(ref, label="réference")
plt.legend()
plt.show()

def distance(x,y):
    return lambda x,y: np.abs(x-y)



manhattan_distance = distance(test,ref)



"""         la fonction DTW
    prend en entrée:
    les deux vecteurs
    la mesure de distance
    
    renvoie:
        la distance: resultat[0]
        la matrice des couts : resultat [1]
        le path : resultat[3]
"""


resultat = dtw(test, ref, dist=manhattan_distance)
distance=resultat[0]
mat_cout=resultat[2]
path=resultat[3]


#visualisation du chemin

plt.imshow(mat_cout,origin="low", cmap="gray")
plt.plot(path[0], path[1], 'w',label="path")
plt.legend()
plt.show()


## alignement
##imporation du module dtwalign 
from dtwalign import dtw

#res est un objet de type dtwresult
res=dtw(test,ref)



#aligné le test par raaport à la référence

test_warping_path = res.get_warping_path(target="query")
plt.plot(test[test_warping_path], label="test aligné à la ref")
plt.plot(ref, label="réference")
plt.legend()
plt.show()

# aligné la reférence à la test

ref_warping_path = res.get_warping_path(target="reference")
plt.plot(test, label="test")
plt.plot(ref[ref_warping_path], label="réference aligné au test")
plt.legend()
plt.show()




