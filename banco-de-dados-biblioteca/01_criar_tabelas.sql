-- ============================================================
-- Modelagem de Banco de Dados - Biblioteca
-- Script de criação das tabelas (DDL)
-- ============================================================

CREATE TABLE autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nacionalidade TEXT
);

CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER NOT NULL,
    ano_publicacao INTEGER,
    genero TEXT,
    quantidade_exemplares INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (autor_id) REFERENCES autores (id)
);

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    data_cadastro TEXT NOT NULL DEFAULT (date('now'))
);

CREATE TABLE emprestimos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livro_id INTEGER NOT NULL,
    usuario_id INTEGER NOT NULL,
    data_emprestimo TEXT NOT NULL DEFAULT (date('now')),
    data_devolucao_prevista TEXT NOT NULL,
    data_devolucao_real TEXT,
    FOREIGN KEY (livro_id) REFERENCES livros (id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);
