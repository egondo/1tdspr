import oracledb

con = oracledb.connect(user="pf0313",
                       password="professor#23",
                       dsn="oracle.fiap.com.br/orcl")

cur = con.cursor()
placa = "LIE-8R90"
modelo = "Compass"
id=15
sql = f'''update carro set placa=:placa, 
                modelo=:modelo where id=:id'''
print(sql)
cur.execute(sql, {'placa': placa, 'modelo': modelo, 
                    'id': id})
con.commit()
cur.close()
con.close()


