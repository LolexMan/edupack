#Codigo Generador

from funciones_generales import *
import time

#------Parametros----------
total_datos = 10
total_notas = 20
porcentaje_buenos = 0.2
porcentaje_malos  = 0.2
ls_ruido = [0.3, 0.4, 0.5]

tic = time.time()
for ruido in ls_ruido:
    dic = generar_datos(total_datos, total_notas, ruido, porcentaje_buenos, ruido, porcentaje_malos, ruido)
#Visualizacion datos
#hist_means(dic)

#Aqui vendra la prediccion
print(precision(dic))
toc = time.time()
time = toc - tic 
print(time)


#Aqui se comparara los resultados



