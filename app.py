from flask import Flask,render_template,request,jsonify
from funcion import pagary, encontrar_propietario

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/procesar', methods=['GET'])
def procesar():
    ratio_seleccionado = request.args.get('ratio')
    valor = request.args.get('valor')
    money = request.args.get('dinero')
    valor2 = request.args.get('destino')
    
    if ratio_seleccionado == "yape" :
        return jsonify(pagary(valor,money,valor2))
    else:
        return jsonify(encontrar_propietario(valor))

if __name__ == '__main__':
    app.run(debug=True)