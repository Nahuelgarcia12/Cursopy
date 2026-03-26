from flask import Flask, render_template

import cliente_dao

app = Flask(__name__)
titulo_app = "Zona Fit (GYM)"
 # url : http://localhost:5000/
@app.route('/')
@app.route('/index.html')#url:http://localhost:5000/index.html
def inicio():
  app.logger.debug("Entramos al path de inicio /")
  #recuperamos datos de la bd
  cliente_db=cliente_dao.ClienteDAO.seleccionar()
  return render_template('index.html', titulo=titulo_app,clientes=cliente_db)

if __name__ == '__main__':
    app.run(debug=True)