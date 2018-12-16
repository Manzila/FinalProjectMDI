import pyodbc
import dateparser as dp

koneksi = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-57PI20C;'
                      'Database=ShareITSData;'
                      'Trusted_Connection=yes;')

read = open("dataset_2.txt")
txt = list(read.readlines())

for line in range(len(txt)):
    try:
        if line == 0:
           print('pass')
        else:
            isidata = list(txt[line].split('\t'))
            teks = ''
            for isi in range(len(isidata)):
                if isi == len(isidata)-2:
                   teks = teks+",\'"+str(dp.parse(isidata[isi]))+ "\'"
                else:
                   if teks == '':
                      teks = teks+"\'"+isidata[isi].replace("\n","")+"\'"
                   else:
                      teks = teks+ ",\'" + isidata[isi].replace("\n","") + "\'"
            sql = "INSERT INTO [ShareITSData].[dbo].[Dosen] ([No],[Fakultas],[Jurusan],[Matakuliah],[Dosen], [Last_Access], [Email]) VAlUES(" + teks + ")"
            cursor = koneksi.cursor()
            cursor.execute(sql)
            koneksi.commit()
    except Exception:
        pass
print('success')


