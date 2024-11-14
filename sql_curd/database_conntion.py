import mysql.connector as sql

# conntion 
connection = sql.Connect(
    host="localhost",
    user="root",
    password="@5Jayanthmurala",
    database="students"
)
# cursor
cursor = connection.cursor()
if __name__=="__main__":
    print("DATABASE CONNECTED SUCESSFULLY!")
    connection.commit()
    connection.close()