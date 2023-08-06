-- connect to created database
\c phil_corpus_juris_db

-- create answers table
CREATE TABLE Answers (
    id SERIAL PRIMARY KEY, 
    file_path VARCHAR(250), 
    answer VARCHAR(100)
);

-- create juris_meta table
CREATE TABLE JurisMeta (
    id SERIAL PRIMARY KEY,
    file_path VARCHAR(250),
    answer VARCHAR(20),
    title VARCHAR(250),
    file_name VARCHAR(250),
    year CHAR,
    month CHAR,
    day CHAR,
    gr_number VARCHAR(100),
    division VARCHAR(100),
    case_code VARCHAR(100)
);