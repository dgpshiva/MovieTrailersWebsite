'''
Created on Jul 29, 2017

@author: shiva
'''

from flask_api import FlaskAPI
import os

app = FlaskAPI(__name__)

@app.route("/moviesTrailerApi/v1/getMovies", methods=['GET'])
def getMovies():
    movieList = []
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DataFile/DataFile.txt'))) as fileContent:
        headerLine = next(fileContent)
        headerElements = headerLine.split('\t')
        for line in fileContent:
            movieDictionary = {}
            movieElements = line.split('\t')
            movieDictionary[headerElements[0]] = movieElements[0]
            movieDictionary[headerElements[1]] = movieElements[1]
            movieDictionary[headerElements[2]] = movieElements[2]
            movieDictionary[headerElements[3]] = movieElements[3]
            movieList.append(movieDictionary)
            
    return movieList
    
    
@app.route("/moviesTrailerApi/v1/getMovieKeys", methods=['GET'])    
def getMovieKeys():
    with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'DataFile/DataFile.txt'))) as fileContent:
        headerLine = next(fileContent)
        headerElements = headerLine.split('\t')
        return headerElements
    
    
    
if __name__ == '__main__':
    app.run(debug=True)