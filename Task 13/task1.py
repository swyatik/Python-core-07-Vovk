import sqlite3
conn = sqlite3.connect('my.db')
c = conn.cursor()
c.execute('''CREATE TABLE users (id int auto_increment primary key, name varchar, password varchar)''')
c.execute("INSERT INTO users (name,password) VALUES ('admin', '123')")
conn.commit()
c.close()
conn.close()