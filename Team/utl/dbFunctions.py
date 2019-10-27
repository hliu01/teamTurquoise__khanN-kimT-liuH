import sqlite3
import csv

def accountExists(username, password):
    DB_FILE= "accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id, username FROM USERNAMES WHERE username = \"{}\" AND password = \"{}\";".format(username, password)
    c.execute(command)
    q = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    else:
        return q[0][0] #return ID of user if exists


def userExists(username):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id, username FROM USERNAMES WHERE username = \"{}\";".format(username)
    c.execute(command)
    q = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    else:
        return q[0][0] #return ID of user if exists

def addUser(username, password):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id, username FROM USERNAMES WHERE username = \"{}\";".format(username)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 0:
        command = "SELECT id FROM USERNAMES;"
        c.execute(command)
        q = c.fetchall()
        command = "INSERT INTO USERNAMES VALUES({}, \"{}\", \"{}\");".format(q[len(q)-1][0]+1,username,password)
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False

def addStory(title, text, date):
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id, title FROM STORIES WHERE title = \"{}\";".format(title)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 0:
        command = "SELECT id FROM STORIES;"
        c.execute(command)
        q = c.fetchall()
        command = "INSERT INTO STORIES VALUES({}, \"{}\", \"{}\", \"{}\");".format(q[len(q)-1][0]+1,title,text,date)
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False

def getStory():
    DB_FILE="accounts.db"
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT * FROM STORIES;"
    c.execute(command)
    new = c.fetchall()
    db.commit() #save changes
    db.close()  #close database
    return new