# Repetir 3 vezes
for volta in range(3):
    print("Gato diz 'Meow!'")
    print("Dar uma volta")

# Desafio: o usuário escolhe quantas voltas, e mostramos o número de cada uma
voltas = int(input("Quantas voltas? "))
for volta in range(1, voltas + 1):
    print(f"Volta {volta}: Gato diz 'Meow!'")
