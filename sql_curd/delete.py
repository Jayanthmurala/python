import database_conntion as sql

# Delete Row From Table

def delete_row():
    table=input("Enter Table Name: ")
    condtition=input("Enter Condtition or row: ")
    try:
        if table=="":
            table='*'
            sql.cursor.execute(f"DELETE FROM {table} WHERE {condtition}")
        else:
            sql.cursor.execute(f"DELETE FROM {table} WHERE {condtition}")
        
        print("DELETED SUCCESSFULLY")
    except Exception:
        print("Error")


# DELETE DATA OF FULL TABLE 

def delete_full_table_data():
    table=input("Enter Table Name: ")
    try:
        sql.cursor.execute(f"DELETE FROM {table}")
        print(f"{table.capitalize()} TABLE DATA DELETE")
    except Exception:
        print("Error")

#  DROP TABLE

def delete_table():
    table=input("Enter Table Name: ")
    try:
        sql.cursor.execute(f"DROP TABLE {table}")
        print(f"{table.capitalize()} TABLE DELETE")
    except Exception:
        print("Error")





if __name__=="__main__":
    # delete_row()
    # delete_full_table_data()
    # delete_table()
    sql.connection.commit() 
    sql.connection.close()
