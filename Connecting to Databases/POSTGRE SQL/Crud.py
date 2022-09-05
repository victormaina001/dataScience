# Import libraries
import pandas as pd
import psycopg2
from config.config import config_1
from src.data.db_conn import load_db_table
# Connect to PostgreSQL
params = config_1(config_db = 'database.ini')
engine = psycopg2.connect(**params)
print('Python connected to PostgreSQL!')
# Create table
cur = engine.cursor()
cur.execute('DROP TABLE IF EXISTS customer')
cur.execute("""
CREATE TABLE customer(
customer_id INT PRIMARY KEY NOT NULL,
name CHAR(50) NOT NULL,
address CHAR(100),
email CHAR(50),
phone_number CHAR(20));
""")
print('Table created in PostgreSQL')
# Close the connection
engine.commit()
# Insert values to the table
cur = engine.cursor()
cur.execute("""
INSERT INTO customer (customer_id,name,address,email,phone_number)
VALUES (12345,'Audhi','Indonesia','myemail@gmail.com','+621234567');
""")
cur.execute("""
INSERT INTO customer (customer_id,name,address,email,phone_number)
VALUES (56789,'Aprilliant','Japan','email@gmail.com','+6213579246');
""")
print('Values inserted to PostgreSQL')
# Close the connection
engine.commit()
engine.close()


# # Read the table
# cur = engine.cursor()
# cur.execute("""
# SELECT customer_id,name,email FROM customer LIMIT 5;
# """)
# print('Read table in PostgreSQL')
# # Close the connection
# engine.commit()
# engine.close()

# # Insert values to the table
# cur = engine.cursor()
# cur.execute("""
# UPDATE customer SET address = 'Japan' WHERE customer_id = 12345;
# """)
# print('Values updated in PostgreSQL')
# # Close the connection
# engine.commit()
# engine.close()

# # Delete rows from the table
# cur = engine.cursor()
# cur.execute("""
# DELETE FROM customer WHERE customer_id = 12345;
# """)
# print('Values deleted from PostgreSQL')
# # Close the connection
# engine.commit()
# engine.close()
