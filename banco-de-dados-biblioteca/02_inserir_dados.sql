-- Dados de exemplo pra testar o banco

INSERT INTO autores (nome, nacionalidade) VALUES ('Machado de Assis', 'Brasileiro');
INSERT INTO autores (nome, nacionalidade) VALUES ('J.K. Rowling', 'Britanica');
INSERT INTO autores (nome, nacionalidade) VALUES ('George Orwell', 'Britanico');
INSERT INTO autores (nome, nacionalidade) VALUES ('Clarice Lispector', 'Brasileira');

INSERT INTO livros (titulo, autor_id, ano_publicacao, genero, quantidade_exemplares) VALUES ('Dom Casmurro', 1, 1899, 'Romance', 3);
INSERT INTO livros (titulo, autor_id, ano_publicacao, genero, quantidade_exemplares) VALUES ('Harry Potter e a Pedra Filosofal', 2, 1997, 'Fantasia', 5);
INSERT INTO livros (titulo, autor_id, ano_publicacao, genero, quantidade_exemplares) VALUES ('1984', 3, 1949, 'Ficcao', 4);
INSERT INTO livros (titulo, autor_id, ano_publicacao, genero, quantidade_exemplares) VALUES ('A Hora da Estrela', 4, 1977, 'Romance', 2);

INSERT INTO usuarios (nome, email) VALUES ('Joao Pereira', 'joao@email.com');
INSERT INTO usuarios (nome, email) VALUES ('Ana Souza', 'ana@email.com');
INSERT INTO usuarios (nome, email) VALUES ('Pedro Lima', 'pedro@email.com');

INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista, data_devolucao_real)
VALUES (1, 1, '2026-08-01', '2026-08-15', '2026-08-14');

INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista, data_devolucao_real)
VALUES (2, 2, '2026-08-10', '2026-08-24', NULL);

INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista, data_devolucao_real)
VALUES (3, 3, '2026-08-20', '2026-09-03', NULL);
