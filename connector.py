import psycopg2
from config import config

class PostgreSQLConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(**params)
            print('Connection successful!')
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def execute_query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        cur.close()

    def load_data_into_table(self, file_path, table_name):
        """ Load data from a file into a table in the database """
        try:
            schema_name = 'raw'
            if table_name == 'timesheet':
                copy_query = f"COPY {schema_name}.timesheet FROM STDIN WITH CSV DELIMITER ',' NULL ''"
            elif table_name == 'employee':
                copy_query = f"COPY {schema_name}.employee FROM STDIN WITH CSV DELIMITER ',' NULL ''"
            else:
                print(f"Unknown table name: {table_name}")
                return

            with open(file_path, 'r') as file:
                next(file)  # Skip header line
                cur = self.conn.cursor()
                cur.copy_expert(copy_query, file)
                self.conn.commit()
                cur.close()

            print('Data loaded successfully into the table!')
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error loading data:', error)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print('Disconnected from the PostgreSQL database.')

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()


