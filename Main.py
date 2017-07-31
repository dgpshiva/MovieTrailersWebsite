'''
Created on Jul 27, 2017

@author: shiva
'''
import fresh_tomatoes
import MovieClass
import requests
import json

import sys

if __name__ == '__main__':
    
    movieKeys = []
    movieKeysResponse = requests.get('http://127.0.0.1:5000/moviesTrailerApi/v1/getMovieKeys')
    movieKeys = json.loads(movieKeysResponse.text)
    
    movieInstances = []
    moviesListResponse = requests.get('http://127.0.0.1:5000/moviesTrailerApi/v1/getMovies')
    moviesList = json.loads(moviesListResponse.text)
    for movie in moviesList:
        #print movie.get(movieKeys[2])
        movieInstances.append(MovieClass.Movie(movie.get(movieKeys[0]), movie.get(movieKeys[1]), str(movie.get(movieKeys[2])), movie.get(movieKeys[3])  ))
         
    fresh_tomatoes.open_movies_page(movieInstances)

        
#     print MovieClass.Movie.__doc__
#     print MovieClass.Movie.__name__
#     print MovieClass.Movie.__module__