# 17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba 
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade = input("Qual a velocidade do carro? ")

if int(velocidade) > 80:
    multa = (int(velocidade)-80)*5
    print("Velocidade excedida. \nMulta: R$"+str(multa))

# 18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade 
# dela e depois mostre se ela pode ou não votar.
    
nascimento = input("Em que ano você nasceu? ")

idade = 2023 - int(nascimento)

if idade > 150:
    print("Você deve estar morto, mas pode votar")
elif idade < 16: 
    print("Você não pode votar")
elif idade > 16:
    print("Você pode votar")
else: print("Você pode votar") 

# 19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua 
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou 
# não um bom aproveitamento (se ficou acima da média 7.0).

nome = input("Qual é seu nome? ")
nota = input("Qual sua nota? ")
nota2 = input("Qual a sua outra nota? ")

média = (int(nota) + int(nota2))/2

print("Sua média é "+str(média))

if média > 7:
    print(nome+" obteve um bom aproveitamento")
elif média < 7:
    print(nome+" não obteve um bom aproveitamento")
else: print(nome+" obteve um bom aproveitamento")

# 20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou 
# ÍMPAR.

numero = input("digite um número: \n")

if int(numero)%2 >0 :
    print("Ímpar")
else: print("Par")

# 21) Faça um algoritmo que leia um determinado ano e mostre se ele é ou não 
# BISSEXTO.

ano = input("Digite um ano: ")

if int(ano) %4 > 0:
    print("Ano não bissexto")
else: print("Ano bissexto")

# 22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua 
# situação em relação ao alistamento militar.
    
ano = input("Em que ano você nasceu? ")

idade = 2023 - int(ano) 
alistamento = idade -18 


if idade < 18:
    print("Daqui a "+str(-alistamento)+" anos você terá que se alistar")
elif idade > 18:
    print("Você deveria ter se alistado há "+str(alistamento)+" anos")
else: 
    print("Você deve se alistar neste ano")

# 23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos 
# para todos, mas especialmente para mulheres. Faça um programa que leia nome, 
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo 
# que:
    
nome = input("Qual seu nome? ")
sexo = input("Qual o seu sexo (M ou F)? ")
valor = float(input("Qual o valor das suas compras? "))

homem = valor *0.95
mulher = valor * 0.87

if sexo.upper == "M":
    print("Nome:", nome, "\nO valor de suas compras foram de", homem)
else: 
    print("Nome:", nome, "\nO valor de suas compras foram de", mulher)

# 24) Faça um algoritmo que pergunte a distância que um passageiro deseja 
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para 
# viagens até 200Km e R$0.45 para viagens mais longas.
    
distância = float(input("Qual distância você deseja percorrer em Km? "))

if distância > 200:
    km = distância *0.45
else: km = distância *0.50

print("O valor da passagem é de",km,"reais")

# 25) [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. 
# Analise seus comprimentos e diga se é possível formar um triângulo com essas 
# retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento 
# de cada lado deve ser menor que a soma dos outros dois.

a = float(input("Digite uma medida: "))
b = float(input("Digite outra medida: "))
c = float(input("Digite outra medida: "))

if a < b + c and b < a + c and c < b + a:
    print("É possível formar um triângulo")
else:
    print("Não é possível formar um triângulo")

