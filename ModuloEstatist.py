# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 13:41:41 2022
Version 1.0
@author: Ricieri
Modules for statistical use

To do:
"""
#%% --> Módulos
import math

#%% OK
def somatorio(*x):
    '''soma n valores'''
    soma = 0
    for e1 in x:
        soma += e1
    return soma

#%% OK
def media(*x):
    '''calcula a média de um conjunto de valores'''
    n = len(x)
    med = somatorio(*x) / n
    return med

#%% OK
def variancia(*x):
    '''calcula a variancia de um conjunto'''
    n = len(x)
    var = 0
    for e2 in x:
        var += ((e2 - media(*x))**2)/(n-1)
    return var

#%% OK
def desvio_padrao(*x):
    '''retorna o desvio padrão de um conjunto'''
    desvp = math.sqrt(variancia(*x))
    return desvp


#%% OK
def estatisticas(*x):
    print(somatorio(*x))
    print(media(*x))
    print(variancia(*x))
    print(desvio_padrao(*x))

#%%
def bhaskara(a, b ,c):
    delta = (b ** 2 - 4 * a * c)
    x1 = (- b + cmath.sqrt(delta)) / 2 * a
    x2 = (- b - cmath.sqrt(delta)) / 2 * a
    if delta < 0:
        mens = "Não existem raízes reais"
    elif delta == 0:
        mens = "Existe uma raiz real"
    else:
        mens = "Existem duas raizes reais"
    return(x1, x2, delta, mens)

