import pyodbc


koneksi = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-57PI20C;'
                      'Database=ShareITSData;'
                      'Trusted_Connection=yes;')


cursor = koneksi.cursor()
cursor.execute('SELECT * FROM dbo.Dosen')

for row in cursor:
    print(row)

