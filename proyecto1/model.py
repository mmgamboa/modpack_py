#Importamos modulo general
import numpy as np

def m1(x,a,loc,ancho):
	"""Modelo gausseano"""
	return( a*np.exp(-0.5*(x-loc)**2/ancho**2 ))
