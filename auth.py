from functools import wraps
from flask import request, jsonify

API_KEY = "SENHA_SUPER_SECRETA_123"

def token_required(f):
    """
    Decorator para proteger rotas com uma chave de API estática.
    A chave deve ser enviada no cabeçalho 'Authorization' como 'Bearer <API_KEY>'.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(" ")[1]
            except IndexError:
                return jsonify({"error": "Formato do token inválido. Use 'Bearer <token>.'"}), 401

        if not token:
            return jsonify({"error": "Token de autorização está faltando."}), 401

        if token != API_KEY:
            return jsonify({"error": "Token inválido."}), 401

        return f(*args, **kwargs)

    return decorated_function
