import database_conntion as sql

#  shows all the tables

def show_table(cursor=sql.cursor):
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for index,table in enumerate(tables,1):
        print(f"{index}.{table[0]}")



#  shows details of full table

def full_table(cursor=sql.cursor):
    table_name=input("Enter Table Name: ")
    try:
        cursor.execute(f"SELECT * FROM {table_name.lower()} ")
        table=cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description]
        output = " | ".join(column_names) + "\n"  # Add column names as the header
        output += "-" * (len(output) - 1) + "\n"  # Add a separator line
        for  row in table:
            output+= "|".join(map(str,row))+"\n"
        print(output)
    except Exception as e:
        print("Error")


# SELECT Requred columns

def userquere(cursor=sql.cursor):
    table_name=input("Enter Table Name: ")
    args=input("Enter Perameters: ")
    # selecter=",".join(args)
    try:
        cursor.execute(f"SELECT {args.lower()} FROM {table_name.lower()} ")
        table=cursor.fetchall()
        output=""
        for  row in table:
            output+= "|".join(map(str,row))+"\n"
        print(output)
    except Exception as e:
        print("Error")



if __name__=="__main__":
    # show_table(sql.cursor)
    # full_table("employees")
    # userquere(sql.cursor,"Employees","id","name")
    sql.connection.commit()
    sql.connection.close()


