#Importamos modulo de ajuste
from scipy.optimize import curve_fit
# Importo solo modulo para graficar
import pylab as plt

#Importamos modulo especifico de nuestro proyecto
from model import m1

def ajusto(m,x,y):
	"""Ajuste de datos utilizando modelo m"""
	popt, _ = curve_fit(m, x, y)
	return popt

def grafica(x,y, model, pars):
	"""Esta funcion realiza un grafico y el grafico de una funcion ajustada con los mismos datos
	x: x-data de la forma de array de numpy
	y: y-data de la forma de array de numpy
	model: modelo utilizado para ajustar los datos
	pars: parametros ajustados del modelo"""

	plt.grid()
	plt.xlabel('t[seg]')
	plt.ylabel('Data[ua]')
	plt.plot(x, y, 'ko',alpha=0.5, label = 'Datos')
	plt.plot(x, model(x, *pars), 'r-', label='Ajuste')
	plt.legend(loc='best')
	plt.show()
