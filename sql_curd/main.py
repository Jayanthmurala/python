import database_conntion
from insert_data import insert_data
import read_table
from create_tables import create_table 
#   TO CREATE TABLE
create_table("Employees", "id INT PRIMARY KEY", "name TEXT", "salary REAL")

insert_data()