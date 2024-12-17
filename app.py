
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('Database/assistants.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/save', methods=['POST'])
def save_changes():
    data = request.json
    assistant_name = data.get('assistantName')
    instructions = data.get('instructions')
    new_function = data.get('newFunction')
    code_changes = data.get('codeChanges')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Save or update assistant data
    cursor.execute('''
        INSERT INTO assistants (name, instructions, functions, code)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
        instructions=excluded.instructions,
        functions=excluded.functions,
        code=excluded.code;
    ''', (assistant_name, instructions, new_function, code_changes))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Изменения сохранены успешно!'})

if __name__ == '__main__':
    app.run(debug=True)
