
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR,p_phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN 
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE 
        INSERT INTO phonebook(name,phone)
        VALUES (p_name,p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    v_name TEXT;
    v_phone TEXT;
BEGIN
   CREATE TEMP TABLE IF NOT EXISTS incorect_data(
       name TEXT,
       phone TEXT,
       reason TEXT
   ) ON COMMIT PRESERVE ROWS;

   DELETE FROM incorect_data;
    IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names array and phones array must have the same length';
    END IF;

    FOR i IN 1..array_length(p_names, 1) LOOP
        v_name := p_names[i];
        v_phone := p_phones[i];

        IF v_phone !~ '^\+?[0-9]{10,15}$' THEN
            INSERT INTO incorect_data(name, phone, reason)
            VALUES (v_name, v_phone, 'Invalid phone format');
        ELSE
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = v_name) THEN
                UPDATE phonebook
                SET phone = v_phone
                WHERE name = v_name;
            ELSE
                INSERT INTO phonebook(name, phone)
                VALUES (v_name, v_phone);
            END IF;
        END IF;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
   DELETE FROM phonebook
   WHERE name = p_value
   OR phone = p_value;
END;
$$