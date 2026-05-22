from bottle import Bottle, template
import sqlite3
app = Bottle()

@app.route('/')
def index():
    return 'Hello from Bottle'

@app.route('/todo')
def todo_list():
    show  = request.query.show or 'open'
    match show:
        case 'open':
            db_query = "SELECT id, task FROM todo WHERE status LIKE '1'"
        case 'closed':
            db_query = "SELECT id, task FROM todo WHERE status LIKE '0'"
        case 'all':
            db_query = "SELECT id, task FROM todo"
        case _:
            return template('message.tpl',
                message = 'Wrong query parameter: show must be either open, closed or all.')
    with sqlite3.connect('todo.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")
        result = cursor.fetchall()
    output = template('show_tasks', rows=result)
    return str(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)