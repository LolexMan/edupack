# Edupack
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
	ls= [] # inicializamos la lista vacia

	# Iteramos aumentando en la lista los numeros aleatorios
	for i in range(lend):
		ls.append(round(rd.uniform(min,max),2)) # Redondeamos a dos decimales
	return ls

	
def est_bueno(re,n):
	"""Crea el perfil de un estudiante bueno cuyas notas están el rago (8.0,10.0)
		input:
			re -> Tamaño de la lista
			n -> Propabilidad de la nota rara rango (4.0,6.0)
		output:
			ls -> Lista de nota de un estudiante bueno"""
	ls= lista_aleatoria(re,8.0,10.0) # Creamos una lista aleatoria de un rango que oscila de 8.0 a 10.0
	for i in range(re):
		dado= rd.uniform(0,1) # Creamos un dado que nos da una probabilidad de 0 y 1
		if dado < n:
			ls[i]= round(rd.uniform(4,7.5),2) # Modificamos la nota "i" de las notas con una nota en un rango entre 4.0 a 6.0
	return ls


def est_malo(re,n):
	"""Crea el perfil de un estudiante malo cuyas notas están el rago (5.0,7.0)
		input:
			re -> Tamaño de la lista
			n -> Propabilidad de la nota rara rango (4.0,6.0)
		output:
			ls -> Lista de nota de un estudiante bueno"""
	ls= lista_aleatoria(re,5.0,7.0) # Creamos una lista aleatoria con un rango que oscila de 5.0 a 7.0
	for i in range(re):
		dado= rd.uniform(0,1) # Creamos un dado que nos da una probabilidad de 0 y 1
		if dado < n:
			ls[i]= round(rd.uniform(7.0,9.5),2) # Modificamos la nota "i" de las notas con una nota en un rango entre 8.0 a 9.5
	return ls


def est_reg(re,pm,pb):
	"""Crea el perfil de un estudiante regular cuyas notas están el rago (6.0,8.0)
		input:
			re -> Tamaño de la lista
			pm -> Propabilidad de nota mala de un rango (4.0,6.0)
			pb -> Probabilidad de nota buena de un rango (8.0,9.5)
		output:
			ls -> Lista de nota de un estudiante regular"""
	ls= lista_aleatoria(re,6.0,8.0) # Creamos una lista aleatoria con un rango que oscila de 6.0 a 8.0
	for i in range(re):
		dado= rd.uniform(0,1) # Creamos un dado que nos da una probabilidad de 0 y 1
		if dado < pm:
			ls[i]= round(rd.uniform(4.0,6.0),2) # Modificamos la nota "i" de las notas con un rango entre 4.0 a 6.0
		elif dado >= pm and dado < pm + pb:
			ls[i]= round(rd.uniform(8.0,9.5),2) # Modificamos la nota "i" de las notas con un rango entre 8.0 a 9.5
	return ls

def count_mala(ls):
	"""Contador de cuántas notas malas tuvo en su registro rango de 0 a 6
		input:
			ls -> Lista de notas del estudiante
		output:
			cont -> Cuenta de las notas malas"""
	cont = 0 # El contador inicial será cero
	for el in ls: # el es para los elementos de la lista
		if el < 6.0: # Condicionamos que si el elemento es menor que seis este sumará las notas en +1
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
		if el > 8.0: # Condicionamos que si el elemento es mayor que 8 este sumará las notas en +1
			cont += 1 
	return cont 

def generar_datos(N,notas,pf_b,db,pf_m,dm,pf_rb,pf_rm):
	"""Generador de datos del estudiante desde su id que desplegará sus notas
		input:
			N -> Id del estudiante
			notas -> registro de notas del estudiante
			pf_b -> propabilidad de una nota rara de estudiante bueno
			db -> densidad de estudiante bueno
			pf_m -> probabilidad de nota rara de estudiante malo
			dm -> densidad de estudiante malo
			pf_rb -> probabilidad de una nota buena estudiante regular
			pf_rm -> propabilidad de una nota mala estudiante regular
			
		output: 
			dic -> Diccionario con los datos de un estudiante"""
	
	dic= {}
	for i in range(N):
		dado= rd.uniform(0,1)
		if dado < dm: # Condicional de si el estudiante que ingresa será malo
			dic[i]= est_malo(notas,pf_m)
		elif dado >= dm and dado < dm + db: # Condicional de si el estudiante que ingresa será bueno
			dic[i]= est_bueno(notas,pf_b)
		else:
			dic[i]= est_reg(notas,pf_rm, pf_rb) # Condicional de si el estudiante que ingresa será regular

	return dic


def histograma(dic,est): # Función para crear un histograma de un estudiante selecto
	pyplot.hist(dic[est],bins= 17)
	m = np.mean(dic[est])
	s = np.std(dic[est])
	pyplot.axvline(m, linestyle="--", color="r")
	pyplot.axvline(m-s, linestyle="--", color="g")
	pyplot.axvline(m+s, linestyle="--", color="g")
	pyplot.show()

def prof_rango(dic,est,min,max):
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

