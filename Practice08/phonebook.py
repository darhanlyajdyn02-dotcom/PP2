from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL
    )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created seccessfully")

def load_sql_file(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, "r" , encoding = "utf-8") as file:
        sql = file.read()
        cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print(f"{filename} Loaded successfully")

def call_search_function():
    pattern = input("Enter search pattern: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_phonebook(%s)",(pattern,))
    rows = cur.fetchall()
    print("\nSearch results: ")
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def call_upsert_procedure():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s,%s)",(name,phone))
    conn.commit()
    print("Upsert completed")
    cur.close()
    conn.close()
    

def call_bulk_insert():
    n = int(input("How many contacts do you want to add: "))
    names = []
    phones = []

    for i in range(n):
        name = input(f"Enter name #{i+1}: ")
        phone = input(f"Enter phone #{i+1}: ")
        names.append(name)
        phones.append(phone)
    
    conn = connect()
    cur = conn.cursor()
    cur.execute("Call insert_many_contacts(%s,%s)", (names,phones))
    conn.commit()
    print("Bulk insert completed")

    cur.execute("SELECT * FROM incorect_data")
    bad_rows = cur.fetchall()
    if bad_rows:
        print("\nIncorrect data: ")
        for row in bad_rows:
            print(row)
    else:
        print("No incorrect data.")
    cur.close()
    conn.close()
    

def call_pagination_function():
    limit = int(input("Enter Limit: "))
    offset = int(input("Enter Offset: "))

    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_phonebook_paginated(%s,%s)", (limit,offset))
    rows = cur.fetchall()

    print("\nPaginated results: ")
    for row in rows:
        print(row)
    cur.close()
    conn.close()
    

def call_delete_procedure():
    value = input("Enter name or phone to delete: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)",(value,))
    conn.commit()
    print("Delete completed.")
    cur.close()
    conn.close()

def show_all_contacts():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    print("\nAll contacts: ")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n_____PHONEBOOK MENU_____")
        print("1. Create tabble")
        print("2. Load functioncs.sql")
        print("3. Load procedures.sql")
        print("4. Search by pattern")
        print("5. Upsert contact")
        print("6. Insert many contacts")
        print("7. Show paginated contacts")
        print("8. Delete contact by name or phone")
        print("9. Show all contact")
        print("0. Exit")
        choice = input("Choose one option: ")

        if choice == "1":
            create_table()
        if choice == "2":
            load_sql_file("functions.sql")
        if choice == "3":
            load_sql_file("procedures.sql")
        if choice == "4":
            call_search_function()
        if choice == "5":
            call_upsert_procedure()
        if choice == "6":
            call_bulk_insert()
        if choice == "7":
            call_pagination_function()
        if choice == "8":
            call_delete_procedure()
        if choice == "9":
            show_all_contacts()
        if choice == "0":
            print("Goodbye!")
            break
        

if __name__ == "__main__":
    menu()