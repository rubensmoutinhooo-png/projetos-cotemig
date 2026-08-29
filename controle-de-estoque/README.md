# Controle de Estoque e Vendas

Trabalho de lógica de programação e banco de dados feito durante o curso de
Análise e Desenvolvimento de Sistemas (Cotemig). Sistema simples pra cadastrar
produto, controlar o estoque e registrar venda, em Python + SQLite.

## O que faz

- Cadastra produto (nome, preço, quantidade)
- Lista produtos e mostra o estoque
- Registra venda (desconta do estoque automático)
- Avisa quando o estoque tá baixo
- Mostra histórico de vendas

## Como rodar

```
python3 estoque.py
```

O banco (`estoque.db`) é criado sozinho na primeira vez que roda.

## Arquivos

- `estoque.py` - todo o código
- `estoque.db` - banco de dados (gerado ao rodar)
