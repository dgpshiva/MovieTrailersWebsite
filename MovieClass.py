'''
Created on Jul 27, 2017

@author: shiva
'''
import webbrowser


class Movie():    
    """ Each instance of this class is one movie.
        This class also has functions to display a movie's trailer and poster.
    """
    
    def __init__(self, title, storyLine, posterImageLink, youTubeTrailerUrl):
        self.title = title
        self.storyLine = storyLine
        self.poster_image_url = posterImageLink
        self.trailer_youtube_url = youTubeTrailerUrl
        
    def startTrailer(self):
        webbrowser.open("https://www.youtube.com/watch?v=8hYlB38asDY")
        
    def displayPoster(self):
        webbrowser.open(self.posterImageLink)
