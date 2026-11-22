# Exercício 01 – Seu primeiro programa gerador de sites

**Missão:** usar a lógica de programação (Python) para criar a estrutura do nosso próprio site (HTML).

1. Escrever um código em Python.
2. O Python vai criar um arquivo HTML automaticamente.
3. Abrir o site no navegador.

## Tarefa

Crie o arquivo `gerar_site.py` com o código abaixo e execute:

```python
# 1. O Python guarda nosso HTML na memória
meu_site = '<meta charset="utf-8"><h1>Olá, Internet! Meu primeiro site.</h1>'

# 2. O Python cria um arquivo real e escreve nele
with open('index.html', 'w', encoding='utf-8') as arquivo:
    arquivo.write(meu_site)

print('Site gerado com sucesso!')
```

```bash
python gerar_site.py
```

Depois, dê dois cliques no arquivo `index.html` que apareceu na pasta.

> **Por que `encoding='utf-8'` e `<meta charset="utf-8">`?**
> Sem eles, no Windows, acentos podem aparecer quebrados no navegador (ex.: `OlÃ¡`).
> Um define como o Python grava o arquivo; o outro avisa o navegador como lê-lo.

## Desafios

1. Adicione um parágrafo (`<p>`) com uma frase sobre você.
2. Use CSS para mudar a cor do título: `<h1 style="color: blue">`.
3. Adicione um botão que mostre "Olá, mundo!" ao ser clicado (JavaScript):
   `<button onclick="alert('Olá, mundo!')">Clique aqui</button>`
