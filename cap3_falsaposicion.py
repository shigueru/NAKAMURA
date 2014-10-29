"""
Metodo de la Falsa Posicion
autor : Shigueru Nagata
Fecha : 31/10/2013
----------------------------
Lo defino como funcion
para poder usarlo como
modulo y poder llamar
al metodo desde otro
script
"""

def FalsaPosicion(f,a,c,t):
	"""
	f : funcion a resolver
	a : inicio del intervalo
	c : fin del intervalo
	t : tolerancia
	"""

	def medio(fm,am,cm):
		w = ((am * fm(cm)) - (cm * fm(am))) / (fm(cm) - fm(am))
		return w
	if f(a) * f(c) < 0:
		b = a
		while abs(f(b)) > t:
			b = medio(f,a,c)
			if f(a) * f(b) <= 0:
				c = b
			else:
				a = b
		return b
	else:
		return "el rango no contiene raiz"
