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
from flask import Flask, jsonify, request, make_response
from bd import Livros
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database='bibliotecalivros'
)



#criando aplicação flask
main = Flask(__name__)

main.config['JSON_SORT_KEYS'] = False

#livros = Livros

my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM livros")
meus_livros = my_cursor.fetchall() #fetchall() - retorna todos os registros
livros = list()
for livro in meus_livros:
    livros.append(
        {
            'ID': livro[0],
            'titulo': livro[1],
            'autor': livro[2],
            'editora': livro[3],
            'ano': livro[4]

        }
    )


# consultar(Todos)
@main.route("/livros", methods=["GET"])
def obter_livros():
    return make_response(
            jsonify(
                mensagem='Lista de livros', 
                dados=livros
            )
        )

# consultar(id)

@main.route("/livros/<int:id>", methods=["GET"])
def obter_livros_por_id(id):
    
    for livro in livros:
        if livro.get('ID') == id:
            return jsonify(livro)
    return jsonify({"erro": "livro não encontrado"}), 404

# Criar
@main.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    sql = f"INSERT INTO livros (titulo, autor, editora, ano) VALUES ('{novo_livro['titulo']}','{novo_livro['autor']}','{novo_livro['editora']}','{novo_livro['ano']}')"
    my_cursor.execute(sql)
    mydb.commit()


    return make_response( 
        jsonify(
            mensagem='Carro criado com sucesso',
            livropost=novo_livro
        )
    )

# Editar
@main.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    #receber o livro que será alterado do front
    livro_alterado = request.get_json()
    #saber indice e livro/id para saber qual alterar
    for indice, livro in enumerate(livros):
        if livro.get('ID') == id: #Verifica se o id do livro é igual ao id passado na url
            #livros[indice].update(livro_alterado)
            sql = f"UPDATE livros SET titulo = '{livro_alterado['titulo']}', autor = '{livro_alterado['autor']}', editora = '{livro_alterado['editora']}', ano = '{livro_alterado['ano']}' WHERE id = {id}"      
            my_cursor.execute(sql)
            mydb.commit()
            
            return make_response(
                jsonify(
                    mensagem='Carro criado com sucesso',
                    editado=livro_alterado
                )
            )


# Excluir
@main.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('ID') == id:
            sql = f"DELETE FROM livros WHERE id = {id}"
            my_cursor.execute(sql)
            mydb.commit()
            
            return make_response(
                jsonify(
                    mensagem='livro excluido com sucesso',
                    deletado=livro
                )
            )
    return make_response(
        jsonify(
            mensagem= "livro não encontrado"
        ), 404
    )


    '''
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            #livros.pop(indice)
            del livros[indice]
            return make_response (
                jsonify(
                    mensagem="livro excluido com sucesso"
                ), 200
            )
        return make_response(
            jsonify(
                mensagem= "livro não encontrado"
             ), 404
        )
    return jsonify(livros)
    '''


main.run(port=5000, host='localhost', debug=True)