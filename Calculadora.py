def somar(a1,a2):
    resultado = a1 + a2
    print(resultado)
    return(resultado)
def subtrair(a1,a2):
    resultado = a1 - a2
    print(resultado)
    return(resultado)
def multiplicar(a1,a2):
    resultado = a1 * a2
    print(resultado)
    return(resultado)
def dividir(a1,a2):
    resultado = a1 / a2
    print(resultado)
    return(resultado)

print(f'Seja bem vindo a sua nova calculadora, por favor digite dois números')
a1 = int(input('Primeiro Número '))
a2 = int(input('Segundo Número '))
var = input('Agora digite a operação a ser realizada{somar,subtrair,multiplicar ou dividir}')
if var.lower()=='somar':
    somar(a1,a2)
if var.lower()=='subtrair':
    somar(a1,a2)
if var.lower()=='multiplicar':
    somar(a1,a2)
if var.lower()=='dividir':
    somar(a1,a2)