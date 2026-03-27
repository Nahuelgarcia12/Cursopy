from flask import Flask, render_template, redirect, url_for
import cliente_dao
from cliente_form import ClienteForm
from cliente import Cliente

app = Flask(__name__)
titulo_app = "Zona Fit (GYM)"
app.config['SECRET_KEY'] = 'mundial2026'

@app.route('/')
@app.route('/index.html')
def inicio():
    app.logger.debug("Entramos al path de inicio /")
    clientes_db = cliente_dao.ClienteDAO.seleccionar()
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        #llenamos el objeto cliente con los valores del form
        cliente_forma.populate_obj(cliente)
        #guardo al nuevo cliente en bd
        cliente_dao.ClienteDAO.insertar(cliente)
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    cliente =cliente_dao.ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    clientes_db = cliente_dao.ClienteDAO.seleccionar()
    return render_template('index.html',titulo=titulo_app,
                           clientes=clientes_db, forma=cliente_forma)


@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))



if __name__ == '__main__':
    app.run(debug=True)