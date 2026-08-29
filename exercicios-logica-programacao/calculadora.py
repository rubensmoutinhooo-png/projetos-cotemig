# Calculadora simples
# Exercicio de logica de programacao

import math

while True:
    print("\n----- CALCULADORA -----")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Potencia")
    print("6 - Raiz quadrada")
    print("7 - Sair")

    opcao = input("Escolhe uma opcao: ")

    if opcao == "7":
        print("tchau")
        break

    if opcao == "6":
        num = float(input("Numero: ").replace(",", "."))
        if num < 0:
            print("nao da pra tirar raiz de numero negativo")
        else:
            print("Resultado: " + str(math.sqrt(num)))
        continue

    if opcao in ["1", "2", "3", "4", "5"]:
        n1 = float(input("Primeiro numero: ").replace(",", "."))
        n2 = float(input("Segundo numero: ").replace(",", "."))

        if opcao == "1":
            resultado = n1 + n2
        elif opcao == "2":
            resultado = n1 - n2
        elif opcao == "3":
            resultado = n1 * n2
        elif opcao == "4":
            if n2 == 0:
                print("nao da pra dividir por zero")
                continue
            resultado = n1 / n2
        elif opcao == "5":
            resultado = n1 ** n2

        print("Resultado: " + str(resultado))
    else:
        print("opcao invalida")
