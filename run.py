from connector import PostgreSQLConnection
import csv
import sqlite3


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("Error reading file:", e)

if __name__ == '__main__':
    
    with PostgreSQLConnection() as conn:
        try:
            file_paths1 = ['schemas/raw/employee.sql', 'schemas/raw/timesheet.sql']
                          
            for file_path in file_paths1:
                sql_query = read_file(file_path)
                if sql_query:
                    conn.execute_query(sql_query)
            
            

           
            file_table_pairs = [
                            ('data/output_file.csv', 'timesheet'),
                        ('data/employee_2021_08_01.csv', 'employee')
    ]
            for  file_path, table_name in file_table_pairs:
                if file_path:
                    conn.load_data_into_table(file_path, table_name)
                    
            file_paths2 = ['schemas/standard/employee.sql', 'schemas/standard/timesheet.sql',
                          'schemas/standard/insert_timesheet.sql', 
                          'schemas/standard/insert_employee.sql']
            for file_path in file_paths2:
                sql_query = read_file(file_path)
                if sql_query:
                    conn.execute_query(sql_query)
            
  
            

        except Exception as e:
            print(e)
            conn.disconnect()