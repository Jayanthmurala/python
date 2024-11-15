import database_conntion as sql


# Where Condtition's

def main(table_name,condtition,column='*',cursor=sql.cursor):
    try:
        cursor.execute(f"SELECT {column} FROM {table_name} WHERE {condtition}")
        data=cursor.fetchall()
        output=""
        for row in data:
            output+="|".join(map(str,row))+'\n'
        print(output)
    except Exception:
        print("Error")

# Taking inputs block
def where():
    table=input("Enter Table Name: ")
    column=input("Select Columns: ")
    condtition=input("Enter Condtition: ")
    if column == "":
        column="*"
        main(table,condtition,column,cursor=sql.cursor)
    else:
        main(table,condtition,column,cursor=sql.cursor)


if __name__=="__main__":
    where()
    sql.connection.commit()
    sql.connection.close()