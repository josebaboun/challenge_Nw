from flask import Flask, request, jsonify
from flask_restful import Api
from flask_cors import CORS
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    print(request)
    X = request.json['data']  # Suponiendo que los datos se envían en formato JSON
  
    
    # Código para procesar los datos de entrada y realizar predicciones con el modelo
    # ...
    predictions = model.predict(X)
    
    # Retornar las predicciones en el formato deseado (por ejemplo, JSON)
    return jsonify({'predictions': predictions.tolist()})

api = Api(app)
cors = CORS(app)

if __name__ == '__main__':
    # Cargamos el modelo serializado
    with open('best_model.sav', 'rb') as file:
        model = pickle.load(file)
    app.run(host='0.0.0.0', port=5500, debug=True)
