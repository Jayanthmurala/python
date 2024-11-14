import database_conntion as sql

#  shows all the tables

def show_table(cursor):
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for index,table in enumerate(tables,1):
        print(f"{index}.{table[0]}")



#  shows details of full table

def full_table(cursor,table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name.lower()} ")
        table=cursor.fetchall()
        output=""
        for  row in table:
            output+= ",".join(map(str,row))+"\n"
        print(output)
    except Exception as e:
        print("Error")


# SELECT Requred columns

def userquere(cursor,table_name,*args):
    selecter=",".join(args)
    try:
        cursor.execute(f"SELECT {selecter.lower()} FROM {table_name.lower()} ")
        table=cursor.fetchall()
        output=""
        for  row in table:
            output+= "|".join(map(str,row))+"\n"
        print(output)
    except Exception as e:
        print("Error")



if __name__=="__main__":
    # show_table(sql.cursor)
    # full_table(sql.cursor,"employees")
    userquere(sql.cursor,"Employees","id","name")
    sql.connection.commit()
    sql.connection.close()


