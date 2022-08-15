# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:17:38 2022
Version 0.1
@author: Ricieri
Desc: Conta a ocorrencia de elementos em uma string
To do: captação de erros, conversão para string das entradas, generalização das descrições(diferenciar letras e numeros no resultado), contar sem casesensitivity
"""
#%% Entrada de Valores

texto = input("Insira o texto a serem contadas os caracteres:    ")

#%% Entrada e verificacao do letra a ser contada

while True:
    letra = input("Insira a letra a ser contada:     ")
    if len(letra) == 1:
        break
    else:
        print("Mais de uma letra inserida")

#%% saida de valores

print(f"O texto contém {texto.count(letra)} letras {letra}")
