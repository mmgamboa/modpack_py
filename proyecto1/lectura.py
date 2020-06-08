#Importamos modulo de numpy
import numpy as np

def leo(arch):
	#leemos los datos del archivo
	t, datos = np.loadtxt(arch, unpack= True)

	return t, datos

def normalizo(datos):
	# Normalizamos los datos 
	d_norm = datos/np.max(datos)
	return d_norm