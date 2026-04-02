
CREATE TABLE IF NOT EXISTS phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN 
    RETURN QUERY
    SELECT pb.id,pb.name,pb.phone
    FROM phonebook pb
    WHERE pb.name ILIKE '%' || p_pattern || '%'
       OR pb.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT pb.id , pb.name, pb.phone
    FROM phonebook pb
    ORDER BY pb.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;