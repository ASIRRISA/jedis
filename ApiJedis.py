from flask import Flask, jsonify, request

app = Flask(__name__)

from jedis import jedis # importa el diccionario  para luego leer, añadir, modificar, borrar
#ten en cuenta que el diccionario esta en otro fichero aparte sino lo importara, 
#no podria tener acceso a el
@app.route("/")
def saludo():
    print("Bienvenido a mi API REST de Jedis, para Fikis de Star Wars, ¡Que la fuerza te acompañe! )


@app.route('/jedis', methods=['GET'])#se puede obviar GET por qu es  el metodo por defecto
def templojedis():

    return jsonify({'jedis': jedis})

@app.route('/jedis/<string:jedi_nombre>')
def templojedi(jedi_nombre):#aqui en singular
    
    for jedi in jedis:

        if jedi['nombre'] == jedi_nombre.lower():
            jedisFound=jedi
        #me devuelve un diccionario
    if (len(jedisFound) > 0):

        return jsonify({'jedi': jedisFound})

    return jsonify({'Holomensaje': 'Jedi no registrado en los archivos del templo'})

#Create Data Routes
@app.route('/jedis', methods=['POST'])
def Consejojedi():

    nuevo_jedi = {
        'nombre': request.json['nombre'],
        'raza': request.json['raza'],
        'planeta_origen': request.json['planeta_origen'],
        'color_espada':  request.json['color_espada']
    }
    jedis.append(nuevo_jedi)
    return jsonify({'Holomensaje':'El jedi ha sido añadido al consejo','jedis': jedis})

#Update Data Route
@app.route('/jedis/<string:jedi_nombre>', methods=['PUT'])
def entrenarpadawan(jedi_nombre):
    
    jedisFound = [jedi for jedi in jedis if jedi['nombre'] == jedi_nombre]

    if (len(jedisFound) > 0):
        jedisFound[0]['nombre'] = request.json['nombre']
        jedisFound[0]['raza'] = request.json['raza']
        jedisFound[0]['planeta_origen'] = request.json['planeta_origen']
        jedisFound[0]['color_espada'] = request.json['color_espada']
        return jsonify({
            'Holomensaje': 'El padawan ha sido entrenado Correctamente',
            'jedi': jedisFound[0]
        })
    return jsonify({'Holomensaje': 'jedi no entrenado'})

#DELETE Data Route
@app.route('/jedis/<string:jedi_nombre>', methods=['DELETE'])
def Orden66(jedi_nombre):

    jedisFound = [jedi for jedi in jedis if jedi['nombre'] == jedi_nombre]

    if len(jedisFound) > 0:
        
        jedis.remove(jedisFound[0])
        return jsonify({
            'Ejecute la orden 66': 'Jedi eliminado',
            'jedis': jedis
        })
    return jsonify({"Holomensaje":"El jedi se ha escondido"})

if __name__ == '__main__':
    app.run(debug=True, port=1990)