import sqlite3

conn = sqlite3.connect('docDB.db')
c = conn.cursor()
print("Connected to SQLite")

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

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData



def storeImg(docID, img, visualisationType):
    c = conn.cursor()
    sqlite_insert_blob_query = """ INSERT INTO visualisationImages
                              (docId, visualisationType, image) VALUES (?, ?, ?)"""
    image = convertToBinaryData(img)
    data_tuple = (docID, visualisationType, image)
    c.execute(sqlite_insert_blob_query, data_tuple)
 #   c.execute("INSERT INTO visualisationImages values (?, ?, ?)", [docID, visualisationType, sqlite3.Binary(img.read())])
    conn.commit()
    c.close()

