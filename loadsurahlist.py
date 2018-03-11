import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='1373naam',
                       db='hifztracker')
cursor = mydb.cursor()

csv_data = csv.reader('/Users/naziram/PycharmProjects/HifzTracker/surahs114.csv')

for row in csv_data:
    cursor.execute("INSERT INTO surahs(('id','inEnglish','name','numberOfAyahs','revelationType', 'arabicName') VALUES(%s, %s, %s, %s, %s, %s)", row)))


# close the connection to the database.
mydb.commit()
cursor.close()
print()
"Done"
