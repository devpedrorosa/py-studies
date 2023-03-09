import math
import time
#while true usado para criar loop
while True:
    # Solicita a operação desejada e os valores numéricos
    operacao = input("Digite a operação desejada (+, -, *, /, sqrt) ou digite sair: ")
    
    if operacao == "sair":
        break
    #break é quebrar o loop quando determinada palavra for digitada

    #if é para criar uma situação, nesse caso como a raiz quadrada so pode ser de um numero ent eu criei uma situação que se a operação for raiz ent ele so vai pedir um número
    if operacao == "sqrt":
        valor = float(input("Digite o valor numérico: "))
        #caso a operação seja qualquer outra q n seja raiz quadrada entao ele vai pedir para digitar dois numeros
    else:
        valor1 = float(input("Digite o primeiro valor numérico: "))
        valor2 = float(input("Digite o segundo valor numérico: "))
        
    
    # começa de novo usando o if para as operação, "if" é so pra iniciar a sequencia de quantos casos vc quer ter ai começa com if e termina com elif ou else 
    # Executa a operação desejada
    if operacao == "+":
        resultado = valor1 + valor2
    elif operacao == "-":
        resultado = valor1 - valor2
    elif operacao == "*":
        resultado = valor1 * valor2
    elif operacao == "/":
        resultado = valor1 / valor2
    elif operacao == "sqrt":
        resultado = math.sqrt(valor)
        #caso o usuario digite outra opção que nao esteja na lista, o programa vai dizer que a operação é invalida e vai retonar o programa se usar o continue
    else:
        print("Operação inválida!")
        continue

    # Exibe o resultado da operação
    print("Resultado: {}".format(resultado))