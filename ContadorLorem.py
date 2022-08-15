# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 13:17:38 2022
Version 0.1
@author: Ricieri
Desc: Conta a ocorrencia de elementos em uma string
To do: captação de erros, conversão para string das entradas, generalização das descrições(diferenciar letras e numeros no resultado), contar sem casesensitivity
"""
texto = input("Insira o texto a serem contadas as letras:    ")
letra = input("Insira a letra a ser contada:     ")
print(f"O texto possui {texto.count(letra)} letras {letra}")