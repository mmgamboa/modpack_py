#Script para generar archivos de datos
# de tiempo e intensidad para cada fuente

import numpy as np
import sys
import scipy.stats as stats

proy = sys.argv[1]
num = sys.argv[2]
#100 segundos de observacion, 200 puntos
t = np.linspace(0,100, 200)

#datos
if proy == '1':
    #gaussiana con media en un valor random entre 30 y 70, y varianza = 5
    datos = 1000*stats.norm.pdf(t,np.random.randint(30,70),5 )

elif proy == '2':
    #sinusoide de amplitud A y periodo P + errores aleatorios de amplitud 1
    A, P = 10, 50
    datos = A*np.sin(t*(2*np.pi/P))
    datos += np.random.random(t.shape)


np.savetxt('proyecto{}/archivo{}.dat'.format(proy,num), np.transpose([t,datos]))