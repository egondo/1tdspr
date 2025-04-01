import oracledb

con = oracledb.connect(user="pf0313",
                       password="professor#23",
                       dsn="oracle.fiap.com.br/orcl")

cur = con.cursor()
placa = "GBL-8R34"
modelo = "BMW X5"
id='15 or 1=1'
sql = f'''update carro set placa='{placa}', 
                modelo='{modelo}' where id={id}'''
print(sql)
cur.execute(sql)
con.commit()
cur.close()
con.close()


