# Jogo da Forca
# Exercicio de logica de programacao

import random

palavras = ["python", "programacao", "computador", "algoritmo", "teclado", "internet", "software"]

palavra = random.choice(palavras)
letras_certas = []
letras_erradas = []
tentativas = 6

print("----- JOGO DA FORCA -----")

while tentativas > 0:
    # mostra a palavra com _ nas letras que faltam
    mostrar = ""
    for letra in palavra:
        if letra in letras_certas:
            mostrar = mostrar + letra + " "
        else:
            mostrar = mostrar + "_ "
    print("\nPalavra: " + mostrar)
    print("Letras erradas: " + str(letras_erradas))
    print("Tentativas restantes: " + str(tentativas))

    if "_" not in mostrar:
        print("\nVoce ganhou! A palavra era " + palavra)
        break

    chute = input("Chuta uma letra: ").lower()

    if len(chute) != 1:
        print("digita só uma letra")
        continue

    if chute in palavra:
        if chute not in letras_certas:
            letras_certas.append(chute)
            print("acertou!")
        else:
            print("voce ja tentou essa")
    else:
        if chute not in letras_erradas:
            letras_erradas.append(chute)
            tentativas = tentativas - 1
            print("errou")
        else:
            print("voce ja tentou essa")

if tentativas == 0:
    print("\nVoce perdeu! A palavra era: " + palavra)
