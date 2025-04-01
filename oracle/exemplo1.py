import oracledb

conexao = oracledb.connect(user="pf0313",
                           password="professor#23",
                           dsn="oracle.fiap.com.br/orcl")

versao = conexao.version
print(f"Versao do banco oracle {versao}")
#print(type(conexao))

#abrindo o cursor com o banco de dados
#Equivalente ao Statement/PreparedStatement do Java
cur = conexao.cursor()
cur.execute("SELECT * FROM tb_filme")

#recuperando todos os registros da tabela tb_filme
registros = cur.fetchall()
for reg in registros:
    print(reg)

cur.close()
conexao.close()





