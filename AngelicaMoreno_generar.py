import numpy as np

#Funcion que retorna numeros aleatorios siguiendo la distribucion discreta de probabilidad dada
# PUNTO 2
def sample_1(N):
	p = [-10,-5,3,9]
	a = [0.1,0.4,0.2,0.3]
	rta = numpy.random.choice(p,N,a)
	return rta

#Funcion que retorna numeros aleatorios siguiendo la distribucion discreta de probabilidad exponencial dada

def sample_2(N):
	b = 0.5
	rta = numpy.random.choice(b,N)
	return rta

#Funcion que retorna M promedios asociados a dada la funcion de sampleo.
def get_mean(sampling_fun,N,M):
	#Lista que me retorna los N promedios
	prome = []
	#Ciclo que me genera las el M promedios 
	for i in range(N):
		actual = sampling_fun(M)
		prome.append(actual)

	promedios = np.array(prome)

	return promedios

#Funcion que crea archivos con los datos arrojados por la aplicacion de  la funcion get_mean

M = 1000
N = [10, 100, 1000]
Np = ['10', '100', '1000']
nombres = ['sample_1','sample_2']

#Creacion de los txt dados con sample_1
for i in range(len(N)):
	u = i-1
	name = nombres[0] + Np[u]
	datos = get_mean(nombres[0],N[u],M)	
	np.savetxt(name, datos)

#Creacion de los txt dados con sample_2
for i in range(len(N)):
	u = i-1
	name = nombres[1] + Np[u]
	datos = get_mean(nombres[1],N[u],M)	
	np.savetxt(name, datos)
	
#PUNTO 3

#Funcion que a  distribucion normal con promedio y desviacion estandar

	
