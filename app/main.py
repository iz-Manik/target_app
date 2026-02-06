from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/divide')
def divide():
    """This has a bug - no zero check!"""
    a = float(request.args.get('a', 10))
    b = float(request.args.get('b', 2))

    # 🐛 BUG: No zero division check
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
    result = a / b

    return jsonify({"result": result})

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    """This has a bug - no user validation!"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}

    # 🐛 BUG: Will crash if user_id not in dict
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    user = users[user_id]

    return jsonify({"id": user_id, "name": user})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
