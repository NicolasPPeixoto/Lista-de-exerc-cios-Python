import random

# 38) Escreva um programa que mostre na tela a seguinte contagem: 
# 6 7 8 9 10 11 Acabou!

print("6\n7\n8\n9\n10\n11\nAcabou!")

# 39) Faça um algoritmo que mostre na tela a seguinte contagem:
# 10 9 8 7 6 5 4 3 Acabou!

contagem = 10
while contagem >= 3:
    print(contagem)
    contagem = contagem - 1
print("Acabou!")

# 40) Crie um aplicativo que mostre na tela a seguinte contagem:
# 0 3 6 9 12 15 18 Acabou!

contagem = 0
while contagem <= 18:
    print(contagem)
    contagem = contagem + 3
print("Acabou!")

# 41) Desenvolva um programa que mostre na tela a seguinte contagem:
# 100 95 90 85 80 ... 0 Acabou!

contagem = 100
while contagem >= 0:
    print(contagem)
    contagem = contagem - 5
print("Acabou!")

# 42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo 
# qualquer e mostre uma contagem até esse valor:
# Ex: Digite um valor: 35
# Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

contagem = int(input("Digite um número inteiro e positivo:"))

while contagem >= 0:
    print(contagem)
    contagem = contagem - 1
print("Acabou!")

# 43) Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1, 
# marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
# 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...

contagem = 30 


while contagem >= 0:
    if contagem %4 == 0:
        print("["+str(contagem)+"]")
    else: 
        print(contagem)

    contagem -= 1

print("Acabou!")


# 44) Crie um algoritmo que leia o valor inicial da contagem, o valor final e o 
# incremento, mostrando em seguida todos os valores no intervalo:

# Ex: Digite o primeiro Valor: 3
# Digite o último Valor: 10
# Digite o incremento: 2
# Contagem: 3 5 7 9 Acabou!

primeiro = int(input("Digite o valor inicial: "))
ultimo = int(input("Digite o valor final: "))
incremento = int(input("Digite o incremento: "))


while primeiro <= ultimo:
    print(primeiro)
    primeiro = primeiro + incremento
print("Acabou!")

# 45) O programa acima vai ter um problema quando digitarmos o primeiro valor 
# maior que o último. Resolva esse problema com um código que funcione em qualquer 
# situação.

primeiro = int(input("Digite o valor inicial: "))
ultimo = int(input("Digite o valor final: "))
incremento = int(input("Digite o incremento: "))


if primeiro < ultimo:
   while primeiro <= ultimo:
    print(primeiro)
    primeiro = primeiro + incremento
else: 
     while primeiro >= ultimo:
        print(ultimo)
        ultimo = ultimo + incremento

print("Acabou!")

# 46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 
# 8 + 10 + 12 + 14 + ... + 98 + 100.
    
soma = 0

for num in range(6,101):
    if num %2 == 0:
        soma = soma + num
        
print(soma)

# 47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 
# 450 + 400 + 350 + 300 + ... + 50 + 0

soma = 0

for num in range(0,501):
    if num %5 == 0:
        soma = soma + num

print(soma)

# 48) Faça um programa que leia 7 números inteiros e no final mostre o somatório 
# entre eles.

soma = 0 

for num in range(0, 7):
    numeros = int(input("Digite um número: "))
    soma = numeros + soma

print(soma)

# 49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles 
# são pares e quantos são ímpares.

par = 0
ímpar = 0

for num in range(0, 6):
    numeros = int(input("Digite um número: "))
    if numeros %2 == 0:
        par = par + 1
    elif numeros %2 == 1:
        ímpar = ímpar + 1
    
print(ímpar,"números são ímpares.\n"+str(par),"números são pares.")

# 50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e 
# mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3

import random

sorteio = []
maior= 0 
divisivel = 0 



for num in range(20): 

    numeros = random.randint(0, 10)

    sorteio.append(numeros)

    if numeros > 5:
        maior +=  1
  
    if numeros == 0:
        divisivel = divisivel
    elif numeros %3 == 0:
        divisivel += 1
    
print(sorteio)

print(divisivel)

print(maior)   

# 51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela 
# qual foi o maior e qual foi o menor preço digitados.

produtos = []
maior = 0
menor = 1

for produto in range(0,4) :
    produto = int(input("Digite uma produtos: "))

    produtos.append(produto)

    if produto > maior:
        maior = produto
        
    if produto < menor:
        menor = produto


print(maior,menor)

#  52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida  

idades = []
menor = 0
maior = 0
maioridade = 0
soma = 0 

for idade in range(0,5) :
    idade = int(input("Digite uma idade: "))

    idades.append(idade)

    soma += idade
    
    if idade >= 18:
        maior += 1

    if idade < 5 :
        menor += 1

    if idade > maioridade:
        maioridade = idade

media = soma /10

print("\nHá",menor,"pessoas menores de 5 anos e", maior,"pessoas maiores de 18 anos" )
print("\nA maior idade é de", maioridade)
print("\nA média de idades neste grupo é de",media)

# 53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens    
# e) Quantas mulheres tem mais de 20 anos

idade = 0
media_ = 0
media = 0
soma = 0
homem = 0
mulheres = 0
M = 0

for i in range(5):
    
    sexo = input("Qual o seu sexo (M ou F)? ")
    idade = int(input("Qual é sua idade? "))

    soma += idade

    if sexo.upper() == "F":
        mulheres += 1
        if idade > 20:
            M += 1
    else: 
        homem += 1
        media_ += idade
    
    
media = soma /5  
media_h = media_ /homem

print("Foram cadastrados",homem,"homens")
print("Foram cadastradas",mulheres,"mulheres")
print("Este é o número de mulheres acima de 20 anos:",M)
print("A média de idade entre estas pessoas é de",media,"anos")
print("A média de idade entre homens é de",media_h,"anos")


# 54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando 
# no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

soma = 0
pesado = 0
messi = 0
taquara = 0

for i in range(7):

    peso = float(input("Qual o seu peso? "))
    altura = float(input("Qual a sua altura? "))

    soma += altura

    if peso > 90:
        pesado += 1
    elif peso < 50 and altura < 1.60:
        messi += 1
        
    if altura > 1.90 and peso > 100:
        taquara += 1

media = round(soma /7, 2)

print("Há",pesado,"pessoas que pesam mais de 90kg")
print("Há",messi,"pessoas que pesam menos de 50kg e menos de 1.60m")
print("Há",taquara,"pessoas que medem mais de 1.90 e pesam mais de 100kg")
print("A média de altura deste grupo de pessoas é de:",media)


# 55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de 
# agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4 
# tentativas para tentar acertar.

for i in range (4):

    jogador = int(input("Tente adivinhar o número de 1 a 10: "))

maquina = random.randint(1,11)

print("O número sorteado era",maquina)

if maquina == jogador:
    print("Jogador ganhou!")
else: print("Máquina ganhou!")