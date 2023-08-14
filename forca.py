palavra = "flex-das-estrelas"
letras = []
chances = 5
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances.")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras:
            ganhou = False
        
    if chances == 0 or ganhou:
            break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")
else:
    print(f"Você perdeu. A palavra era: {palavra}")