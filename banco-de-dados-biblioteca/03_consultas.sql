-- Consultas de exemplo pra usar no banco da biblioteca

-- 1. lista todos os livros com o nome do autor
SELECT livros.titulo, autores.nome, livros.ano_publicacao
FROM livros, autores
WHERE livros.autor_id = autores.id;

-- 2. livros que ainda nao foram devolvidos
SELECT livros.titulo, usuarios.nome, emprestimos.data_devolucao_prevista
FROM emprestimos, livros, usuarios
WHERE emprestimos.livro_id = livros.id
AND emprestimos.usuario_id = usuarios.id
AND emprestimos.data_devolucao_real IS NULL;

-- 3. quantidade de livros por genero
SELECT genero, COUNT(*) as quantidade
FROM livros
GROUP BY genero;

-- 4. autores brasileiros
SELECT nome FROM autores WHERE nacionalidade LIKE '%rasileir%';

-- 5. quantos emprestimos cada usuario ja fez
SELECT usuarios.nome, COUNT(*) as total_emprestimos
FROM emprestimos, usuarios
WHERE emprestimos.usuario_id = usuarios.id
GROUP BY usuarios.nome;
