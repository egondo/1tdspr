import oracledb

con = oracledb.connect(user="pf0313", dsn="oracle.fiap.com.br/orcl", password="professor#23")

sql = "insert into paciente(convenio, nome, nascimento) values(:convenio, :nome, to_date(:data, 'YYYY-MM-DD'))"
pac = {"nome": "Paulo Camargo", "convenio": "Prevent Senior", "data": '1960-08-21'}

cursor = con.cursor()
cursor.execute(sql, pac)

con.commit()
cursor.close()
con.close()
print("Paciente inserido com sucesso!")
