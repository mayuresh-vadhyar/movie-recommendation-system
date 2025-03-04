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
  try:
    title = request.args.get('title')
    response = str(df.getIndexOfClosestTitle(title))
    return jsonify({'result': 'success', 'response': response})
  except Exception as E:
    return jsonify({'result': 'failure', 'error': str(E)})

@app.route('/movies/recommendations/<movieIndex>', methods=['GET'])
def getRecommendedMoviesByIndex(movieIndex):
  try:
    response = cbf.getRecommendedMovies(int(movieIndex))
    return jsonify({'result': 'success', 'data': response})
  except Exception as E:
    return jsonify({'result': 'failure', 'error': str(E)})

@app.route('/movies/recommendations', methods=['GET'])
def getRecommendedMovies():
  try:
    title = request.args.get('title')
    pageSize = request.args.get('pageSize') or 0
    pageNo = request.args.get('pageNo') or 1
    movieIndex = df.getIndexOfClosestTitle(title)
    response = cbf.getRecommendedMovies(int(movieIndex), int(pageSize), int(pageNo))
    return jsonify({'result': 'success', 'data': response})
  except Exception as E:
    return jsonify({'result': 'failure', 'error': str(E)})

app.run()