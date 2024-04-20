# 1) Escreva um programa que mostre na tela a mensagem "Olá, Mundo!"

print("\nOlá, Mundo!\n")

# 2) Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-
# vindas para ela:

nome = input("Qual é seu nome? ")

print("\nOlá "+ nome+", é um prazer te conhecer!\n")

# 3) Crie um programa que leia o nome e o salário de um funcionário, mostrando no 
# final uma mensagem.

nome = input("Qual é seu nome? ")
salário = input("Qual é seu salário? ")

print("\nNome do Funcionário: "+ nome +"\nSalário: "+ str(salário)+"\n")

# 4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório 
# entre eles.

numero = input("digite um número: \n")
numero2 = input("\ndigite outro número: \n")

print ("\nO número "+str(numero)+" somado com " +str(numero2)+ " é igual a " + str(int(numero)+int(numero2))+"\n")

# 5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre 
# na tela a sua média na disciplina.

nota1 = input("Qual a sua nota? ")
nota2 = input("Qual a sua outra nota? ")

média = (int(nota1) + int(nota2))/2

print("\nNota 1 "+str(nota1)+"\nNota 2 "+str(nota2)+"\n\nA média entre "+str(nota1) +" e "+str(nota2) +" é "+str(média)+"\n")

# 6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu 
# sucessor.

numero = input("digite um número: \n")

antecessor = int(numero) -1
sucessor = int(numero) +1

print("\nO antecessor de "+ str(numero) +" é "+ str(antecessor) +" e seu sucessor é "+ str(sucessor)+"\n")

# 7) Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a 
# sua terça parte.

numero = input("digite um número: \n")

dobro = int(numero)*2
tercaparte = int(numero)/3

print("\nO dobro de "+str(numero)+" é "+str(dobro)+"\n\nA terça parte de "+str(numero)+" é "+str(tercaparte)+"\n")

# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores 
# relativos em outras medidas.

m = input("Digite uma distância em metros ")

km = int(m) / 1000
hm = km * 10
dam = hm * 10
dm = int(m) * 10
cm = dm * 10
mm = cm * 10

print("\nA distância "+ m +" corresponde a:\n\n"+str(km)+"Km\n"+str(hm)+"Hm\n"+str(dam)+"Dam\n"+str(dm)+"dm\n"+str(cm)+"cm\n"+str(mm)+"mm\n")