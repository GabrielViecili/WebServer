from flask import Flask, request, jsonify
from auth import token_required
import database as db

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso não encontrado"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

@app.route('/api/data', methods=['POST'])
@token_required
def create_data_route():
    """
    Rota para adicionar um novo dado.
    Espera um JSON no corpo da requisição com a chave 'data'.
    """
    if not request.is_json:
        return jsonify({"error": "Corpo da requisição deve ser JSON"}), 400

    value = request.json.get('data', None)
    if not value:
        return jsonify({"error": "O campo 'data' é obrigatório"}), 400

    try:
        db.add_data(value)
        return jsonify({"message": "Valor adicionado com sucesso"}), 201
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"error": "Não foi possível salvar o dado"}), 500

@app.route('/api/data', methods=['GET'])
@token_required
def get_data_route():
    """
    Rota para buscar todos os dados.
    """
    try:
        all_data = db.get_all_data()
        return jsonify(all_data), 200
    except Exception as e:
        print(f"Erro no servidor: {e}")
        return jsonify({"error": "Não foi possível buscar os dados"}), 500

if __name__ == '__main__':
    db.init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
