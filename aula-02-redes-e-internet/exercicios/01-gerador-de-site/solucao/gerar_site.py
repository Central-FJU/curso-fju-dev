# 1. O Python guarda nosso HTML na memória
meu_site = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Meu primeiro site</title>
</head>
<body>
  <h1 style="color: blue">Olá, Internet! Meu primeiro site.</h1>
  <p>Esta página foi gerada por um programa em Python.</p>
  <button onclick="alert('Olá, mundo!')">Clique aqui</button>
</body>
</html>
"""

# 2. O Python cria um arquivo real e escreve nele
with open('index.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(meu_site)

print('Site gerado com sucesso!')
