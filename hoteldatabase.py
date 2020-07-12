import sqlite3

def hotelData():
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS booking(id INTEGER PRIMARY KEY, CustID TEXT, FirstName TEXT, Surname TEXT,\
                  Address TEXT, Gender TEXT, Mobile TEXT, Nationality TEXT, TpeofID TEXT, CheckIn TEXT, CheckOut TEXT)')
    con.commit()
    con.close()

def addHotelRec(CustID, FirstName, Surname ,Address , Gender , Mobile , Nationality , TypeOfId , CheckIn , CheckOut):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute('INSERT INTO booking VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', \
                (CustID, FirstName, Surname ,Address , Gender , Mobile , Nationality , TypeOfId , CheckIn , CheckOut))
    con.commit()
    con.close()

def displayHotelRec():
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM booking')
    rows = cur.fetchall()
    con.close
    return rows

def deleteHotelRec(id):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute('DELETE FROM booking WHERE id=?', (id,))
    con.commit()
    con.close

def updateHotelRec(ID, CustID='', FirstName='', Surname='', Address='', Gender='', Mobile='', Nationality='', TypeOfId='', CheckIn='', CheckOut=''):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute('UPDATE booking SET CustID=?, FirstName=?, Surname=?, Address=?, Gender=?, Mobile=?, Nationality=?, TypeOfId=?, CheckIn=?, CheckOut=?',\
                  (CustID, FirstName, Surname ,Address , Gender , Mobile , Nationality , TypeOfId , CheckIn , CheckOut, ID))
    con.commit()
    con.close()

def searchHotelRec(CustID='', FirstName='', Surname='', Address='', Gender='', Mobile='', Nationality='', TpeofID='', CheckIn='', CheckOut=''):
    con = sqlite3.connect('booking.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM booking WHERE CustID=? OR FirstName=? OR Surname=? OR Address=? OR Gender=? OR Mobile=? OR Nationality=?\
                OR TypeOfId=? OR CheckIn=? OR CheckOut=?', (CustID, FirstName, Surname ,Address , Gender , Mobile , Nationality , TypeOfId , CheckIn , CheckOut, ID))
    rows = cur.fetchall()
    con.close
    return rows

hotelData()
