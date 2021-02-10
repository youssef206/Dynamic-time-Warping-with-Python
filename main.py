# -*- coding: utf-8 -*-


# les diffÃ©rentes importations
import numpy as np
import matplotlib.pyplot as plt
import librosa
from dtw import dtw
import librosa.display
from numpy.linalg import norm


#lecture des fichiers audio
#y la forme d'onde
#sr pour l'échantillonage
y1, sr1 = librosa.load('test_09b.wav') 
y2, sr2 = librosa.load('10_ostende.wav')
test=y1
ref=y2
#affichage du graphe 
plt.plot(y1,label="test")
plt.plot(y2,label="ref")
#ajout des lÃ©gendes
plt.legend()
plt.show()

#calcul des MFCC
#pour le fichier test
mfcc1 = librosa.feature.mfcc(y1,sr1)  
librosa.display.specshow(mfcc1)
plt.colorbar()
plt.title('MFCC test')
plt.tight_layout()
plt.show()

#pour la ref
mfcc2 = librosa.feature.mfcc(y2,sr2)  
librosa.display.specshow(mfcc2)
plt.colorbar()
plt.title('MFCC ref')
plt.tight_layout()
plt.show()
"""
def distance(x,y):
    return lambda x,y: np.abs(x-y)

manhattan_distance = distance(mfcc1.T,mfcc2.T)
"""


dist, cost, acc_cost, path = dtw(mfcc1.T, mfcc2.T,dist=lambda x, y: norm(x - y, ord=1))
    
plt.imshow(cost.T, origin='lower', cmap="gray", interpolation='nearest')
plt.plot(path[0], path[1], 'w',label="path")
plt.legend()
plt.show()

print ("la distance est egale", dist)

from dtwalign import dtw
res=dtw(mfcc1.T,mfcc2.T)
x_path = res.path[:,0]
y_path = res.path[:,1]
plt.plot(test[x_path],'--',label="aligned query")
plt.plot(ref[y_path],label="aligned reference")
plt.legend()
plt.show()