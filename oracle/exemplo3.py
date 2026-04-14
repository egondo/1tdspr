import oracledb

conexao = oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

id = input("ID do paciente: ")
convenio = input("Convenio: ")

sql = "update paciente set convenio = :convenio where pac_id = :id"
print(sql)
dado = {"convenio": convenio, "id": id}

cur = conexao.cursor()
cur.execute(sql, dado)

conexao.commit()
cur.close()
conexao.close()