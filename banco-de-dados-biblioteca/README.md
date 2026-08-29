# Banco de Dados - Biblioteca

Trabalho de modelagem de banco de dados feito durante o curso de Análise e
Desenvolvimento de Sistemas (Cotemig). Modelo de um sistema de biblioteca:
livros, autores, usuários e empréstimos.

## Tabelas

- **autores** - id, nome, nacionalidade
- **livros** - id, titulo, autor_id, ano_publicacao, genero, quantidade_exemplares
- **usuarios** - id, nome, email, data_cadastro
- **emprestimos** - id, livro_id, usuario_id, data_emprestimo, data_devolucao_prevista, data_devolucao_real

Um autor pode ter vários livros. Um usuário pode ter vários empréstimos. Cada
empréstimo é de um livro só, pra um usuário só.

```
autores 1---N livros
usuarios 1---N emprestimos N---1 livros
```

## Arquivos

- `01_criar_tabelas.sql` - cria as 4 tabelas
- `02_inserir_dados.sql` - insere alguns dados de exemplo
- `03_consultas.sql` - consultas de exemplo (join, group by, etc)

## Como testar

```
sqlite3 biblioteca.db < 01_criar_tabelas.sql
sqlite3 biblioteca.db < 02_inserir_dados.sql
sqlite3 biblioteca.db < 03_consultas.sql
```
