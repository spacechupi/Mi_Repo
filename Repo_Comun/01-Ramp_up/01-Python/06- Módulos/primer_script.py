# -*- coding: utf-8 -*-
"""
Ejemplo de un módulo python.
Contiene una variable llamada pi,
una función para calcular el área de un círculo de radio r
y una clase llamada Punto.
"""

import math

pi = math.pi

def area_circulo(radio):
    """
    Función que devuelve el área de un círculo de radio r
    
    Parameters
    ----------
    radio : TYPE float

    Returns 
    -------
    area : TYPE float

    """
    return pi * radio ** 2

class Punto:
    """
    Clase que instancia puntos en dos dimensiones
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def formato(self):
        return "(" + str(self.x) + ", " + str(self.y) + "()"
    
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x < 0 and self.y < 0:
            return 4
        elif self.x != 0 and self.y == 0:
            return "x"
        elif self.y != 0 and self.x == 0:
            return "y"
        else:
            return 0
    
    def distancia(self, p):
        """
        Calcula la distancia del punto a otro punto

        """
        d = math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return d