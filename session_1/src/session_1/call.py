var1 = int(input("Primeiro numero: "))
var2 = int(input("Segundo numero: "))

op = int(input("Escolha a operação (1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão): "))

def teste(op):
    if op == 1:
        resultado = var1 + var2
        return resultado
    elif op == 2:
        resultado = var1 - var2
        return resultado
    elif op == 3:
        resultado = var1 * var2
        return resultado
    elif op == 4:
        if var2 != 0:  
            resultado = var1 / var2
            return resultado
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida"

print(teste(op))
