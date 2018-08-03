import numpy as np
import csv
import pymysql

data_file = open("data.txt")
count= 0
date=[]
countries=[]
for aline in data_file.readlines(): #read each line of text file
    aline.strip("\n")
    count=count+1
    if count>11:
        values=aline.split(',') #seperate values by comma
        countries.append(values[1:]) #store in countries array
        date.append(values[0])
#print(date[0])
date= np.array(date)
country=np.array(countries)
country[:,-1] = [w.replace('\n', '') for w in country[:,-1]]
data=np.column_stack((date,country))
data1=[[char or 0 for char in i]for i in data]

connection = pymysql.connect(host='localhost',
                             user='root',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Create a new record
        
        cursor.execute("CREATE DATABASE WORLDFLUDATABASE")

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Create table coloumn
        cursor.execute("CREATE TABLE WORLDFLUDATABASE.FLUDATA(Date DATE,Argentina INT,Australia INT,Austria INT,Belgium INT,Bolivia INT,Brazil INT,Bulgaria INT,Canada INT,Chile INT,France INT,Germany INT,Hungary INT,Japan INT,Mexico INT,Netherlands INT,NewZealand INT,Norway INT,Paraguay INT,Peru INT,Poland INT,Romania INT,Russia INT,SouthAfrica INT,Spain INT,Sweden INT,Switzerland INT,Ukraine INT,UnitedStates INT,Uruguay INT)")
    connection.commit()

    with connection.cursor() as cursor:
        for i in range(1,np.shape(data1)[0]):
            cursor.execute("INSERT INTO WORLDFLUDATABASE.FLUDATA(Date,Argentina,Australia,Austria,Belgium,Bolivia,Brazil,Bulgaria,Canada,Chile,France,Germany,Hungary,Japan,Mexico,Netherlands,NewZealand,Norway,Paraguay,Peru,Poland,Romania,Russia,SouthAfrica,Spain,Sweden,Switzerland,Ukraine,UnitedStates,Uruguay) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[char for char in data1[i]])
    connection.commit()
#### Q1 ####
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM WORLDFLUDATABASE.FLUDATA WHERE Date BETWEEN '2003-08-01' AND '2003-08-31'")
    connection.commit()

#### Q2 ####
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT YEAR(Date) FROM WORLDFLUDATABASE.FLUDATA WHERE UnitedStates>1000")
    connection.commit()

#### Q3 ####
    with connection.cursor() as cursor:
        cursor.execute("SELECT DISTINCT YEAR(Date) FROM WORLDFLUDATABASE.FLUDATA WHERE UnitedStates > (Argentina +Australia+Austria+Belgium+Bolivia+Brazil+Bulgaria+Canada+Chile+France+Germany+Hungary+Japan+Mexico+Netherlands+NewZealand+Norway+Paraguay+Peru+Poland+Romania+Russia+SouthAfrica+Spain+Sweden+Switzerland+Ukraine+UnitedStates+Uruguay)/29")
    connection.commit()

#### Q4 ####
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM WORLDFLUDATABASE.FLUDATA PROCEDURE ANALYSE()")
    connection.commit()

#### Q5 ####
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM WORLDFLUDATABASE.FLUDATA PROCEDURE ANALYSE()")

finally:
    connection.close()
#data2=pd.dataframe(data1)
data_file.close()

