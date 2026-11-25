# Exercício 03 – Repetição (laços / loops)

Loops ensinam a máquina a repetir a mesma tarefa várias vezes, poupando você de
escrever a mesma instrução centenas de vezes.

Nos slides, o algoritmo do gato foi escrito assim:

```
Repetir 3 vezes:
    Gato diz 'Meow!'
    Dar uma volta
```

## Tarefa

Transforme esse algoritmo em Python. Em Python, "repetir 3 vezes" se escreve `for volta in range(3):`.

Repare que, assim como no `if`, as instruções que se repetem ficam **recuadas** (com espaço na frente).

## Desafio

1. Mostre também o número da volta (1, 2, 3).
2. Pergunte ao usuário quantas voltas o gato deve dar.
   Dica: `int(input("Quantas voltas? "))` transforma a resposta em número.
