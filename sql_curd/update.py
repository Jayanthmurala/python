import database_conntion as sql
from read_table import full_table


# Function to Update Table

def update_data():
    Taking_table_name=input("Enter Table Name: ")
    full_table(Taking_table_name)
    columns=input("Enter Changes (name='name'..): ")
    condition=input("Enter Your Conditon(id=1): ")
    try:
        update_block(Taking_table_name,columns,condition)
    except Exception:
        print(" Error ")

# quere function
def update_block(tablename,columns,condition,cursor=sql.cursor):
    cursor.execute(f"UPDATE {tablename} SET {columns} WHERE {condition}")
    sql.connection.commit()
    print('update Successfull')






if __name__=="__main__":
    update_data()
    sql.connection.close()
    