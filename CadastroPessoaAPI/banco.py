import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", 
                            password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")


def insere_pessoa(pessoa: dict):
    sql = "insert into tb_pessoa(nome, telefone, cpf, nascimento) values(:nome, :telefone, :cpf, to_date(:nascimento, 'DD/MM/YYYY')) returning id into :id"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            new_id = cur.var(oracledb.NUMBER)
            pessoa['id'] = new_id
            cur.execute(sql, pessoa)
            pessoa['id'] = new_id.getvalue()[0]
        conn.commit()


def insere_endereco(endereco: dict):
    sql = "insert into tb_endereco(logradouro, numero, complemento, bairro, municipio, id_pessoa, cep) values(:logradouro, :numero, :complemento, :bairro, :municipio, :id_pessoa, :cep)"

    with get_conexao() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, endereco)
        conn.commit()


if __name__ == "__main__":
    #testando as funcoes de insercao
    pes = {"nome": "Donald Trump", "telefone": "(51) 9238-0492", "cpf": "423.038.019-99", "nascimento": "29/04/1978"}

    insere_pessoa(pes)

    end = {"logradouro": "Av Paulista", "numero": "1106", "complemento": "7 andar", "bairro": "Jardins", "cep": "01349-000", "municipio": "São Paulo"}

    end['id_pessoa'] = pes['id']
    insere_endereco(end)





