def calcular(x, y, op=1):
    if(op == 1):
        print("a soma é:", x + y)
    elif(op == 2):
        print("o resto é: ", x - y)
    elif(op == 3):
        print("o produto é: ", x * y)
    elif(op == 4):
        print("o quociente é: ", x / y)
    elif(op == 5):
        print("o resto da divisão é: ", x % y)
    elif(op == 6):
        print("a potência é: ", x ** y)


x = int(input("digite o numero:"))
y = int(input("digite outro numero:"))
print("OPERAÇÔES")
print("1 adição")
print("2 subtração")
print("3 multiplicação")
print("4 divisão")
print("5 restto da divisão")
print("6 potência")
op = int(input("escolha a operação"))
calcular(x, y, op)

# Visto 29/05 - Prof. Parisotto
