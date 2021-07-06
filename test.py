#Codigo Generador

from funciones_generales import *

#------Parametros----------
total_datos = 1000000
total_notas = 20
porcentaje_buenos = 0.3
porcentaje_malos  = 0.2
prob_nr_b = 0.2
prob_nr_m = 0.2
prob_nr_r = 0.2

#Generamos los datos
dic = generar_datos(total_datos, total_notas, prob_nr_b, porcentaje_buenos, prob_nr_m, porcentaje_malos, prob_nr_r)
#Visualizacion datos
#hist_means(dic)

#Aqui vendra la prediccion
print(precision(dic))

#Aqui se comparara los resultados



