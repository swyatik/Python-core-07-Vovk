import sqlite3
conn = sqlite3.connect('my.db')
c = conn.cursor()
def add_user(username, userpass):
    c.execute("INSERT INTO users (name,password) VALUES ('%s', '%s')" % (username, userpass))
    conn.commit()

name = input("enter login\n")
passwd = input('enter code\n')
print("Users' list:\n")
add_user(name, passwd)
c.execute('SELECT * FROM users')
row = c.fetchone()
while row is not None:
    print("id:" + str(row[0]) + " Login: " + row[1] + " | code: " + row[2])
    row = c.fetchone()

c.close()
conn.close()