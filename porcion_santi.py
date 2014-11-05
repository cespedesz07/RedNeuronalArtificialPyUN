#Función que actualiza los pesos luego de comparar cada entrada en X con y
#El proceso se repite el número de veces que indique el parámetro numIteraciones
def entrenar( self, numIteraciones, tasa_aprendizaje=1 ):
	self.tasa_aprendizaje = tasa_aprendizaje
	n = self.X.shape[0]
	for i in range(numIteraciones):
		indice = list( range(n) )	
		np.random.shuffle( indice )

		for fila in index:
			x = self.X[fila]
			y = self.y[fila]
			self.actualizacion_pesos(x, y)


def predecir_x( self, x ):
	return self.feedforward(x)


def predecir( self, X ):
	n = len(X)
	m = self.tamanos[-1]
	ret = np.ones( (n, m) )
	for i in range( len(X) ):
		ret[ i, : ] = self.feedforward( X[i] )
	return ret


#Función que representa la función de activación Sigmoidea
def sigmoidea(x):
	return 1.0  /  ( 1 + np.exp(-x) )


#Función que representa la derivada de la función de activacion
#sigmoidea
def sigmoidea_prima(x):
	expresion = np.exp(-x)
	return expresion  /  ( (1+expresion)**2 )