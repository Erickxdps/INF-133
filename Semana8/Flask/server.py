    from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route("/sumar", methods=["GET"])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    
    if not num1:
        return (
            jsonify({"error": "Se requiere el num1 en los parámetros de la URL."}),
            400,
        )
    if not num2:
        return (
            jsonify({"error": "Se requiere el num2 en los parámetros de la URL."}),
            400,
        )
    num1 = int(num1)
    num2 = int(num2)
    return jsonify({"mensaje": f"La suma de ambos numeros es: {num1+num2}!"})

@app.route("/palindromo", methods=["GET"])
def palindromo():
    cad = request.args.get("cadena")
    if not cad:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )    
    c = cad[::-1]
    if c == cad:
        return jsonify({"mensaje": f"La cadena es palíndroma!"})
    else:
        return jsonify({"mensaje": f"La cadena no es palíndroma!"})
        
    


@app.route("/contar", methods=["GET"])
def contar():
    cad = request.args.get("cadena")
    vocal = request.args.get("vocal")
    
    if not cad:
        return (
            jsonify({"error": "Se requieren una cadena en los parámetros de la URL."}),
            400,
        )
    if not vocal:
        return (
            jsonify({"error": "Se requieren una vocal en los parámetros de la URL."}),
            400,
        )
    count = cad.lower().count(vocal.lower())
    
    return jsonify({"mensaje": f"La vocal '{vocal}' aparece {count} veces"})



if __name__ == "__main__":
    app.run()
    