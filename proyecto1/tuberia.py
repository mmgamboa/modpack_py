#Importamos modulos generales
import sys

#importamos modulos especificos de nuestro proyecto
import lectura 
import ajuste 
#Importamos de forma diferente para claridad conceptual (se puede importar un modulo de diferentes formas)
from model import m1,m2

archivo = sys.argv[1]
model_number = sys.argv[2]

t, fuente = lectura.leo(archivo)
data_norm = lectura.normalizo(fuente)
pars = ajuste.ajusto(t,data_norm, model_number)

ajuste.grafica(model_number,t, data_norm, pars)