#Exercício 18:
#Escreva uma função que tem o valor True se o seu
#argumento for 5 e False no caso contrario

def valida5(valor):

    if valor==5:
        return True
    return False

valor = int(input("introduza um valor"))
resultado = valida5(valor)
print(resultado)
