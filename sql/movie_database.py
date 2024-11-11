import mysql.connector as sql
import sys

#  functions used
def full_table(cursor):
    cursor.execute("SELECT * FROM movie_data")
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        print(row)

def show_tables(cursor):
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)

def read_tables(cursor,table_Name,read='*'):
    cursor.execute(f"SELECT {read} FROM {table_Name}")
    rows = cursor.fetchall()
    print(rows)

# movie data
movies_data = [
    ["Inception", "8.8", "2010", "English", "Yes"],
    ["Parasite", "8.6", "2019", "Korean", "Yes"],
    ["RRR", "8.0", "2022", "Telugu", "Yes"],
    ["The Dark Knight", "9.0", "2008", "English", "Yes"],
    ["Dangal", "8.4", "2016", "Hindi", "Yes"]
]
# connectoin to mysql 
connection = sql.connect(
    host="localhost",
    user="root",
    password="@5Jayanthmurala",
    database="movieData"
)

# cursor
cursor = connection.cursor()

# create table
try:
    # ["Movie Name", "Rating", "Year", "Language", "Available in OTT"]
    cursor.execute("""
                CREATE table movie_data (
                    movie_name varchar(255),
                    rating float,
                    year Int,
                   language varchar(255),
                   ott varchar(255)
                );
                """)
    print("Table created successfully.")
    
except Exception as e:
    print("Table alredy exist\nlike to continu CURD")
    res=input('->y/n ')
    if(res=="y"):
        opp =input("1.full_table\n2.read_tables\n3.show_tables\n: ")
        match opp:
            case "1":
                full_table(cursor)
            case "2":
                tn= input("Enter table name: ")
                m = input("Enter column(s) to read (default '*'): ")
                if m == "":
                    m = '*'
                read_tables(cursor, tn, m)
            case "3":
                show_tables(cursor)
            case _:
                print("Invalid option. Exiting program.")
                sys.exit()
        

    else:
        print("Tank You :)")
        sys.exit()
    
for data in movies_data:
    cursor.execute(
        "INSERT INTO movie_data (movie_name, rating, year, language, ott) VALUES (%s, %s, %s, %s, %s)",
        (data[0], data[1], data[2], data[3], data[4])
    )
print("queary successfully")


connection.commit()
connection.close()