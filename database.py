import psycopg2

# Function to connect to the database
def get_connection():
    return psycopg2.connect(
        database="concerts",
        user="james",
        password="Secure@sql", 
        host="127.0.0.1",
        port="5432"
    )

def get_cursor(connection):
    return connection.cursor()

def close_connection(connection, cursor):
    cursor.close()
    connection.close()
