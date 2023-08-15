## Jogo da forca ##
import random
palavras = ["flex-das-estrelas", "nidalee", "vayne", "ezreal", "thresh"]
palavra = random.choice(palavras)
letras = []
chances = 5
ganhou = False

print("Bem vindo ao jogo da forca")
print("Você terá que acertar a palavra")
print("Terá que arriscar uma letra por vez")
print("Tendo 5 chances, caso você acerte mostrará a letra, se errar perde uma chance")
print("As chances estarão visíveis no jogo")
print("Todas as palavras são voltadas ao jogo League of Legends")

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