'''
Created on Jul 27, 2017

@author: shiva
'''
import fresh_tomatoes
import json
import requests
import sys

import MovieClass

if __name__ == '__main__':
    # Getting the movie keys from the header line of data file
    movieKeys = []
    movieKeysResponse = requests.get('http://127.0.0.1:5000/moviesTrailerApi/v1/getMovieKeys')  # NOQA
    movieKeys = json.loads(movieKeysResponse.text)
    
    # Getting the movie instances inside data file as a list
    movieInstances = []
    moviesListResponse = requests.get('http://127.0.0.1:5000/moviesTrailerApi/v1/getMovies')  # NOQA
    
    # Get list of movies in the DataFile.txt
    moviesList = json.loads(moviesListResponse.text)
    
    for movie in moviesList:
        movieInstances.append(MovieClass.Movie(movie.get(movieKeys[0]), 
                                               movie.get(movieKeys[1]), 
                                               str(movie.get(movieKeys[2])), 
                                               movie.get(movieKeys[3])))
         
    fresh_tomatoes.open_movies_page(movieInstances)
