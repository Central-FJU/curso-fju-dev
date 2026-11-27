menor, maior = 1, 100
tentativas = 0

print("Pense em um número de 1 a 100.")
while True:
    chute = (menor + maior) // 2
    tentativas += 1
    resposta = input(f"É {chute}? (+ maior, - menor, = acertou): ")
    if resposta == "=":
        print(f"Acertei em {tentativas} tentativas!")
        break
    elif resposta == "+":
        menor = chute + 1
    else:
        maior = chute - 1
