# Exercício 03 – A soma em C (desafio opcional)

Baseado no material de apoio [A Ilusão da Soma](../../material-de-apoio/012-A-Ilusao-da-Soma.pdf).

A linha `c = a + b` parece uma só instrução, mas o processador executa uma **lista de ordens**:

1. `load A` — traz o 5 para a mesa de trabalho (registrador)
2. `load B` — traz o 3 para a mesa
3. `add` — soma os dois elementos na mesa
4. `store C` — guarda o resultado (8) de volta na gaveta (memória)

## Tarefa

1. Leia o arquivo [`solucao/soma.c`](solucao/soma.c).
2. Veja o Assembly gerado **sem otimização** (`-O0`), para o compilador não resolver a conta sozinho:
   - Com GCC instalado: `gcc -O0 -S soma.c` e abra o arquivo `soma.s`.
   - Ou cole o código no [Compiler Explorer](https://godbolt.org), escolha um compilador
     **RISC-V** e use a opção `-O0`.
3. Encontre no Assembly as instruções de carregar (`lw`), somar (`add`) e guardar (`sw`).
4. Agora compile com `-O2`. O que aconteceu com a soma?
