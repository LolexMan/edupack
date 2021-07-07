
# Edupac
# Codigo Funciones generador
# Autor: Steven Cisneros

import random as rd
import numpy as np
from matplotlib import pyplot

def lista_aleatoria(lend, min, max):
	""" Funcion que genera una lista con numeros aleatorios en un rango (min, max) de longitud lend
		input: 
			lend -> tamaño de la lista
			min -> cota inferior de los aleatorios
			max -> cota superior de los aleatorios
		output: 
			ls -> list aleatoria
	"""
	ls= [] 
	# inicializamos la lista vacia

	# Iteramos aumentando en la lista los numeros aleatorios
	for i in range(lend):
		ls.append(round(rd.uniform(min,max),2)) 
				# Redondeamos a dos decimales
	return ls

	
def est_bueno(re,n):
	"""Crea el perfil de un estudiante bueno cuyas notas están el rago (8.0,10.0)
		input:
			re -> Tamaño de la lista
			n -> Propabilidad de la nota rara rango (4.0,6.0)
		output:
			ls -> Lista de nota de un estudiante bueno"""
	ls= lista_aleatoria(re,8.0,10.0) 
	# Creamos una lista aleatoria de un rango que oscila de 8.0 a 10.0
	for i in range(re):
		dado= rd.uniform(0,1) 
		# Creamos un dado que nos da una probabilidad de 0 y 1
		if dado < n:
			ls[i]= round(rd.uniform(4,7.5),2) 
			# Modificamos la nota "i" de las notas con una nota en un rango entre 4.0 a 6.0
	return ls


def est_malo(re,n):
	"""Crea el perfil de un estudiante malo cuyas notas están el rago (5.0,7.0)
		input:
			re -> Tamaño de la lista
			n -> Propabilidad de la nota rara rango (4.0,6.0)
		output:
			ls -> Lista de nota de un estudiante bueno"""
	ls= lista_aleatoria(re,5.0,7.0) 
	# Creamos una lista aleatoria con un rango que oscila de 5.0 a 7.0
	for i in range(re):
		dado= rd.uniform(0,1) 
		# Creamos un dado que nos da una probabilidad de 0 y 1
		if dado < n:
			ls[i]= round(rd.uniform(7.0,9.5),2) 
			# Modificamos la nota "i" de las notas con una nota en un rango entre 8.0 a 9.5
	return ls


def est_reg(re,pnr):
	"""Crea el perfil de un estudiante regular cuyas notas están el rago (6.0,8.0)
		input:
			re -> Tamaño de la lista
			pnr -> Propabilidad de nota rara
		output:
			ls -> Lista de nota de un estudiante regular"""
	ls= lista_aleatoria(re,6.0,8.0) 
	# Creamos una lista aleatoria con un rango que oscila de 6.0 a 8.0
	for i in range(re):
		dado= rd.uniform(0,1) 
		# Creamos un dado que nos da una probabilidad de 0 y 1
		if dado < pnr:
			dado2 = rd.uniform(0,1)
			# Segundo dado para con 50% de probabilidad elegir una nota entre 3 - 6 o 8 -9.5
			if dado2 <= 0.5:
				ls[i]= round(rd.uniform(8.0,9.5),2) 
				# Modificamos la nota "i" de las notas con un rango entre 8.0 a 9.5
			else:
				ls[i]= round(rd.uniform(3.0,6.0),2) 
				# Modificamos la nota "i" de las notas con rango entre 3.0 a 6.0
	return ls

def count_mala(ls):
	"""Contador de cuántas notas malas tuvo en su registro rango de 0 a 6
		input:
			ls -> Lista de notas del estudiante
		output:
			cont -> Cuenta de las notas malas"""
	cont = 0 
	# El contador inicial será cero
	for el in ls: 
	# el es para los elementos de la lista
		if el < 6.0: 
		# Condicionamos que si el elemento es menor que seis este sumará las notas en +1
			cont += 1 
	return cont 

def count_buena(ls):
	"""Contador de cuántas notas buenas tuvo el estudiante en su registro rango 0 a 8
	input:
		ls -> Lista de notas del estudiante
	output:
		cont -> Cuenta de las notas buenas""" 
	cont = 0 
	for el in ls:
		if el > 8.0: 
			# Condicionamos que si el elemento es mayor que 8 este sumará las notas en +1
			cont += 1 
	return cont 

def generar_datos(N,notas,pf_b,por_b,pf_m,por_m,pnr_r):
	"""Generador de datos del estudiante desde su id que desplegará sus notas
		input:
			N -> Numero total de estudiantes
			notas -> registro de notas del estudiante
			pf_b -> propabilidad de una nota rara de estudiante bueno
			por_b -> Porcentaje de estudiantes bueno
			pf_m -> probabilidad de nota rara de estudiante malo
			por_m -> porcentaje de estudiante malos
			pnr_r -> probabilidad de una nota rara en un estudiante regular
			
		output: 
			dic -> Diccionario con los datos de un estudiante"""
	
	dic= {}
	cont=0
	for i in range(N):
		dado= rd.uniform(0,1)
		if dado < por_m: 
		# Condicional de si el estudiante que ingresa será malo
			dic[i]= est_malo(notas,pf_m)
		elif dado >= por_m and dado < por_m + por_b: 
		# Condicional de si el estudiante que ingresa será bueno
			dic[i]= est_bueno(notas,pf_b)
		else:
			cont+=1
			dic[i]= est_reg(notas,pnr_r) 
			# Condicional de si el estudiante que ingresa será regular
			
	return dic


def histograma(dic,est): 
	""" Función para crear un histograma de un estudiante selecto
	"""
	pyplot.hist(dic[est],bins= 17)
	m = np.mean(dic[est])
	s = np.std(dic[est])
	pyplot.axvline(m, linestyle="--", color="r")
	pyplot.axvline(m-s, linestyle="--", color="g")
	pyplot.axvline(m+s, linestyle="--", color="g")
	pyplot.show()

def prob_rango(dic,est,min,max):
	"""Probabilidad de que una nota de un estudiante este en un rango dado por min y max
		input:
			dic -> Diccionario
			est -> id del estudiante
			min -> rango mínimo
			max -> rango máximo
		output:
			P -> Probabilidad
		"""
	cont = 0
	for nota in dic[est]:
		if nota <= max and nota >= min:
			cont += 1
	T= len(dic[est])
	P=  round(cont/T,2)
	return P  

def grafica_notas(dic,est):
	"""Gráfica que muestra el rendimiento del estudiante en relación al tiempo
		input:
			dic -> Diccionario
			est -> Id estudiante
		output:
			pyplot -> gráfica"""
	pyplot.plot(range(len(dic[est])),dic[est]) 
	# Se identifica el rango que tendrá la gráfica
	m = np.mean(dic[est]) 
	s = np.std(dic[est]) 
	pyplot.axhline(m, linestyle="--", color="r") 
	# Linea que permitirá observar el promedio del estudiante
	pyplot.axhline(m-s, linestyle="--", color="g") 
	pyplot.axhline(m+s, linestyle="--", color="g")
	pyplot.show()

def aprueba(ls):
	"""Verifica qué estudiante aprueba
		input:
			ls -> lista de notas
		output:
			ap -> aprobado"""
	if np.mean(ls) >= 7.0:
		ap=1
	else:
		ap=0
	return ap

def ls_apro(dic):
	"""Lista de estudiantes aprobados
		input:
			dic -> diccionario
		output:
			ls_ap -> Lista de 1 y 0, donde 1 es aprobado 0 suspenso"""
	ls_ap = []
	for est in list(dic.values()):
		ls_ap.append(aprueba(est))
	return ls_ap

def n_apro(dic):
	"""Número de estudiantes aprobados
		input:
			dic -> diccionario
		output:
			número de estudiantes aprobados"""
	return np.sum(ls_apro(dic))

def hist_means(dic):
	""" 
		Funcion que obtiene un histograma de los promedios de todos los estudiantes
	"""
	ls_mean = [] 
	# Lista vacia donde se almacenaran los promedios de cada clase
	ls_notas = list(dic.values()) 
	# Se obtiene las notas de los estudiantes
	for notas in ls_notas:
		mean = np.mean(notas) 
		# Calculamos el promedio de la clase
		ls_mean.append(mean) 
		# Añadimos el promedio a la lista
	pyplot.hist(ls_mean,bins= 15) 
	#Creamos un histograma
	m = np.mean(ls_mean) 
	# Calculamos el promedio de los promedios
	s = np.std(ls_mean) 
	# Calculamos la desviacion estandar de los promedios
	
	# Aqui graficamos
	pyplot.title('Histograma Promedios')
	pyplot.xlabel("Promedios")
	pyplot.axvline(m, linestyle="--", color="r") 
	pyplot.axvline(m-s, linestyle="--", color="g")
	pyplot.axvline(m+s, linestyle="--", color="g")
	pyplot.show()
	
def pred_notas(notas, num_pred):
	filt = notas[0:len(notas)-num_pred]
	prom = np.mean(filt)
	des_est = np.std(filt)
	min_int = prom - des_est
	max_int = prom + des_est
	pred = lista_aleatoria(num_pred, min_int, max_int)
	nueva_lista = filt + pred
	return nueva_lista

def prediccion(dic, num_pred):
	n = len(dic) 
	# Obtenemos el tamaño del diccionario
	ls = []
	# Lista vacia, se llenara de 1 y 0 
	for i in range(n):
		# Obtenemos la prediccion de las notas
		pred_aprob = aprueba(pred_notas(dic[i], num_pred))
		# Determinamos si en la prediccion el est aprueba
		ls.append(pred_aprob)
		# Agregamos a la lista
	return ls 
	
	
def precision(dic):
	real = ls_apro(dic)
	pred = prediccion(dic, 8)
	acc = 0
	for i in range(len(real)):
		if real[i] == pred[i]:
			acc += 1
	precision = acc/ len(real) *100
	return precision