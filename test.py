#Codigo Generador
from funciones_generales import *
import time

#------Parametros----------
total_datos = 100000
total_notas = 20
porcentaje_buenos = 0.2
porcentaje_malos  = 0.2
ls_ruido = [0.1,0.2, 0.3, 0.4, 0.5]



for ruido in ls_ruido:
        dic = generar_datos(total_datos, total_notas, ruido, porcentaje_buenos, ruido, porcentaje_malos, ruido)
        hist_means(dic,'hist_ruido_'+str(ruido)+'.png')


# tic = time.time()
# ls = []
# for ruido in ls_ruido:
#         acc = 0
#         for i in range(100):
#             dic = generar_datos(total_datos, total_notas, ruido, porcentaje_buenos, ruido, porcentaje_malos, ruido)
#             acc += precision(dic)
#         ls.append(acc/100)
# print( ls )


#Aqui vendra la prediccion

# toc = time.time()
# time = toc - tic 
# print(time)


#Aqui se comparara los resultados



