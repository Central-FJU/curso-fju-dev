chovendo = input("Está chovendo? (s/n) ")
if chovendo == "s":
    print("Leve o guarda-chuva ☂️")
else:
    print("Leve os óculos de sol 😎")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2

print(f"Média: {media}")
if media >= 7:
    print("Aprovado! 🎉")
elif media >= 5:
    print("Recuperação 📚")
else:
    print("Reprovado 😢")
