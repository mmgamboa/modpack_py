#Importamos modulo de ajuste
from scipy.optimize import curve_fit
# Importo solo modulo para graficar
import pylab as plt

#Importamos modulo especifico de nuestro proyecto
from paq_func import model

def ajusto(x,y,m,p0):
	"""Ajuste de datos utilizando modelo m y valores semilla en p0"""
	if m=='m1':
		popt, _ = curve_fit(model.m1, x, y, p0)
	elif m == 'm2':
		popt, _ = curve_fit(model.m2, x, y, p0)

	return popt

def grafica(m,x,y, pars):
	"""Esta funcion realiza un grafico y el grafico de una funcion ajustada con los mismos datos
	x: x-data de la forma de array de numpy
	y: y-data de la forma de array de numpy
	modelo: modelo utilizado para ajustar los datos
	pars: parametros ajustados del modelo"""

	plt.grid()
	plt.xlabel('t[seg]')
	plt.ylabel('I[un. arb.]')
	plt.plot(x, y, 'ko',alpha=0.5, label = 'Datos')
	if m == 'm1':
		plt.plot(x, model.m1(x, *pars), 'r-', label='Ajuste')
	elif m == 'm2':
		plt.plot(x, model.m2(x, *pars), 'r-', label='Ajuste')
	plt.legend(loc='best')
	plt.show()
