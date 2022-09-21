import psycopg2
import psycopg2.extras
import psycopg2.extras
from config import config
import psycopg2.extras




try:
    params = config()
    conn = psycopg2.connect(**params)
                       
    
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS customer1')

            create_script = ''' CREATE TABLE IF NOT EXISTS customer1 (
                                    id      int PRIMARY KEY,
                                    name    varchar(40) NOT NULL,
                                    salary  int,
                                    dept_id varchar(30)) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO customer1 (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'James', 12000, 'D1'), (2, 'Robin', 15000, 'D1'), (3, 'Xavier', 20000, 'D2'),(4,'Victor',25000,'D2')]
            for record in insert_values:
                cur.execute(insert_script, record)

            update_script = 'UPDATE customer1 SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            delete_script = 'DELETE FROM customer1 WHERE name = %s'
            delete_record = ('James',)
            cur.execute(delete_script, delete_record)

            cur.execute('SELECT * FROM customer1')
            for record in cur.fetchall():
                print(record['name'], record['salary'])
except Exception as error:
        print(error)
finally:
        if conn is not None:
            conn.close()