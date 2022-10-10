# -*- coding: utf-8 -*-
"""
Programa: Simulação MRUV com erro artificial
Descrição: gera a partir dos dados de entrada (tempo, n° de medidas, condições
iniciais) um arquivo com as medidas das posições acrescidas de um erro gerado
aleatoriamente

Versão:
Data de Criação: 10/10/2022 18:55:28
"""
#%% Importação de módulos
import numpy as np
import os
import matplotlib.pyplot as plt

#%%Entrada dos valores
##Tempo

while True:
    t1 = float(input("Insira o tempo inicial (Apenas números): \n"))  #TODO: capturar erro quando input != numeros
    t2 = float(input("Insira o tempo final (Apenas números): \n"))
    # verifica se delta t será positivo
    if t2<t1: #and t1&t2 in int or float: TODO: verificar para strings
        print("O tempo final não pode ser maior que o tempo inicial: \n")
    else:
        break
    
## n de medidas ao longo do experimento

while True:
    n = int(input("Qual foi o número de medidas? \n"))
    # verifica se n>0
    if n <= 0:
        print("O número de medidas deve ser um número natural! \n")
    else:
        break
    
## condições iniciais da particula

x0 = float(input("Insira a posição inicial da particula: \n"))
v0 = float(input("Insira a velocidade inicial da particula: \n"))    
a = float(input("Insira a aceleração da particula: \n"))
      
#%% Processamento de dados  
# gerando uma array com os tempos das medidas
t = np.linspace(t1, t2, n) #gera a array de t1 à t2 com n argumentos

# gerando as medidas de posição
pos = x0 + v0*t + (0.5)*a*t**2 

# forçando um erro na medida
erro = np.random.normal(loc=0, scale=1, size=pos.size)

Xmedido = pos + erro

#%% Saída de dados
# cria um diretorio para a saida de dados 
wdir = os.getcwd()
data_dir = None
try:
    data_dir = os.mkdir(wdir + "\\DataOutput")
except: pass

# seleciona o diretorio
data_dir = wdir + "\\DataOutput\\"    

# nomeia o arquivo
data_loc = data_dir + input("Digite o nome do arquivo:\n \n")

print('')  # estética
print('')

# concatenando os dados para saída
dados = np.stack((Xmedido, t))

# salvando os dados
np.savetxt(data_loc, dados)

#%% Gerando o gráfico da simuação (opcionalmente)

print('Para gerar o gráfico do experimento insira a letra \"s\", para prosseguir\
com o fim do programa insira qualquer outro ou aperte enter \n\n')
     
g = input("Deseja gerar o gráfico?:     ")

if g == 's': #gera o gráfico caso o usuario tenha confirmado
    plt.scatter(t, Xmedido,c='green',s=2)
    
    #criando um tempo especial para os gráficos
    te = np.linspace(min(t),max(t),100)
    
    ## ajustando uma curva de 1o e umas de 2o grau às medidas
    #  segundo grau
    pol2o = np.polyfit(t, Xmedido, 2)
    X2o = pol2o[2]
    V2o = pol2o[1]
    A2o = 2 * pol2o[0]
    pos2o = X2o + V2o * te + A2o * te **2
    
    #primeiro grau
    pol1o = np.polyfit(t, Xmedido, 1)
    X1o = pol1o[1]
    V1o = pol1o[0]
    pos1o = X1o + V1o*te
    
    #gerando os gráficos
    plt.plot(te, pos2o, c='black', label='Modelo 2o grau')
    plt.plot(te, pos1o, c='red', label='Modelo 1o grau')
    plt.xlabel("Instante medido(s)")
    plt.ylabel("Posição medida(m)")
    plt.legend(loc='best')

















