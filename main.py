import numpy as np

#intervalo [0,1)
print(np.random.randint(2))
print('***********')
#intervalo [0,1), ou seja, só pode dar zero!
print(np.random.randint(1))
print('***********')
#intervalo [0, 10]
print (np.random.randint(0,11))
print('***********')
#intervalo [2, 4]
print(np.random.randint(2, 5))
print('***********')
#array de 10 posições
#intervalo [1, 10]
print (np.random.randint(1, 11, 10))
print('***********')
#matriz 2x3, use uma tupla!
#intervalo [1,5]
print (np.random.randint(1, 6, (2,3)))


#semelhante à função rand
#só muda a distribuição
# print (np.random.randn(2,5))

#
# #um único valor no intervalo [0,1)
# print(np.random.rand())
# print('***********')
# #um array com um único valor no intervalo [0,1)
# print(np.random.rand(1))
# print('***********')
# #vetor de 10 valores no intervalo [0,1)
# print (np.random.rand(10))
# print('***********')
# #matriz, duas linhas, 4 colunas
# #intervalo [0,1)
# #recebe os números de fato e não uma tupla que os contém
# print (np.random.rand(2, 4))


# np.random
# #diagonal secundária repleta de uns
# print (np.flipud(np.eye(3, 3)))
# print('***********')
# #desloca para a direita uma vez
# print (np.flipud(np.eye(3, 3, 1)))
# print('***********')
# #desloca para a direita duas vezes
# print (np.flipud(np.eye(3, 3, 2)))
# print('***********')
# #desloca para a esquerda uma vez
# print (np.flipud(np.eye(3, 3, -1)))


# print (np.eye(5, 5, -1))
# print('***********')
# print (np.eye(5, 5, -2))
# print('***********')
# print (np.eye(5, 5, -3))


# print(np.eye(5, 5, -1))


# # 0 = diagonal "principal"
# print (np.eye(3, 5, 0))
# print('***********')
# #1 = desloca para a "próxima diagonal"
# print (np.eye(3, 5, 1))
# print('***********')
# #2 = desloca duas vezes
# print (np.eye(3, 5, 2))
# print('***********')
# #5 = deslocou demais
# print (np.eye(3, 5, 5))

# # matriz quadrada de ordem 3, tal qual identity
# #N=M=3
# print (np.eye(3))
# print ('*******')
# #4 linhas, 5 colunas
# print(np.eye(4, 5))
# print ('*******')
# #2 linhas, 5 colunas
# print(np.eye(2, 5))




# #matriz identidade de ordem 4
# print (np.identity(4))
# print ('*******')
# #matriz identidade de ordem 5
# print (np.identity(5))

# print (np.linspace(5, 5, 10))
# print ('*******')
# print (np.linspace(5, 1, 11))
# print ('*******')


# #cinco números no intervalo de 0 a 10
# #intervalo fechado: inclui os dois extremos
# print(np.linspace(0, 10, 5))
# print ('*******')
# #dois números no intervalo de 1 a 5
# print (np.linspace(1, 5, 2))
# print ('*******')
# #10 números no intervalo de 1 a 20
# print (np.linspace(1, 20, 10))
# print ('*******')
# #e agora?
# #padrão: 50
# print (np.linspace(1, 2))
# print (np.linspace(1, 0))
# #uma dimensão
# print (np.ones(10))
# print ('*********')
# #duas dimensões. 3 linhas, 4 colunas
# # lembre-se sempre de passar uma tupla: (3, 4)
# print (np.ones((3, 4)))

# print (np.zeros((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)))
# #três dimensões
# print (np.zeros([2, 4, 2]))
# print ('*********')
# print (np.zeros([3, 3, 3]))
# #quatro dimensões
# # print (np.zeros([2, 3, 4, 3]))

# #uma dimensão, 10 zeros
# print(np.zeros(10))
# print('******')
# #duas dimensões de 6 zeros cada
# #recebe uma tupla!
# print(np.zeros((6,6)))
# print('******')
# #duas dimensões: 3 linhas, 5 colunas
# varios_zeros = np.zeros(5)
# de_zero_a_dois = np.arange(3)
# de_dois_a_seis = np.arange(2, 6)
# dois_a_onze_de_tres_em_tres = np.arange(2, 12, 3)
# print (de_zero_a_dois)
# print (de_dois_a_seis)
# print (dois_a_onze_de_tres_em_tres)

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print (type(matriz))
# array_duas_dimensoes = np.array(matriz)
# print (type (array_duas_dimensoes))

# lista = [1, 2, 3, 4, 5, 6]
# print (type(lista))
# array = np.array(lista)
# print (type(array))
# print (type(lista))

# print (np.array([1, 2]))

