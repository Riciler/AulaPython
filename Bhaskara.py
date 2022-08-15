# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:54:38 2022
Version 1.1
@author: Ricieri
Desc: Calcula as raizes de uma equação da forma ax**2+bx+c=0
To do: Captação de erros no modulo Bhaskara
"""
import ModuloEstatist
barrav = 5 * " "
barra = 5 * "="
print(15 * barra)
print(5 * barra,"Bhaskara resolvimentos", 5 * barra)
print(15 * barra)
#%%    Entrada dos valores de a, b, c (da forma ax**2+bx+c=0)
while True:
    try:
        while True:
            a = int(input((5 * barrav) + ("Digite o Valor de a:     ")))
            if a == 0: print("Valor Invalido!")
            else: break
        b = int(input((5 * barrav) + "Digite o Valor de b:     "))
        c = int(input((5 * barrav) + "Digite o Valor de c:     "))
    except ValueError:
        print((5 * barrav) + "-Entrada Inválida.-")
    break

#%%    Decoration
print(15 * barra)
print(5 * barra,"Resolvente", 7 * barra)
print(15 * barra)

#%%    Saída de valores
conj_s = ModuloEstatist.bhaskara(a, b, c)
print((5 * barrav) + f"x1 = {conj_s[0]}")
print((5 * barrav) + f"x2 = {conj_s[1]}")
print((5 * barrav) + f"Delta = {conj_s[2]}")
print((5 * barrav) + f"{conj_s[3]}")

#%%    Decoration
print(15 * barra)
print(5 * barra,"Acabô!", 8 * barra)
print(15 * barra)

#%% Segura o programa no final para leitura
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
input("Aperte qualquer tecla para finalizar o programa.")
