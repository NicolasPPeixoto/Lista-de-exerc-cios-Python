# 56) Crie um programa que leia vários números pelo teclado e mostre no final o 
# somatório entre eles.

flag = True

num = 0
numero = num 

while flag: 

    for i in range (4):
        num = int(input("Digite um número: "))
         
        if num == 1111:
            flag = False
            numero = "erro"
        else:
            numero += num
        
    
    flag = False
   
if numero == "erro":
    print("error 404")
else:
    print("A soma dos números é:",numero)

# 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. 
# No final, mostre o total de salários pagos aos homens e o total pago às 
# mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não 
# sempre que ler os dados de um funcionário.

flag = True

salarios_F = 0
salarios_M = 0

while flag:


        
        salario = int(input("Digite o salário: "))
        sexo = input("Digite o sexo(M ou F):  ")

        continuar = input("Você quer continuar(S ou N)?: ")

        if continuar.upper() == "N":
                flag = False    

        if sexo.upper() == "F":
                salarios_F += salario 
        else:
                salarios_M += salario
                
       
print("Este é o total dos salários dos homens R$",salarios_M)
print("ESte é o total dos salários das mulheres R$",salarios_F)

# 58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa 
# vai parar quando for digitada a idade 999. No final, mostre quantos alunos 
# existem na turma e qual é a média de idade do grupo.

idades =[]
continuar = True 

while continuar:
        idade  = int(input("Digite a idade: "))

        if idade == 999:
                continuar = False
                continue
        
        idades.append(idade)

print("Há",len(idades),"alunos na turma, e a média de idades é de",sum(idades) / len(idades),"anos")

# 60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. 
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

pessoas = []
continuar = True
maior = 0
menor = 1000
media = 0
mulher_menor = 0
homem_maior = 0

while continuar:

        nome = input("Qual é seu nome? ")
        idade = int(input("Qual é sua idade? "))
        sexo = input("Qual é seu sexo? (M ou F) ")

        pessoa = [nome, idade, sexo.upper()]

        pessoas.append(pessoa)

        seguir = input("Você quer continuar(S ou N)?: ")

        if seguir.upper() == "N":
                continuar = False
        
for pessoa in pessoas:

        if  int(pessoa[1]) > maior:
                maior = pessoa[1]

        if pessoa[2] == "F":
                if int(pessoa[1]) < menor:
                        menor = pessoa[1]
                if int(pessoa[1]) < 18:
                        mulher_menor += 1
        else:
                if int(pessoa[1]) > 30:
                        homem_maior += 1

        media += pessoa[1]
                
medias = media / len(pessoas)


print("A mulher mais jovem tem",menor,"anos")
print("O homem mais velho",maior,"anos")
print("Há",mulher_menor,"mulheres com menos de 18 anos e",homem_maior,"homens com mais de 30 anos") 
print("A média de idade neste grupo é de",round(medias, 2),"anos")
        