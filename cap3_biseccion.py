"""
Metodo de biseccion
autor : Shigueru Nagata
Fecha : 30/10/2013
------------------------
Lo defino como funcion
para poder usarlo como modulo
y poder llamar al metodo desde
otro script.
"""

def biseccion(f,a,c,t):
	"""
	f : funcion a resolver
	a : inicio del intervalo
	c : fin del intervalo
	t : tolerancia
	"""

	if (f(a) * f(c) < 0):
		b = a
		while abs(f(b)) > t:
			b = (a + c) / 2
			if f(a) * f(b) <= 0:
				c = b
			else:
				a = b
		return b
	else:
		return "el rango no contiene raiz"
