# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:39:22 2017

@author: Leonardo Venancio
Ultimo trabalho de eletricidade
"""
#primeira simulação

from sympy import init_printing, symbols, diff, sin, cos

init_printing()

x = symbols("x")

f = sin(x**2)+ cos(x) #digitar a equação senoidal

derivada = diff(f,x)

print derivada

