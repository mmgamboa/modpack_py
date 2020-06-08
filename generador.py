#Script para generar archivos de datos
# de tiempo e fuente

import numpy as np
import sys
import scipy.stats as stats

proy = sys.argv[1]
num = sys.argv[2]
#100 segundos de observacion, 200 puntos
t = np.linspace(0,100, 200)

#datos
datos = np.random.random(t.shape)
datos += 1000*stats.norm.pdf(t,np.random.randint(30,70),5 )

np.savetxt('proyecto{}/archivo{}.dat'.format(proy,num), np.transpose([t,datos]))