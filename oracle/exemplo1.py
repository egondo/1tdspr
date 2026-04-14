import oracledb

#abrindo conexao
con = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

print("Mostrando a versao do banco ", con.version)

#abrindo o cursor
cur = con.cursor()
cur.execute("select * from paciente")

#pegando os registros retornados pelo banco
registros = cur.fetchall()
#print(registros)

for info in registros:
    print(info)

cur.close()
con.close()