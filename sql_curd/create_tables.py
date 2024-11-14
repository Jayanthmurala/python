import database_conntion as sql
#  creating table function
def create_table(tableName,*agrs):
    # joinine the  args with , to pass into table columns
    columns = ",".join(agrs)
    try:
        sql.cursor.execute(f"create table {tableName}({columns})")
        print(f"Table {tableName} Created Successfully ")
    except Exception:
        print("Error Or Table Exist\n------Tank you------")
if __name__=="__main__":
    # create_table("Employees", "id INT PRIMARY KEY", "name TEXT", "salary REAL")
    # create_table("Employe", "id INT PRIMARY KEY", "name TEXT", "salary REAL")
    sql.connection.commit()
    sql.connection.close()