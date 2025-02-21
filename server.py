from flask import Flask, request, jsonify
from models.DataFrame import DataFrame
from models.ContentBasedFiltering import ContentBasedFiltering

app = Flask(__name__)
df = DataFrame()
cbf = ContentBasedFiltering()

@app.route('/movies/index', methods=['GET'])
def getMovieIndexByTitle():
  try:
    title = request.args.get('title')
    response = str(df.getIndexFromTitle(title))
    return jsonify({'result': 'success', 'response': response})
  except Exception as E:
    return jsonify({'result': 'failure', 'error': str(E)})

@app.route('/movies/closest-index', methods=['GET'])
def getMovieIndexByClosestTitle():
  return jsonify({'result': 'success'})

@app.route('/movies/recommendations/<movieIndex>', methods=['GET'])
def getRecommendedMoviesByIndex(movieIndex):
  result = cbf.getRecommendedMovies(int(movieIndex))
  return jsonify({'result': result})

app.run()