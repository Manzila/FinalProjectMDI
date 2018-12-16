import pyodbc
import dateparser as dp

koneksi = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-57PI20C;'
                      'Database=ShareITSData;'
                      'Trusted_Connection=yes;')

read = open("dataset_1.txt")
txt = list(read.readlines())

for line in range(len(txt)):
    try:
        if line == 0:
           print('pass')
        else:
            isidata = list(txt[line].split('\t'))
            teks = ''
            for isi in range(len(isidata)):
                if isi == len(isidata)-1:
                   teks = teks+",\'"+str(dp.parse(isidata[isi]))[:-7]+ "\'"
                else:
                   if teks == '':
                      teks = teks+"\'"+isidata[isi].replace("\n","")+"\'"
                   else:
                      teks = teks+ ",\'" + isidata[isi].replace("\n","") + "\'"
            sql = "INSERT INTO [ShareITSData].[dbo].[LastAccess] ([No],[Username],[Nama],[Last_Access]) VAlUES(" + teks + ")"
            #cursor = koneksi.cursor()
            #cursor.execute(sql)
            #koneksi.commit()
            print(sql)
    except Exception:
        pass

           # for i in firstline:
    #kalo ada petik ditengah kita skip ignore error pyodbc
