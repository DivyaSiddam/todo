from flask import Flask, render_template, request, redirect, url_for
from models import add_task, get_tasks, complete_task

app = Flask(__name__)

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task_route():
    title = request.form['title']
    add_task(title)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_index>')
def complete_task_route(task_index):
    complete_task(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
