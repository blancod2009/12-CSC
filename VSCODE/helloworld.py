from bottle import Bottle

app = Bottle()

@app.route('/')
def index():
    return 'Hello World from Bottle'


@app.route('/goodbye')
def index():
    return 'Poo poo'





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True, reloader=True)