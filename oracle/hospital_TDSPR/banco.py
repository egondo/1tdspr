import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

def recupera_paciente_cpf(cpf: str) -> list:
    sql = "SELECT pac_id, nome, convenio, nascimento, cpf FROM PACIENTE WHERE cpf = :cpf"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, {"cpf": cpf})
            pac = cur.fetchone()
            return pac
        
def insere_paciente(pac: dict):
    sql = "INSERT INTO paciente(nome, cpf, convenio, nascimento) VALUES(:nome, :cpf, :convenio, to_date(:nascimento, 'DD-MM-YYYY'))"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, pac)
        conn.commit()

def insere_atendimento(atend: dict):
    sql = "INSERT INTO atendimento(chegada, saida, desfecho, pac_id_fk) VALUES(to_date(:chegada, 'DD-MM-YYYY HH24:MI'), to_date(:saida, 'DD-MM-YYYY HH24:MI'), :desfecho, :pac_id)"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, atend)
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

