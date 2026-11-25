# Exercício 01 – Seu primeiro programa

O programa vai **perguntar** o seu nome, **guardar** a resposta em uma variável (a "caixa")
e depois **mostrar** uma mensagem usando o que foi guardado.

## Tarefa

1. Abra o [Google Colab](https://colab.research.google.com) (ou o Python no seu computador).
2. Digite o código exatamente como está abaixo:
   ```python
   nome = input('Qual é o seu nome? ')
   print('Muito prazer em conhecer você,')
   print(nome)
   ```
3. Execute (no Colab, botão ▶ ou `Shift + Enter`) e responda à pergunta.

## Como ler o código

| Trecho | O que faz |
|--------|-----------|
| `input('Qual é o seu nome? ')` | pergunta ao usuário |
| `nome = ...` | cria a caixa (variável) e guarda a resposta nela (lemos da direita para a esquerda) |
| `print(...)` | mostra o resultado na tela |

## Desafio

Mostre tudo em uma linha só usando uma *f-string*:

```python
print(f"Olá, {nome}")
```
