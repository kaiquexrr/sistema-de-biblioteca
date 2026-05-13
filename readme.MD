# 📚 Sistema de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python com integração ao PostgreSQL. Permite cadastrar autores e livros, realizar empréstimos e devoluções, e listar o acervo com o nome do autor via terminal.

## 📋 Funcionalidades

- Cadastrar autores com nome e nacionalidade
- Cadastrar livros vinculados a um autor
- Listar todos os livros com nome do autor e status de disponibilidade
- Listar apenas livros disponíveis para empréstimo
- Emprestar livro — marca como indisponível no banco
- Devolver livro — marca como disponível novamente
- Validação de entradas inválidas no menu

## 🛠️ Tecnologias utilizadas

- Python 3
- PostgreSQL 16
- [Psycopg2](https://pypi.org/project/psycopg2-binary/) — driver de conexão Python + PostgreSQL

## 🗄️ Estrutura do banco de dados

```sql
CREATE DATABASE biblioteca;
\c biblioteca

CREATE TABLE autores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50)
);

CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor_id INTEGER REFERENCES autores(id),
    ano INTEGER,
    disponivel BOOLEAN DEFAULT TRUE
);
```

## ▶️ Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/kaiquexrr/sistema-de-biblioteca.git
cd sistema-de-biblioteca
```

**2. Crie e ative o ambiente virtual**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale a dependência**
```bash
pip install psycopg2-binary
```

**4. Configure o banco de dados**

Acesse o PostgreSQL e execute o script de criação das tabelas acima.

**5. Configure a conexão**

No arquivo `sistema.py`, ajuste as credenciais conforme seu ambiente:
```python
conn = psycopg2.connect(
    dbname="biblioteca",
    user="seu_usuario",
    password="sua_senha",
    host="localhost"
)
```

**6. Execute o programa**
```bash
python3 sistema.py
```

## 🖥️ Como usar

Ao executar, o menu aparece no terminal:

```
[1] cadastrar autor
[2] cadastrar livro
[3] listar todos os livros
[4] listar livros disponiveis
[5] emprestar livro
[6] devolver livro
[7] sair
```

> ⚠️ Cadastre um autor antes de cadastrar livros. Ao cadastrar um livro, informe o ID do autor gerado automaticamente pelo banco.

## 💡 Conceitos aplicados

- Programação Orientada a Objetos — classes `Autor` e `Livro` com atributos e métodos
- Relacionamento entre tabelas com chave estrangeira (`REFERENCES`)
- JOIN entre tabelas para exibir nome do autor junto ao livro
- CRUD completo com SQL puro — INSERT, SELECT, UPDATE
- Tipo BOOLEAN no PostgreSQL para controle de disponibilidade
- Proteção contra SQL Injection com placeholders `%s`
- Tratamento de exceções com `try/except`
- Estrutura com `if __name__ == '__main__'`

## 📌 Melhorias futuras

- [ ] Usar variáveis de ambiente para as credenciais do banco
- [ ] Listar autores com seus respectivos livros
- [ ] Adicionar histórico de empréstimos
- [ ] Buscar livro pelo título ou autor
- [ ] Validar se livro já está emprestado antes de emprestar novamente

---

Desenvolvido por [Kaique](https://github.com/kaiquexrr) durante os estudos de Python, POO e PostgreSQL.