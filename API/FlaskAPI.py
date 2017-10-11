'''
Created on Jul 29, 2017

@author: shiva
'''

from flask_api import FlaskAPI
import os

app = FlaskAPI(__name__)
curDir = os.path.dirname(__file__)
pathToDataFile = os.path.join(curDir, '..', 'DataFile/DataFile.txt')
    

@app.route("/moviesTrailerApi/v1/getMovieKeys", methods=['GET'])    
def getMovieKeys():
    """ Returning column names of data file as movie keys list """
    with open(os.path.abspath(pathToDataFile)) as fileContent:
        headerLine = next(fileContent)
        headerElements = headerLine.split('\t')
        return headerElements


@app.route("/moviesTrailerApi/v1/getMovies", methods=['GET'])
def getMovies():
    """ Returning a list of movie dictionaries.
    
        The keys of each dictionary element 
        are the column names in the data file.
        
        The values of the dictionary element 
        are the values for the movie in that column.
    """
    movieList = []
    with open(os.path.abspath(pathToDataFile)) as fileContent:
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

if __name__ == '__main__':
    app.run(debug=False)
