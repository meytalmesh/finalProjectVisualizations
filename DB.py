import sqlite3

conn = sqlite3.connect('docDB.db')
c = conn.cursor()

# c.execute("SELECT sentenceNum,content,weight FROM text WHERE docID={}")

def get_text (docID):
    query = "SELECT sentenceNum,content,weight FROM sentence WHERE docID={}".format(docID)
    # print(query)
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    return data

def insert_text (docID, json):
    c = conn.cursor()
    c.execute("INSERT INTO texts values (?, ?)", [docID, json])
    conn.commit()

def get_json (docID):
    query = "SELECT textJson FROM texts WHERE docID={}".format(docID)
    # print(query)
    c.execute(query)
    data = c.fetchall()
    print(data[0][0])
    return data


