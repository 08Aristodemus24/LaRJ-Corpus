-- create database
CREATE DATABASE phil_corpus_juris_db;

-- connect to created database
\c phil_corpus_juris_db

-- create answers table
CREATE TABLE answers (
    id SERIAL PRIMARY KEY, 
    file_path VARCHAR(500), 
    answer VARCHAR(100)
);

INSERT INTO answers (id, file_path, answer) 
VALUES (1, 'test/file/path', 'LABOR RELATED');

-- read jurisprudence answers df here