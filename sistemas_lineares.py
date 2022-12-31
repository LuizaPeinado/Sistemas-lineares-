'''
importamos a biblioteca NUMPY, desenvolvida para solucionar problemas matemáticos,
resuzindo a quantidade de linhas e deixando o código mais limpo e eficiente

O código atende sistemas de infinitas incógtas.

'''
import numpy as np 


#Declaramos as coeficientes das equações dentro da Array.
A = np.array([[7,3], [15,-2]])
#Declaramos os resultados das equações dentro da Array.
B = np.array([[23],[24]])

# Contamos a quantidade de incogtas dentro da matriz A e comparamos com a quantidade 
# de resultados dentro da Matriz B, assim, se os valores forem iguais, a matriz será quadrada.
# O contrário disso significa que a matriz não é quadrada,logo, não funcionará no código.

for lista in (A):
    coeficientes = len(lista)
    break

resultados = 0

for valor in (B):
    resultados += 1
    
if coeficientes != resultados:
    print('O sistema deve ser quadrado')
    print('****************************')
    print("\n\n\n\n")
    
# Depois de verificar a condição de a Matriz ser quadrada, verificamos o valor do determinante, 
# e se for igual a 0, a matriz será impossível e indeterminada. O contrário significa que a matriz é 
#possível e determinada.

determinante = np.linalg.det(A)

if determinante != 0:
    
    #Encontramos a inversa da Matriz A (A matriz que contém os coeficientes)
    A_inversa = np.linalg.inv(A)
    
    '''
    Encontramos a Matriz com os coeficientes em ordem respectiva usando a
    propriedaade de matrizes em que o inverso da Matriz A multiplicado pela 
    matriz B é igual a matriz que contém as incogtas
    
    '''
    incogtas = np.dot(A_inversa, B)
    
    print('****************************************')
    print('A MATRIZ DIGITADA COM OS COEFICIENTES É:')
    print(A)
    print('****************************************')
    print('A MATRIZ DIGITADA COM AS RESPOSTAS É: ')
    print(B)
    print('****************************************')
    print('AS INCOGTAS EM ORDEM RESPECTIVA SÃO: ')
    print(incogtas)
    
else:
    print('O SISTEMA É IMPOSSÍVEL OU INDETERMINADO')
