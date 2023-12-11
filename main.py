'''
04 etapas principais para criação de uma API - É um lugar para disponibilizar recursos e/ou funcionalidades

1 - Objetivo da API - Criar uma api de disponibilizar a consulta, criação, edição e exclusão de livros. 
2 - URL base (domínio) - localhost.com 
3 - Endpoints (rotas) - quais funcionalidades serão disponibilizadas?
    - localhost/livros - GET - Consultar todos os livros
    - localhost/livros/id - GET - (GET com id) | um livro especifico
    - localhost/livros/id - PUT - (PUT com id) | atualizar um livro especifico
    - localhost/livros/id - DELETE - (DELETE com id) | deletar um livro especifico
4 - Quais recursos 

'''
from flask import Flask, jsonify, request


#criando aplicação flask
main = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Aprendendo Python",
        "autor": "Renzo Nuccitelli",
        "isbn": "978-85-7522-721-6"
    },
    {
        "id": 2,
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "isbn": "978-85-7522-508-3"
    },
    {
        "id": 3,
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "isbn": "978-85-7522-508-3"
    }
]

# consultar(Todos)
@main.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)
# consultar(id)

@main.route("/livros/<int:id>", methods=["GET"])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
# Excluir

main.run(port=5000, host='localhost', debug=True)