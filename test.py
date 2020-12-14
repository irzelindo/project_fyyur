from models import Artist

import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(host='127.0.0.1', port=5432, dbname='momas_electronics', user='postgres', password='postgres')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM cliente;")

# Retrieve query results
print(cur.fetchall())
