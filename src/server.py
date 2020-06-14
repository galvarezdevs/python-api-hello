from flask import Flask

app = Flask(__name__)

# ruta principal
@app.route('/', methods=['GET'])
def hello_world():
    return '¡Hello world!'

# inciar servidor
if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port=4040, debug=True)
