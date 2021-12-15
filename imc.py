nome = input("Qual Seu Nome? ")

idade  = int(input("Qual sua idade ? "))    # ex: 34, 33, 21
peso   = float(input("Qual seu peso ? "))   # ex: 45, 99, 78.4, 99.200
altura = float(input("Qual sua Altura ? ")) # ex: 1.89, 1.99
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e seu Imc e de {imc:.2f}.')
