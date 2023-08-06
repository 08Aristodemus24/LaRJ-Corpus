-- read juris_meta.csv and insert values into created JurisMeta table
-- with ff. columns: file_path,answer,title,file_name,year,month,day,gr_number,division,case_code
\COPY JurisMeta (file_path, answer, title, file_name, year, month, day, gr_number, division, case_code) FROM '../raw labor related jurisprudence cleaning/juris_meta.csv' DELIMITER ',' CSV HEADER;




