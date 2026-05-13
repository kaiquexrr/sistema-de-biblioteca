import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST")
)

class Autor():
    def __init__(self,nome,nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        
    def cadastrar(self):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO autores(nome,nacionalidade) VALUES (%s, %s)",(self.nome,self.nacionalidade)
        )
        conn.commit()
        print(f'autor {self.nome} cadastrado com sucesso!')




class Livro:
    def __init__(self,titulo,autor_id,ano):
        self.titulo = titulo
        self.autor_id = autor_id
        self.ano = ano

    def cadastrar(self):
        cursor =conn.cursor()
        cursor.execute(
            "INSERT INTO livros (titulo,autor_id,ano) VALUES (%s,%s,%s)",
            (self.titulo, self.autor_id, self.ano)
        )
        conn.commit()
        print(f'livro {self.titulo} cadastrado com sucesso!')

    def emprestar(self):
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE livros SET disponivel = FALSE WHERE titulo = %s",
            (self.titulo,)
        )
        conn.commit()
        print(f'livro {self.titulo} emprestado com sucesso')


    def devolver(self):
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE livros set disponivel = True WHERE titulo = %s",
            (self.titulo,)
        )
        conn.commit()
        print(f'livro {self.titulo} devolvido com sucesso')


def listar_livros():
    cursor = conn.cursor()
    cursor.execute(
        "SELECT livros.titulo, autores.nome, livros.ano, livros.disponivel" \
        " FROM livros" \
        " JOIN autores ON livros.autor_id = autores.id" 
     
    )
    livros = cursor.fetchall()
    if not livros:
        print('nenhum livro cadastrado')
    else:
        for livro in livros:
            disponivel = "disponivel" if livro[3] else "emprestado"
            print(f'titulo: {livro[0]}, autor: {livro[1]}, ano: {livro[2]}, {disponivel}')



    
def listar_disponiveis():
    cursor = conn.cursor()
    cursor.execute(
        "SELECT livros.titulo, autores.nome, livros.ano, livros.disponivel" \
        " FROM livros" \
        " JOIN autores ON livros.autor_id = autores.id" \
        " WHERE livros.disponivel = TRUE"
    )
    livros = cursor.fetchall()
    if not livros:
        print(f'nenhum livro disponivel')
    else:
        for livro in livros:
                print(f'titulo: {livro[0]}, autor: {livro[1]}, ano: {livro[2]},')


    
def menu():
    while True:
        print('[1] cadastrar autor')
        print('[2] cadastrar livro')
        print('[3] listar todos os livros')
        print('[4] listar livros disponiveis')
        print('[5] emprestar livro')
        print('[6] devolver livro')
        print('[7] sair')
        try:
            resposta = int(input(''))
        except ValueError:
            print('digite o numero correto')
            continue
        if resposta == 1:
            nome = input('nome do autor:')
            nacionalidade = input('nacionalidade:')
            autor = Autor(nome,nacionalidade)
            autor.cadastrar()

        elif resposta == 2:
            titulo = input('titulo do livro:')
            autor_id = int(input('id do autor:'))
            ano = int(input('ano:'))
            livro = Livro(titulo,autor_id,ano)
            livro.cadastrar()
        
        elif resposta == 3:
            listar_livros()

        elif resposta == 4:
            listar_disponiveis()

        elif resposta == 5:
            titulo = input('titulo do livro a emprestar:')
            livro = Livro(titulo,None,None)
            livro.emprestar()
        
        elif resposta == 6:
            titulo =input('titulo do livro a devolver:')
            livro = Livro(titulo,None, None)
            livro.devolver()
        
        elif resposta == 7 :
            break
        
        else:
            print('digite uma opcao valida')

if __name__ == "__main__":
    menu()