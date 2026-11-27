import random

secreto = random.randint(1, 100)
print("Pensei em um número de 1 a 100. Você tem 7 tentativas.")

for tentativa in range(1, 8):
    palpite = int(input(f"Tentativa {tentativa}: "))
    if palpite == secreto:
        print(f"🎉 Acertou em {tentativa} tentativas!")
        break
    elif palpite < secreto:
        print("É maior ⬆️")
    else:
        print("É menor ⬇️")
else:
    print(f"Acabaram as tentativas. O número era {secreto}.")
