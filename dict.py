import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="phone",
   user="phone",
   password="Dev201801"
)
# read_dict: returns the list of all dictionary entries:
#   argument: C - the database connection.
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_work: add the values to the table:
#   argument: C - the database connection.
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict: save the list of all dictionary entries:
#   argument: C - the database connection.
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()
# read_print: print the list of all dictionary entries:
#   argument: C - the database connection.
def read_print():
    print('''Hello and welcome to the phone list, available commands:
    ADD    - add a phone number
    DELETE - delete a contact
    LIST   - list all phone numbers
    QUIT   - quit the program''')
   
def main():
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ")
        if cmd == "list":
            for i, wd, trans in read_dict(conn):
                print(f"{i}: {wd} - {trans}")
        elif cmd == "add":
            name = input("  Word: ")
            phone = input("  Translation: ")
            add_word(conn, name, phone)
            print(f" Added word {name}")
        elif cmd == "delete":
            ID = input("  ID: ")
            delete_word(conn, ID)
            print(f" Deleted {ID}")
        elif cmd == "quit":
            save_dict(conn)
            exit()

read_print()
main()