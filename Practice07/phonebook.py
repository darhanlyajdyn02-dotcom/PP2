from connect import connect
import csv

# CREATE TABLE
def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table ready")

# INSERT FROM CSV
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv","r",encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                cur.execute(
                    "INSERT INTO phonebook(first_name, phone) VALUES (%s, %s)",
                    (row[0], row[1])
                )
            except:
                print("Skipping duplicate:",row)
    conn.commit()
    cur.close()
    conn.close()
    print("CSV data inserted")

# INSERT FROM CONSOLE
def insert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO phonebook(first_name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added!")
    except:
        conn.rollback()
        print("Error (maybe duplicate phone)")

    cur.close()
    conn.close()


# SHOW ALL
def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# SEARCH
def search_by_name():
    name = input("Enter name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s",
        (f"%{name}%",)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# UPDATE
def update_contact():
    phone = input("Enter phone to update: ")
    new_name = input("Enter new name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE phone = %s",
        (new_name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Updated")


# DELETE
def delete_contact():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE first_name = %s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")

# MENU
def menu():
    while True:
        print("\n PHONEBOOK ")
        print("1. Create table")
        print("2. Insert from CSV")
        print("3. Add contact")
        print("4. Show contacts")
        print("5. Search by name")
        print("6. Update contact")
        print("7. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            insert_contact()
        elif choice == "4":
            show_contacts()
        elif choice == "5":
            search_by_name()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# RUN
if __name__ == "__main__":
    menu()

