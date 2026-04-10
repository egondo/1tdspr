import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

if __name__== "__main__":
    nome = input("Nome: ")
    convenio = input("Convenio: ")
    data = input("Nascimento (dd-mm-aaaa): ")

    pac = {"nome": nome, "convenio": convenio, "nascimento": data}

    with get_conexao() as conn:
        with conn.cursor() as cur:
            sql = "insert into paciente(nome, convenio, nascimento) values(:nome, :convenio, to_date(:nascimento, 'DD-MM-YYYY'))"
            cur.execute(sql, pac)
        conn.commit()
    print("Paciente criado com sucesso!")