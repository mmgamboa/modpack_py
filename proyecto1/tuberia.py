#Importamos modulos generales
import sys

#importamos modulos especificos de nuestro proyecto
import lectura 
import ajuste 
#Importamos de forma diferente para claridad conceptual (se puede importar un modulo de diferentes formas)
from model import m1

archivo = sys.argv[1]

t, fuente = lectura.leo(archivo)
data_norm = lectura.normalizo(fuente)
pars = ajuste.ajusto(m1,t,data_norm)

ajuste.grafica(t, data_norm, m1,pars)