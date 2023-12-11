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
    return jsonify({"erro": "livro não encontrado"}), 404

# Criar
@main.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(novo_livro)

# Editar
@main.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    #receber o livro que será alterado do front
    livro_alterado = request.get_json()
    #saber indice e livro/id para saber qual alterar
    for indice, livro in enumerate(livros):
        if livro.get('id') == id: #Verifica se o id do livro é igual ao id passado na url
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Excluir
@main.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            #livros.pop(indice)
            del livros[indice]
            return jsonify({"mensagem": "livro excluido com sucesso"}), 200
        return jsonify({"mensagem": "livro não encontrado"}), 404
    return jsonify(livros)



main.run(port=5000, host='localhost', debug=True)