from bottle import Bottle, template, request, static_file, redirect
from pathlib import Path
import sqlite3

app = Bottle()
ABSOLUTE_APPLICATION_PATH = Path(__file__).resolve().parents[0]
DB_PATH = ABSOLUTE_APPLICATION_PATH / 'todo.db'


@app.route('/')
def index():
    return template('home.tpl')


@app.get('/todo')
def todo_list():
    show = request.query.show or 'open'
    
    match show:
        case 'open':
            db_query = "SELECT id, task, status FROM todo WHERE status = 1"
        case 'closed':
            db_query = "SELECT id, task, status FROM todo WHERE status = 0"
        case 'all':
            db_query = "SELECT id, task, status FROM todo"
        case _:
            return template('message.tpl',
                message='Wrong query parameter: show must be either open, closed or all.')
                
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(db_query)
        result = cursor.fetchall()
        
    return template('show_tasks.tpl', rows=result)


@app.route('/new', method=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        new_task_text = request.forms.get('task', '').strip()
        if not new_task_text:
            return template('message.tpl', message='Task description cannot be empty.')
            
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            # Status 1 = Open, 0 = Closed
            cursor.execute("INSERT INTO todo (task, status) VALUES (?, ?)", (new_task_text, 1))
            new_id = cursor.lastrowid
            
        return template('message.tpl',
            message=f'The new task was inserted into the database, the ID is {new_id}')
    else:
        return template('new_task.tpl')


@app.route('/edit/<number:int>', method=['GET', 'POST'])
def edit_task(number):
    if request.method == 'POST':
        new_data = request.forms.get('task', '').strip()
        status_input = request.forms.get('status', '').strip()
        
        status = 0 if status_input.lower() in ('closed', '0', 'false') else 1
        
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE todo SET task = ?, status = ? WHERE id = ?", (new_data, status, number))
            
        return template('message.tpl',
            message=f'The task number {number} was successfully updated')
    else:
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT task, status FROM todo WHERE id = ?", (number,))
            current_data = cursor.fetchone()
            
        if not current_data:
            return template('message.tpl', message=f'The task number {number} does not exist!')
            
        return template('edit_task.tpl', current_data=current_data, number=number)


@app.route('/delete/<number:int>')
def delete_task(number):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM todo WHERE id = ?", (number,))
        
    redirect('/todo')


@app.route('/details/<task:re:[0-9]+>')
def show_item(task):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT task, status FROM todo WHERE id = ?", (task,))
        result = cursor.fetchone()
        
    if not result:
        return template('message.tpl',
            message=f'The task number {task} does not exist!')
    else:
        status_str = 'Open' if result[1] == 1 else 'Closed'
        return template('message.tpl',
            message=f'Task: {result[0]}, status: {status_str}')


@app.route('/as_json/<number:re:[0-9]+>')
def task_as_json(number):
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, task, status FROM todo WHERE id = ?", (number,))
        result = cursor.fetchone()
        
    if not result:
        return {'error': 'This task ID number does not exist!'}
    else:
        return {'id': result[0], 'task': result[1], 'status': result[2]}


@app.route('/static/<filepath:path>')
def send_static_file(filepath):
    ROOT_PATH = ABSOLUTE_APPLICATION_PATH / 'static'
    return static_file(filepath, root=ROOT_PATH)


@app.error(404)
def error_404(error):
    return 'Sorry, this page does not exist!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
