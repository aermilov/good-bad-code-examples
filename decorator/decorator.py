from functools import wraps
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/public')
def public_endpoint():
    return jsonify(message="Это публичный эндпоинт, доступный всем.")

@app.route('/secret')
def secret_endpoint():
    return jsonify(message="Это секретный эндпоинт, доступный только авторизованным пользователям.")


def log_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f"Запрос к {request.path} от {request.remote_addr}")
        return f(*args, **kwargs)
    return decorated_function

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.headers.get('Authorization')
        if auth_token != 'MySecretToken':
            return jsonify(message="Ошибка аутентификации."), 403
        return f(*args, **kwargs)
    return decorated_function


@app.route('/public_decorated')
@log_access
def public_decorated_endpoint():
    return jsonify(message="Этот публичный эндпоинт логируется.")

@app.route('/secret_decorated')
@log_access
@authenticate
def secret_decorated_endpoint():
    return jsonify(message="Этот секретный эндпоинт требует аутентификации и его вызовы логируются.")
