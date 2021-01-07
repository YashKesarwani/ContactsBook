import sqlite3

try:
    conn=sqlite3.connect('ContactList.db')
    print("Connected")
    curr=conn.cursor()
except:
    print("Connection failed")

def createTable():
    create_table="""CREATE TABLE IF NOT EXISTS contacts(id Integer PRIMARY KEY AUTOINCREMENT, firstName TEXT NOT NULL, lastName TEXT, mobile INTEGER NOT NULL, mobile2 INTEGER NOT NULL, email TEXT NOT NULL UNIQUE,groups TEXT); """
    curr.execute(create_table)
    conn.commit()


def addToDB(data):
    insert_data="""INSERT INTO contacts(firstName,lastName,mobile,mobile2,email,groups) VALUES(?,?,?,?,?,?);"""
    curr.execute(insert_data,data)
    conn.commit()
    print(data)

def getAllContacts():
    get_data="""SELECT id,firstName,lastName FROM contacts; """
    curr.execute(get_data)
    rows=curr.fetchall()
    return rows

def getRecord(name):
    name=name.split(' ')
    if len(name)==1:
        name.append('NULL')
    sel_data="""SELECT * FROM contacts WHERE firstName=(?) and lastName=(?) LIMIT 1; """
    curr.execute(sel_data,name)
    rows=curr.fetchall()
    print(rows)
    return rows

def deleteNumber(name):
    name=name.split(' ')
    if len(name)==1:
        name.append('NULL')
    del_data="""DELETE FROM contacts WHERE firstName=(?) and lastName=(?);"""
    curr.execute(del_data,name)
    conn.commit()
    return 1

def editInDB(data):
    update_data="""UPDATE contacts SET firstName=(?),lastName=(?),mobile=(?),mobile2=(?),email=(?),groups=(?) where id=(?);"""
    print(data)
    curr.execute(update_data,data)
    conn.commit()

def searchEmail(data):
    search_data="""SELECT * FROM contacts where email=(?); """
    curr.execute(search_data,data)
    rows=curr.fetchall()
    if rows==[]:
        return 1
    return 0