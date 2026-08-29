# Conversor de unidades
# Exercicio de logica de programacao
# Converte comprimento, peso e temperatura

while True:
    print("\n----- CONVERSOR DE UNIDADES -----")
    print("1 - Comprimento (km, m, cm)")
    print("2 - Peso (kg, g)")
    print("3 - Temperatura (C, F)")
    print("4 - Sair")

    opcao = input("Escolhe uma opcao: ")

    if opcao == "4":
        print("tchau")
        break

    elif opcao == "1":
        valor = float(input("Valor em km: ").replace(",", "."))
        print(str(valor) + " km = " + str(valor * 1000) + " m")
        print(str(valor) + " km = " + str(valor * 100000) + " cm")

    elif opcao == "2":
        valor = float(input("Valor em kg: ").replace(",", "."))
        print(str(valor) + " kg = " + str(valor * 1000) + " g")

    elif opcao == "3":
        valor = float(input("Valor em Celsius: ").replace(",", "."))
        fahrenheit = valor * 9 / 5 + 32
        print(str(valor) + " C = " + str(fahrenheit) + " F")

    else:
        print("opcao invalida")
