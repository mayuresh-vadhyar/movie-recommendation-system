from flask import Flask, jsonify
from models.ContentBasedFiltering import ContentBasedFiltering

app = Flask(__name__)
cbf = ContentBasedFiltering()

@app.route('/movies/index', methods=['GET'])
def getMovieIndexByTitle():
  return jsonify({'result': 'success'})

@app.route('/movies/closest-index', methods=['GET'])
def getMovieIndexByClosestTitle():
  return jsonify({'result': 'success'})

@app.route('/movies/recommendations/<movieIndex>', methods=['GET'])
def getRecommendedMoviesByIndex(movieIndex):
  result = cbf.getRecommendedMovies(int(movieIndex))
  return jsonify({'result': result})

app.run()