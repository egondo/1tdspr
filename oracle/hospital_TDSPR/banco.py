import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

def recupera_senha() -> int:
    sql = "SELECT senha.nextval FROM dual"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            reg = cur.fetchone()
            return reg[0]


def recupera_paciente_cpf(cpf: str) -> list:
    sql = "SELECT pac_id, nome, convenio, nascimento, cpf FROM PACIENTE WHERE cpf = :cpf"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"cpf": cpf})
            pac = cur.fetchone()
            return pac

def recupera_atendimento_senha(senha: int) -> dict:
    sql = "SELECT atend_id, chegada, saida, desfecho, senha, pac_id_fk  FROM atendimento WHERE senha = :senha ORDER BY atend_id DESC"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"senha": senha})
            reg = cur.fetchone()
            atend = {"atend_id": reg[0], "chegada": reg[1], "saida": reg[2], "desfecho": reg[3], "senha": reg[4], "pac_id_fk": reg[5]}
            return atend

        
def insere_paciente(pac: dict): 
    sql = "INSERT INTO paciente(nome, cpf, convenio, nascimento) VALUES(:nome, :cpf, :convenio, to_date(:nascimento, 'DD-MM-YYYY')) RETURNING pac_id INTO :id"
    with get_conexao() as conn:
        with conn.cursor() as cur:

            new_var = cur.var(oracledb.NUMBER)
            pac['id'] = new_var
            cur.execute(sql, pac)
            pac['id'] = new_var.getvalue()[0]
        conn.commit()

def insere_atendimento(atend: dict):
    sql = "INSERT INTO atendimento(chegada, saida, desfecho, pac_id_fk, senha) VALUES(to_date(:chegada, 'DD-MM-YYYY HH24:MI'), to_date(:saida, 'DD-MM-YYYY HH24:MI'), :desfecho, :pac_id, :senha)"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, atend)
        conn.commit()

def insere_triagem(triagem: dict):
    sql = "INSERT INTO triagem(data, peso, altura, pressao, batimento, temperatura, sintomas, atend_id_fk, func_id_fk) VALUES(to_date(:data, 'DD-MM-YYYY HH24:MI'), :peso, :altura, :pressao, :batimento, :temperatura, :sintomas, :atend_id_fk, :func_id_fk)"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, triagem)
        conn.commit()



if __name__ == "__main__":
    p = recupera_paciente_cpf('22')
    print(p)

    pac = {"nome": "Vagner Moura", "convenio": "SUS", "nascimento": "04-07-1989", "cpf": "23490786798"}
    #insere_paciente(pac)

    p = recupera_paciente_cpf('23490786798')
    print(p)

    atend = {"chegada": '14-04-2026 20:45', 'saida': None, 'desfecho':'em tratamento', 'pac_id': '25'}
    insere_atendimento(atend)

