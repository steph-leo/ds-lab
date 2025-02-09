import sqlite3

conn = sqlite3.connect('Microfinance.db')

#create a cusor
c = conn.cursor()

#creata a table
# c.execute('''CREATE TABLE microfinances (
#         first_name text,
#         last_name text,
#         email_address text)
#     ''')

#insert a data into a table
# many_microfinances = [
#     ('isco', 'sali', 'sali@sali.com'),
#     ('igbo', 'musi', 'igbo@igbo.com'),
#     ('santo', 'ibo', 'ibo@santo.com')
# ]
# c.executemany("INSERT INTO microfinances VALUES (?,?,?)", many_microfinances)

#query the database
c.execute('SELECT  * FROM microfinances')
items = c.fetchall()

print('NAME' + '\t\t' + 'EMAIL')
print('-------' + '\t\t' + '-------')
for item in items:
    print(item[0]  + ' ' + item[1] + ' \t' + item[2])
#Print a messages to the terminal
# print ('Command excuted successfully...')
#commit my command
conn.commit()

#close the connection
conn.close()
