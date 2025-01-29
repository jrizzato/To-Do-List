from flask import Flask, render_template, request, request, redirect, url_for

app = Flask(__name__)

todos = []
# los todo van a tener la estructura de diccionario
# {'tarea': "hacer la tarea", 'hecho': False}


@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/agregar', methods=['POST'])
def agregar():
    todo = request.form.get('tarea')
    todos.append({'tarea': todo, 'hecho': False})
    return redirect(url_for('index'))

@app.route('/editar<int:index>', methods=['GET', 'POST'])
def editar(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['tarea'] = request.form.get('tarea')
        return redirect(url_for('index'))
    else:
        return render_template('editar.html', todo=todo, index=index)

@app.route('/check<int:index>', methods=['POST'])
def check(index):
    todo = todos[index]
    todo['hecho'] = not todo['hecho']
    return redirect(url_for('index'))

@app.route('/eliminar<int:index>')
def eliminar(index):
    del todos[index]
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)