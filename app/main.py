from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/divide')
def divide():
    """This has a bug - no zero check!"""
    try:
        a = float(request.args.get('a', 10))
        b = float(request.args.get('b', 2))

        if b == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400

        result = a / b

        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input for 'a' or 'b'. Must be numbers."}), 400

@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    """This has a bug - no user validation!"""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}

    user = users.get(user_id)

    if user is None:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    return jsonify({"id": user_id, "name": user})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)