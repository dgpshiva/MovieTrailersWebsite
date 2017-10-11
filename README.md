# Movie Trailers Website 

This repository contains code that can be used to host a website on your local machine that will display Movies trailers.
The website displays each movie's Title and its Poster image and on cliking the poster image runs the trailer for that movie.

## Table of content
- [Requirements](#requirements)
- [Running the code](#running-the-code)
- [Extending website to add more movies](#extending-website-to-add-more-movies)
- [Stopping the code](#stopping-the-code)

## Requirements
- Python should be installed on your local machine

## Running the code
- Pull the code from this repository to your local machine
- Navigate to the folder MovieTrailersWebsite/API
- Run the python code FlaskAPI.py from the command prompt (if using Windows) or from the Terminal (if using Mac) using the command "python FlaskAPI.py"
- Leave this window open
- Open another Command prompt/Terminal window
- Naviagte to the folder MovieTrailersWebsite
- Run the python code Main.py from the command prompt (if using Windows) or from the Terminal (if using Mac) using the command "python Main.py"
- This should automatically open up Movies Trailers website in your default web browser
- Click on any movie poster to run its trailer

## Extending website to add more movies
- Close the website if already open
- Naviagte to the folder MovieTrailersWebsite
- Open the text file DataFile.txt
- Add all details (MovieTitle, StoryLine, PosterImageLink, YouTubeTrailerUrl) for new movie in a new line in the text file. Values entered should be separated by tabs
- Save the DataFile.txt text file
- Naviagte to the folder MovieTrailersWebsite
- Run the python code Main.py from the command prompt (if using Windows) or from the Terminal (if using Mac) using the command "python Main.py"
- This should automatically open up Movies Trailers website in your default web browser with the new added movies
- Click on any movie poster to run its trailer

## Stopping the code
- Close the Movie trailers website if already open
- Close all command prompt/terminal windows that were opened
