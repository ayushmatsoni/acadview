import sqlite3
call=sqlite3.connect('assignment16.db')
print("NEW DATABASE CREATED")
#call.execute("DROP TABLE TITLE")
#call.execute('''CREATE TABLE BOOKS(BOOKID INT PRIMARY KEY NOT NULL,TITLEID INT NOT NULL, LOCATION TEXT NOT NULL, GENRE TEXT NOT NULL);''')
#call.execute('''CREATE TABLE TITLE(TITLEID INT  NOT NULL,TITLE TEXT NOT NULL, ISBN TEXT NOT NULL, PUBLISHERID INT  NOT NULL,PUBLISHERYEAR INT NOT NULL);''')
#call.execute('''CREATE TABLE AUTHORTITLE(AUTHORTITLEID INT  NOT NULL,AUTHORID INT NOT NULL,TITLEID INT NOT NULL);''')
#call.execute('''CREATE TABLE PUBLISHERS(PUBLISHERID INT  NOT NULL,NAME TEXT NOT NULL, STREETADDR TEXT NOT NULL, SUITENO INT  NOT NULL,ZIPCODEID INT NOT NULL);''')
#call.execute('''CREATE TABLE AUTHORS(AUTHORID INT  NOT NULL,FNAME TEXT NOT NULL, MNAME TEXT NOT NULL, LNAME TEXT  NOT NULL);''')
#call.execute('''CREATE TABLE ZIPCODES(ZIPCODEID INT  NOT NULL,CITY TEXT NOT NULL,STATE TEXT NOT NULL, ZIPCODE INT  NOT NULL);''')

print("ALL TABLES CREATED")

call.execute('''INSERT INTO BOOKS(BOOKID, TITLEID,LOCATION,GENRE) VALUES (45,33,'SOLAN','THRILLER'); ''')
call.execute('''INSERT INTO BOOKS(BOOKID, TITLEID,LOCATION,GENRE) VALUES (44,23,'SHIMLA','THRILLER'); ''')
call.execute('''INSERT INTO BOOKS(BOOKID, TITLEID,LOCATION,GENRE) VALUES (55,44,'CHD','COMEDY'); ''')
call.execute('''INSERT INTO BOOKS(BOOKID, TITLEID,LOCATION,GENRE) VALUES (74,13,'DELHI','ROMCOM'); ''')
call.execute('''INSERT INTO BOOKS(BOOKID, TITLEID,LOCATION,GENRE) VALUES (85,32,'CHD','HORROR'); ''')
call.execute('''INSERT INTO BOOKS(BOOKID, TITLEID,LOCATION,GENRE) VALUES (102,29,'SHIMLA','THRILLER'); ''')


call.execute('''INSERT INTO TITLE(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHERYEAR) VALUES (78,'HELLO',90,'89',2010); ''')
call.execute('''INSERT INTO TITLE(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHERYEAR) VALUES (778,'wELLO',95,'49',2010); ''')


call.execute('''INSERT INTO AUTHORTITLE(AUTHORTITLEID,AUTHORID,TITLEID) VALUES (78,45,90); ''')
call.execute('''INSERT INTO AUTHORTITLE(AUTHORTITLEID,AUTHORID,TITLEID) VALUES (110,45,78); ''')

call.execute('''INSERT INTO PUBLISHERS(PUBLISHERID,NAME,STREETADDR,SUITENO,ZIPCODEID) VALUES (7,'QWERTY','ASDFG',45,9000); ''')
call.execute('''INSERT INTO PUBLISHERS(PUBLISHERID,NAME,STREETADDR,SUITENO,ZIPCODEID) VALUES (70,'QWERTYASDFGH','QWERTYASDFG',455,90500); ''')

call.execute('''INSERT INTO AUTHORS(AUTHORID,FNAME,MNAME,LNAME) VALUES (45,'AYUSHMAT','B','SONI'); ''')
call.execute('''INSERT INTO AUTHORS(AUTHORID,FNAME,MNAME,LNAME) VALUES (14,'ISHA','','PRASHER'); ''')

call.execute('''INSERT INTO ZIPCODES(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES (45654,'SOLAN','HP',741852); ''')
call.execute('''INSERT INTO ZIPCODES(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES (74185,'SHIMLA','HP',52); ''')

cursor=call.execute("SELECT * FROM BOOKS;")
for row in cursor:
    print("BOOKID= ", row[0])
    print("TITLE= ", row[1])
    print("LOCATION= ", row[2])
    print("GENRE= ", row[3])
    print("")


call.execute("UPDATE BOOKS SET LOCATION ='SPITI' WHERE BOOKID = '102';")
call.execute("UPDATE BOOKS SET LOCATION ='BARALACHA' WHERE BOOKID = '85';")
cursor=call.execute("SELECT * FROM BOOKS;")
for row in cursor:
    print("BOOKID= ", row[0])
    print("TITLE= ", row[1])
    print("LOCATION= ", row[2])
    print("GENRE= ", row[3])
    print("")
