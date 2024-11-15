import database_conntion as sql
import csv



#  Take  input data

def main():
    
    input_data=[]
    files=input("Enter File path: ")
    with open(files, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            input_data.append(tuple(row))
    return input_data


#  Insert data 
    
def into_table(cursor,data,columns,table_name):
    columns_list = columns.split(",")
    placeholders = ", ".join(["%s"] * len(columns_list))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    for datalist in data:
        cursor.execute(query, tuple(datalist))
    sql.connection.commit()
    print("DATA INSERTED SUCCESSFULLY")




# program start here

def insert_data():
    data=main()
    columns=input("Enter Columns (sep','): ")
    table_name = input("Enter Table Name: ")
    sql.cursor.execute("SHOW tables")
    tables = [table[0] for table in sql.cursor.fetchall()]  
    if table_name.lower() in tables:
        into_table(sql.cursor, data, columns, table_name)
    else:
        print("Error: Table does not exist.")
    
if __name__=="__main__":
    insert_data()



