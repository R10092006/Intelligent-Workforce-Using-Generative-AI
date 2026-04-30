from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Create DB
def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Fake AI Logic
def analyze_task(task):
    if "urgent" in task.lower():
        return "High Priority - Assign immediately"
    elif "meeting" in task.lower():
        return "Schedule this meeting"
    elif "delay" in task.lower():
        return "Risk detected - take action"
    else:
        return "Normal task - plan accordingly"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    task = data.get('task')

    result = analyze_task(task)

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, result) VALUES (?, ?)", (task, result))
    conn.commit()
    conn.close()

    return jsonify({"result": result})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)