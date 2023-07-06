from connector import PostgreSQLConnection
import csv
import sqlite3
import sys
import os


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
    if len(sys.argv) < 3:
        print("Usage: python script.py <schema_directory> <data_directory>")
        sys.exit(1)
    
    schema_directory = sys.argv[1]
    data_directory = sys.argv[2]
    
    with PostgreSQLConnection() as conn:
        try:
            # Creating the table in raw_schema
            raw_schema_directory = os.path.join(schema_directory, 'raw')
            file_paths1 = [os.path.join(raw_schema_directory, filename) for filename in os.listdir(raw_schema_directory) if filename.endswith('.sql')]
                          
            for file_path in file_paths1:
                sql_query = read_file(file_path)
                if sql_query:
                    conn.execute_query(sql_query)

            # Loading data in raw_schema
            raw_data_directory = os.path.join(data_directory, 'raw')
            file_table_pairs = [(os.path.join(raw_data_directory, filename), os.path.splitext(filename)[0]) for filename in os.listdir(raw_data_directory) if filename.endswith('.csv')]
            
            for file_path, table_name in file_table_pairs:
                if file_path:
                    conn.load_data_into_table(file_path, table_name)
            
            # Creating and inserting data in standard schema
            standard_schema_directory = os.path.join(schema_directory, 'standard')
            file_paths2 = [os.path.join(standard_schema_directory, filename) for filename in os.listdir(standard_schema_directory) if filename.endswith('.sql')]
            
            for file_path in file_paths2:
                sql_query = read_file(file_path)
                if sql_query:
                    conn.execute_query(sql_query)
            
            # Inserting additional data files
            additional_data_directory = os.path.join(data_directory, 'additional')
            additional_files = [(os.path.join(additional_data_directory, filename), os.path.splitext(filename)[0]) for filename in os.listdir(additional_data_directory) if filename.endswith('.csv')]
            
            for file_path, table_name in additional_files:
                if file_path:
                    conn.load_data_into_table(file_path, table_name)
            
        except Exception as e:
            print(e)
            conn.disconnect()
