print("### CALCULADORA PYTHON ###")

def adicao(num1, num2):
    soma = num1 + num2
    return soma

print("Resultado da soma:", adicao(16, 9))

def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

print("Resultado da subtracao:", subtracao(89,33))

def multiplicacao (num1, num2):
    resultado = num1 * num2
    return resultado

print("resultado da multiplicação:", multiplicacao(6, 8))

def divisao(num1, num2):
    if num2 != 0:
        resultado = num1 / num2
        return resultado
    else:
        return"Não é possível dividir por zero"