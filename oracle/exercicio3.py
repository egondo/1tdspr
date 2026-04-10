import exercicio1 as ex

if __name__ == "__main__":
    nome = input("Digite um fragmento do nome: ")

    with ex.get_conexao() as conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM PACIENTE WHERE lower(nome) LIKE :nome"

            cur.execute(sql, {"nome": f'%{nome.lower()}%'})

            regs = cur.fetchall()
            for reg in regs:
                print(reg)