import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_pessoa(pessoa: dict):
    sql = "insert into tdspr_pessoa(nome, nascimento, altura, peso, sexo) values(:nome, to_date(:nascimento, 'DD-MM-YYYY'), :altura, :peso, :sexo)"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, pessoa)
        conn.commit()

def recupera_pessoa() -> list:
    sql = "select id, nome, to_char(nascimento, 'DD-MM-YYYY'), altura, peso, sexo from tdspr_pessoa"
    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            dados = cur.fetchall()
            return dados
                