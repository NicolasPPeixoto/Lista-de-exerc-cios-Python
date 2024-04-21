# 64) Desenvolva um programa usando a estrutura “para” que mostre na tela a 
# seguinte contagem:

# 0 5 10 15 20 25 30 35 40 Acabou!

for i in range (0,41,5):

    print(i)

print("Acabou!")


# 65) Desenvolva um programa usando a estrutura “para” que mostre na tela a 
# seguinte contagem:
# 100 90 80 70 60 50 40 30 20 10 0 Acabou!

seq = []

for i in range (100, -1, -10):

    print(i)

print("acabou!")

# 66) Escreva um programa que leia um número qualquer e mostre a tabuada desse 
# número, usando a estrutura “para”.
# Ex: Digite um valor: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 ...

for i in range(2):
    num = input("Digite um número:")
    print("5 x "+num+" = "+str(int(num)*5))

# 67) Faça um programa usando a estrutura “para” que leia um número inteiro 
# positivo e mostre na tela uma contagem de 0 até o valor digitado:
# Ex: Digite um valor: 9
# Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM!

num = int(input("Digite um número inteiro: "))

for i in range (0, num+1):
    print(i)

print("Acabou!")

# 68) Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura 
# “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres 
# d) O maior peso entre os homens

pesomulher = 0
mulher = 0
homempeso = 0
homempesomaior = 0
mediamulher = 0

for i in range (3):

    sexo = input("Digite seu sexo (M ou F): ")
    peso = int(input("Digite seu peso: "))

    if sexo.upper() == "F":
        mulher += 1
        pesomulher += peso
    
    
    if sexo.upper() == "M" and peso >= 100 :
        homempeso += 1 

    if sexo.upper() == "M" and peso>homempesomaior :
        homempesomaior = peso
        
if mulher >= 1:  
    mediamulher = pesomulher/mulher

print("O maior peso entre os homens é de",str(homempesomaior)+"kg")
print("A média de peso entre as mulheres é de",str(mediamulher)+"kg")
print("O número de mulheres cadastradas é",mulher)
print("O número de homens que pesam mais de 100kg é",homempeso)

# 69) [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma 
# PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e 
# a soma entre todos os valores da sequência.

termo = int(input("Qual é o termo? "))
razao = int(input("Qual a razão? "))
soma = 0

for i in range(termo, 10):

    print(termo)

    soma += termo

    termo = razao + termo

print("A soma de todos os valores é",soma)
    

# 70) [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência 
# de Fibonacci:
# 1 1 2 3 5 8 13 21...

num = 1
lastnum = 0

for i in range(1, 16, ):

    novonum = lastnum + num

    print(novonum)

    lastnum = num

    num = novonum


# guardar ultimo numero
# somar o ultimo numero com o numero atual