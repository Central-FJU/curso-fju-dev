# FJU Dev

Repositório do curso **FJU Dev**, com o material das aulas: slides, material de apoio e códigos dos exercícios.

> As **gravações das aulas** não ficam no repositório (vídeos são grandes demais para o Git).
> O link de cada gravação está no README da respectiva aula.

## Aulas

| # | Aula | Tópicos |
|---|------|---------|
| 01 | [Hardware e Software](aula-01-hardware-e-software/) | CPU, RAM, disco, binário, ASCII, sistema operacional, portas lógicas |
| 02 | [Redes de Computadores e Internet](aula-02-redes-e-internet/) | IP, cliente/servidor, HTTP, DNS, URL, HTML/CSS/JS |
| 03 | [Pensamento Computacional e Linguagens](aula-03-pensamento-computacional-e-linguagens/) | Algoritmos, variáveis, condicionais (if/else), laços, primeiro programa em Python |

## Organização de cada aula

```
aula-XX-nome/
├── README.md            # objetivos, link da gravação, revisão
├── slides/              # slides apresentados em sala (0X0-*.pdf)
├── material-de-apoio/   # PDFs de apoio (0X1-*, 0X2-*) + links.md
└── exercicios/
    └── NN-nome/
        ├── enunciado.md
        └── solucao/
```

**Numeração dos arquivos:** os dois primeiros dígitos são a aula (`01X` = aula 1, `02X` = aula 2);
o último indica o tipo: `0` = slides da aula, `1` em diante = material de apoio.

## Links úteis

Vídeos recomendados para acompanhar o curso: [links-uteis.md](links-uteis.md)

## Pré-requisitos

Para os exercícios em Python, use **uma** das opções:

- **Google Colab** (não precisa instalar nada): [https://colab.research.google.com](https://colab.research.google.com)
  — crie um *Novo notebook*, cole o código em uma célula e aperte `Shift + Enter`.
- **Python no computador:** [Python 3](https://www.python.org/downloads/) instalado e um editor de código (ex.: VS Code).
