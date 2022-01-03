import mysql.connector
import getpass
  
try:
      db = mysql.connector.connect(
        host="",
        user=input("Enter username: "),
        password=getpass("Enter password: ")
    )
    
except Error as e:
  print(e)
        
