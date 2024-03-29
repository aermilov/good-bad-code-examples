from flask import Flask, request, jsonify
from functools import wraps


app = Flask(__name__)

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

def public_endpoint():
    return jsonify(message="Это публичный эндпоинт, доступный всем.")
app.route('/public')(log_access(public_endpoint))

@app.route('/secret')
def secret_endpoint():
    return jsonify(message="Это секретный эндпоинт, доступный только авторизованным пользователям.")
app.route('/secret')(log_access(authenticate(secret_endpoint)))
