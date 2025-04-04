import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23",
                            dsn="oracle.fiap.com.br/orcl")

def insere_filme(movie: dict):
    sql = "INSERT INTO filme(titulo, diretor, lancamento, atores, nota, genero, duracao) values(:titulo, :diretor, to_date(:lancamento, 'DD-MM-YYYY'), :atores, :nota, :genero, :duracao)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, movie)
        con.commit()


def altera_filme(movie: dict):
    sql = "UPDATE filme set titulo=:titulo, diretor=:diretor, lancamento=to_date(:lancamento, 'DD-MM-YYYY'), atores=:atores, nota=:nota, genero=:genero, duracao=:duracao WHERE id=:id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, movie)
        con.commit()

if __name__ == "__main__":
    filme = {
        'titulo': "Um sonho de liberdade",
        'diretor': 'Frank Darabont',
        'lancamento': '25-01-1995',
        'atores': 'Morgan Freeman, Tim Robbins',
        'nota': 8,
        'genero': 'drama',
        'duracao': 142
    }
    filme2 = {
        'titulo': 'ET',
        'diretor': 'Spielberg',
        'lancamento': '01-01-2000',
        'atores': 'Drew Barrimore',
        'nota': 7,
        'genero': 'infantil',
        'duracao': 150

    }
    filme3 = {
        'titulo': 'O jogo da Imitação',
        'diretor': 'Morten Tyldum',
        'lancamento': '29-08-2014',
        'atores': 'Bennedict Cumberbatch, Keira Knightley',
        'nota': 8,
        'genero': 'drama',
        'duracao': 150,
        'id': 8
    }

    #print(filme)
    #insere_filme(filme)
    altera_filme(filme3)
