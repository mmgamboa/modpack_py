# Importo solo modulo para graficar
import pylab as plt

def grafica(x,y, model, pars):
	"""Esta funcion realiza un grafico y el grafico de una funcion ajustada con los mismos datos
	x: x-data de la forma de array de numpy
	y: y-data de la forma de array de numpy
	model: modelo utilizado para ajustar los datos
	pars: parametros ajustados del modelo"""

	plt.grid()
	plt.plot(x, y, 'ko',alpha=0.5)
	plt.plot(x, model(x, *pars), 'r-')
	plt.show()
