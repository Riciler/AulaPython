# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:54:38 2022
Version 0.1
@author: Ricieri
Desc: Calcula as raizes de uma equação da forma ax**2+bx+c=0
To do: Captação de erros
"""
import cmath

#%% Definindo a função Bhaskara
def bhaskara(a, b ,c):
    '''calcula x1, x2, delta e compara delta para se descobrir o numero de
    raizes, retornando todos e uma mensagem na forma de (x1, x2, delta, mens)
    '''
    delta = ((b ** 2) - 4 * a * c)
    #if delta < 0: raise ValueError("Não existem raízes reais")
    x1 = (- b + cmath.sqrt(delta)) / 2 * a
    x2 = (- b - cmath.sqrt(delta)) / 2 * a
    if delta < 0:
        mens = "Não existem raízes reais"
    elif delta == 0:
        mens = "Existe uma raiz real"
    else:
        mens = "Existem duas raizes reais"
    return(x1, x2, delta, mens)

#%%    Decoration
barrav = 5 * " "
barra = 5 * "="
print(15 * barra)
print(5 * barra,"Bhaskara resolvimentos", 5 * barra)
print(15 * barra)
#%%    Entrada dos valores de a, b, c (da forma ax**2+bx+c=0)

a = int(input((5 * barrav) + "Digite o Valor de a:     "))
b = int(input((5 * barrav) + "Digite o Valor de b:     "))
c = int(input((5 * barrav) + "Digite o Valor de c:     "))
#%%    Decoration
print(15 * barra)
print(5 * barra,"Resolvente", 7 * barra)
print(15 * barra)

#%%    Saída de valores
conj_s = (bhaskara(a, b, c))
print((5 * barrav) + f"x2 = {conj_s[0]}")
print((5 * barrav) + f"x2 = {conj_s[1]}")
print((5 * barrav) + f"x2 = {conj_s[2]}")
print((5 * barrav) + f"x2 = {conj_s[3]}")

#%%    Decoration
print(15 * barra)
print(5 * barra,"Acabô!", 8 * barra)
print(15 * barra)
