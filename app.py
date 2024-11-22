from flask import Flask, request, jsonify
from health_utils import calculate_imc, calculate_mb

app = Flask(__name__)

@app.route('/imc', methods=['POST'])
def imc():
    """Point de terminaison pour calculer l'indice de masse corporelle"""
    data = request.json
    taille = data['taille']
    masse = data['masse']
    resultat = calculate_imc(taille, masse)
    return jsonify({"imc": resultat})

@app.route('/mb', methods=['POST'])
def mb():
    """Point de terminaison pour calculer le métabolisme de base aka les besoins métaboliques en kcal/jour"""
    data = request.json
    taille = data['taille']
    masse = data['masse']
    age = data['age']
    genre = data['genre']
    resultat = calculate_mb(taille, masse, age, genre)
    return jsonify({"mb": resultat})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
