
# les différentes importations
import numpy as np
import matplotlib.pyplot as plt

from dtw import dtw
#from dtwalign import dtw
"""
# deux séquences numériques modélisant les sons
test =np.array([1,3,4,9,8,2,1,5,7,3,2,6,9,10]).reshape(-1,1)
ref = np.array([1,3,4,3,0,9,4,3,6,3,5,10,3,7]).reshape(-1,1)
"""
test=np.sin(2 * np.pi * 3.1 * np.linspace(0, 1, 101))
test+= np.random.rand(test.size)
ref=np.sin(2 * np.pi * 3 * np.linspace(0, 1, 120))
ref += np.random.rand(ref.size)
# état initial des signaux
plt.plot(test, label="test")
plt.plot(ref, label="ref")
plt.legend()
plt.show()

#fonction pour calculer la distance
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
mat_cout=resultat[2]
path=resultat[3]
print(resultat[0])

#visualisation du chemin
plt.imshow(mat_cout,origin="low", cmap="gray")
plt.plot(path[0], path[1], 'w',label="path")
plt.legend()
plt.show()


## alignement
##♥imporation du module dtwalign 
from dtwalign import dtw

#res est un objet de type dtwresult
res=dtw(test,ref)

#aligné le test par raaport à la référence
test_warping_path = res.get_warping_path(target="reference")
plt.plot(test[test_warping_path], label="test aligné à la ref")
plt.plot(ref, label="reference")
plt.legend()
"""
# l'inverse
"""
ref_warping_path = res.get_warping_path(target="query")
plt.plot(test, label="test")
plt.plot(ref[ref_warping_path], label="ref aligné au test")
plt.legend(loc="upper center")




