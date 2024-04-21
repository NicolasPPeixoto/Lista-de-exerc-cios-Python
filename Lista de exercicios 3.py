import random

# 26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando 
# na tela uma das mensagens abaixo:
#  - O primeiro valor é o maior
#  - O segundo valor é o maior
# #  - Não existe valor maior, os dois são iguais


numero = int(input("Digite um número: "))
numero1 = int(input("Digite um número: "))

if numero > numero1:
    print("O primeiro valor é maior")
elif numero1 > numero:
    print("O segundo valor é maior")
else: print("Não existe valor maior, os dois são iguais")

# 27) Crie um programa que leia duas notas de um aluno e calcule a sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média até 4.9: REPROVADO
#  - Média entre 5.0 e 6.9: RECUPERAÇÃO
#  - Média 7.0 ou superior: APROVADO

nota = input("Qual sua nota? ")
nota2 = input("Qual a sua outra nota? ")

média = (float(nota) + float(nota2))

print("Sua média é "+str(média))

if média <= 4.9:
    print("REPROVADO")
elif média < 6.9:
    print("RECUPERAÇÃO")
else: print("APROVADO")

# 28) Faça um programa que leia a largura e o comprimento de um terreno 
# retangular, calculando e mostrando a sua área em m². O programa também 
# devemostrar a classificação desse terreno, de acordo com a lista abaixo:
#  - Abaixo de 100m² = TERRENO POPULAR
#  - Entre 100m² e 500m² = TERRENO MASTER
#  - Acima de 500m² = TERRENO VIP

larg = int(input("Qual a largura do terreno? "))
compri = int(input("Qual o comprimento do terreno? "))

area = larg*compri

print ("A área do terreno é de", str(area),"m²") 

if area <= 100:
    print("TERRENO POPULAR")
elif area < 500:
    print("TERRENO MASTER")
else: print("TERRENO VIP")

# 29) Desenvolva um programa que leia o nome de um funcionário, seu salário, 
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de 
# acordo com a tabela a seguir:
#  - Até 3 anos de empresa: aumento de 3%
#  - entre 3 e 10 anos: aumento de 12.5%
#  - 10 anos ou mais: aumento de 20%

nome = input("Qual é seu nome? ")
salário = float(input("Qual é seu salário? "))
anos = int(input("Há quantos anos você trabalha nesta empresa? "))


if anos <= 3:
    novo = (salário*0.3)+salário
    print(nome,"você recebeu um aumento de 3%, seu novo salário será de",novo)
elif anos <10:
    novo = (salário*0.12*0.05)+salário
    print(nome,"você recebeu um aumento de 12.5%, seu novo salário será de",novo)
elif anos >=10:
    novo = (salário*0.20)+salário 
    print(nome,"você recebeu um aumento de 20%, seu novo salário será de",novo)

# 30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo 
# de triângulo será formado: 
#  - EQUILÁTERO: todos os lados iguais
#  - ISÓSCELES: dois lados iguais
#  - ESCALENO: todos os lados diferentes

a = float(input("Digite uma medida: "))
b = float(input("Digite outra medida: "))
c = float(input("Digite outra medida: "))

if a < b + c and b < a + c and c < b + a:
    print("É possível formar um triângulo")
    if a == b and b == c:
        print("Este triângulo é equilátero")
    elif (a == b and c != a) or (b == c and a!= b) or (a == c and b != a):
        print("Este triângulo é isósceles")
    else: print("Este triângulo é escaleno")
else:
    print("Não é possível formar um triângulo")

# 31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

jogador = int(input("Escolha pedra(1) papel(2) ou tesoura(3):"))

maquina = random.randint(1,3)

print(maquina)

if (jogador == 2 and maquina == 1) or (jogador == 1 and maquina == 3) or (jogador == 3 and maquina == 2):
    print("Jogador ganhou!")
elif jogador == maquina:
    print("Empate")
else: print("Máquina ganhou")

# 32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o 
# jogador vai tentar descobrir qual foi o valor sorteado

jogador = int(input("Tente adivinhar o número de 1 a 5: "))

maquina = random.randint(1,5)

print(maquina)

if maquina == jogador:
    print("Jogador ganhou!")
else: print("Máquina ganhou!")

# # # # 33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra 
# # # # de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e 
# # # # em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que 
# # # # ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = int(input("Qual o valor da casa? "))
salario = float(input("Qual seu salario? "))
anos = float(input("Em quantos anos você deseja pagar a sua casa? "))

prestacao = valor/(anos*12)

if prestacao < salario*0.3:
    print("Empréstimo aceito")
else: print("Empréstimo negado")

# # 34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no 
# # peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o 
# # indivíduo dentro de certas faixas.

peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

imc = peso/(altura*altura)

if imc < 18.5:
    print("Abaixo do peso") 
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else: print("Obesidade mórbida")

# 35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O 
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para 
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e 
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a 
# tabela a seguir:

carro = input("Qual o tipo de carro alugado, popular ou luxo? ")
dias = float(input("Por quantos dias o carro será alugado? "))
km = float(input("Quantos quilômetros você irá andar com o carro?  "))

aluguel = carro 

if aluguel == "popular" and km <= 100 :
    preço = dias * 90+ km * 0.2
elif aluguel == "popular" and km >= 100:
    preço = dias * 90 + km * 0.1
elif aluguel == "luxo" and km <= 200:
    preço = dias * 150 + km * 0.3
else: preço = dias * 150 + km * 0.25

print("O preço a ser pago é de",preço,"reais")

# 36) Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, 
# calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

horas = float(input("Quantas horas de atividade você fez nesse mês? "))

if horas <= 10:
    pontos = 2*horas
elif horas <= 20:
    pontos = 5*horas
else: pontos = 10*horas

dinheiro = pontos*0.05

print("Você obteve",pontos,"pontos, logo vai receber: R$"+str(dinheiro))

# 37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um 
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, 
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. 
# No final, mostre o seu novo salário, baseado na tabela a seguir:

anos = int(input("Há quantos anos você trabalha nesta empresa? "))
salário = float(input("Qual é seu salário? "))
sexo = input("Qual o seu sexo (M ou F)? ")

if sexo.upper() == "F":
    if anos < 15:
        aumento = salário*1.05
    elif anos < 20:
        aumento = salário*1.12
    else: aumento = salário*1.23
else:
    if anos < 20:
        aumento = salário*1.03
    elif anos < 30:
        aumento = salário*1.13
    else: aumento = salário*1.25

arredondado = round(aumento, 2)

print("Seu novo salário é de: R$"+str(arredondado))