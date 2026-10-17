import sqlite3

conn=sqlite3.connect('pyadvanced24.db')
cursor=conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id int PRIMARY KEY,
    product_name TEXT NOT NULL,
    price NUMERIC NOT NULL
    );
''')

cursor.execute('''
   CREATE TABLE IF NOT EXISTS orders(
    id int PRIMARY KEY,
    date_time TEXT NOT NULL,
    place TEXT NOT NULL,
    user_ID INTEGER,
    product_ID INTEGER,
    FOREIGN KEY(user_ID) REFERENCES users(id),
    FOREIGN KEY(product_ID) REFERENCES products(id)
    );
''')

# cursor.execute("DELETE FROM products;")
# cursor.execute("DELETE FROM orders;")
# cursor.execute("INSERT INTO products(id,product_name, price) VALUES(1,'iPhone18', 1500);")
# cursor.execute("INSERT INTO orders(date_time, place, user_ID, product_ID) VALUES('17-10-2026 12:20', 'XK',2,1);")
conn.commit()
cursor.execute('''
    SELECT p.product_name, u.name,o.*
    FROM orders o INNER JOIN products p
    ON o.product_ID=p.id INNER JOIN users u
    ON u.id=o.user_ID;
''')
records_from_db=cursor.fetchall()
for row in records_from_db:
    print(row)

