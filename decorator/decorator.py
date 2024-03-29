from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/public')
def public_endpoint():
    print(f"Запрос к {request.path} от {request.remote_addr}")

    return jsonify(message="Это публичный эндпоинт, доступный всем.")

@app.route('/secret')
def secret_endpoint():
    print(f"Запрос к {request.path} от {request.remote_addr}")

    auth_token = request.headers.get('Authorization')
    if auth_token != 'MySecretToken':
        return jsonify(message="Ошибка аутентификации."), 403
    return jsonify(message="Это секретный эндпоинт, доступный только авторизованным пользователям.")

@app.route('/public_decorated')
def public_decorated_endpoint():
    print(f"Запрос к {request.path} от {request.remote_addr}")

    return jsonify(message="Этот публичный эндпоинт логируется.")

@app.route('/secret_decorated')
def secret_decorated_endpoint():
    print(f"Запрос к {request.path} от {request.remote_addr}")

    auth_token = request.headers.get('Authorization')
    if auth_token != 'СекретныйТокен':
        return jsonify(message="Ошибка аутентификации."), 403
    return jsonify(message="Этот секретный эндпоинт требует аутентификации и его вызовы логируются.")
