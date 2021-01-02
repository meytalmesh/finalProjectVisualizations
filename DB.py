import sqlite3

conn = sqlite3.connect('docDB.db')
c = conn.cursor()

# c.execute("SELECT sentenceNum,content,weight FROM text WHERE docID={}")

def get_text (docID):
    query = "SELECT sentenceNum,content,weight FROM sentence WHERE docID={}".format(docID)
    # print(query)
    c.execute(query)
    data = c.fetchall()
    # print(data)
    return data