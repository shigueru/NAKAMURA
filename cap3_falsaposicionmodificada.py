"""
Metod de la Falsa Posicion Modificada
autor : Shigueru Nagata
fecha : 31/10/2013
--------------------------------------
Lo defino como funcion
para poder usarlo como
modulo y poder llamar
al metodo desde otro script
"""

def FalsaPosicionMod(f,a,c,t):
	"""
	f : funcion a resolver
	a : inicio del intervalo
	c : fin del intervalo
	t : tolerancia
	"""

	kr = 0
	kl = 0
	fa = f(a)
	fc = f(c)
	if f(a) * f(c) < 0:
		b = a
		fb = f(b)
		while abs(fb) > t:
			b = ((a * fc) - (c * fa)) / (fc - fa)
			fb = f(b)
			if fa * fb <= 0:
				c = b
				fc = fb
				kr = 0
				kl += 1
				if kl > 1:
					fa = fa / 2
			else:
				a = b
				fa = fb
				kl = 0
				kr += 1
				if kr > 1:
					fc = fc / 2
		return b
	else:
		return $return "el rango no contiene raiz"$
