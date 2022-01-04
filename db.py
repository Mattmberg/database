from mysql.connector import connect, Error
from getpass import getpass

options = ["a", "r", "q"]

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE deck_colors"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
        #print(connection)
except Error as e:
    print(e)

while True:
    user_choice = input("Welcome to the Deck List database, what would you like to do? (a)dd to data, (r)ead the data, or (q)uit the program: ")

    if user_choice == "q":
        break

    if user_choice == "a":

    if user_choice == "r":
        cursor.execute("SELECT * FROM deck_colors")
