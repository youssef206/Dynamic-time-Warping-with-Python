
# les différentes importations
import numpy as np
import matplotlib.pyplot as plt
from dtw import dtw

# deux séquences numériques modélisant les sons
test =[1,3,4,9,8,2,1,5,7,3]
ref = [1,6,2,3,0,9,4,3,6,3]

# état initial des signaux
plt.plot(test, label="test")
plt.plot(ref, label="ref")
plt.legend()


# calcul de la distance 

manhattan_distance = lambda x, y: np.abs(x - y)

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
#visualisation
plt.imshow(mat_cout)
plt.plot(path[0],path[1],'w')
#You can also visualise the accumulated cost and the shortest path

plt.imshow(mat_cout,origin="low", cmap="gray")
plt.plot(path[0], path[1], 'w',label="path")
plt.legend()
plt.show()


## alignement
test_path = path[:0]
ref_path = path[:1]
ref_warping_path = resultat.get_warping_path(target="reference")
plt.plot(test, label="query")
plt.plot(test[test_warping_path], label="aligned reference to query")
plt.legend()
plt.ylim(-1, 3)




