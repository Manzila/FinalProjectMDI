import pyodbc
koneksi = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-57PI20C;'
                      'Database=ShareITS;'
                      'Trusted_Connection=yes;')



read = open("dataset_2.txt")
#for line in read:
txt = (read.readline())
dataset2 = txt.split("\t")
#print(dataset2)


sql = "use ShareITSData create table Dosen(" + dataset2[0] + " VARCHAR(255)," + dataset2[1] + " VARCHAR(255)," + dataset2[
    2] + " VARCHAR(255)," + dataset2[3] + " VARCHAR(255), " + dataset2[4] + " VARCHAR(255), Last_Access Datetime, Email VARCHAR(255))"
cursor = koneksi.cursor()
cursor.execute(sql)
koneksi.commit()
print('success')


read = open("dataset_3.txt")
#for line in read:
txt = (read.readline())
dataset3 = txt.split("\t")
#print(dataset3)


sql = "use ShareITSData create table Mahasiswa(" + dataset3[0] + " VARCHAR(255)," + dataset3[1] + " VARCHAR(255)," + dataset3[
    2] + " VARCHAR(255)," + dataset3[3] + " VARCHAR(255), " + dataset3[4] + " VARCHAR(255), Last_Access Datetime, Email VARCHAR(255))"
cursor = koneksi.cursor()
cursor.execute(sql)
koneksi.commit()
print('success')

read.close()

read = open("dataset_1.txt")
#for line in read:
txt = (read.readline())
dataset1 = txt.split("\t")
#print(dataset1)


sql = "use ShareITSData create table LastAccess(" + dataset1[0] + " VARCHAR(255)," + dataset1[1] + " VARCHAR(255)," + dataset1[
    2] + " VARCHAR(255),Last_Access Datetime)"
cursor = koneksi.cursor()
cursor.execute(sql)
koneksi.commit()
print('success')
