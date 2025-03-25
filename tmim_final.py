# -*- coding: utf-8 -*-

pip install IMDbPY

# This allows the data to print out nicely. It is a code to warp text
# I pulled this code from "https://stackoverflow.com/questions/58890109/line-wrapping-in-collaboratory-google-results"

from IPython.display import HTML, display

def set_css():
  display(HTML('''
  <style>
    pre {
        white-space: pre-wrap;
    }
  </style>
  '''))
get_ipython().events.register('pre_run_cell', set_css)

# I created these functions to pick the specific information I wanted to pull from the APIs
#   I had to create two seperate functions because the data in the Top 100 movies had slightly different keys than the
# data in my other API used to pull info on the specifc movie/series the user inputs

def print_movie(m): # This function is used for the Top 100 movies
  print(f"\nTitle: {m['title']}")
  print(f"IMDb's Rating: {m['rating']}")
  print(f"Description: {m['description']}")

# This function is used for the movie/series the user inputs
# I added in more information since this is the specific movie/series the user wants info on
def print_movie2(m):
  print(f"\nTitle: {m['Title']}")
  print(f"Released {m['Released']}")
  print(f"IMDb's Rating: {m['Ratings'][0]['Value']}")
  print(f"Rated: {m['Rated']}")
  print(f"Genre: {m['Genre']}")
  print(f"Director: {m['Director']}")
  print(f"Writer: {m['Writer']}")
  print(f"Main Actors: {m['Actors']}")
  print(f"Type: {m['Type']}")
  print(f"Runtime: {m['Runtime']}")
  print(f"Language: {m['Language']}")
  print(f"Description: {m['Plot']}")

#  This code either prints out the Top 100 Movies from IMDb if user enters 'yes' (acting as movie recommendations for the user)
# OR it prompts the user to enter the title of any movie or series they would like information on, printing the selected data
# chosen by the second function I created (the title, IMDb's rating, rated, genre, actors, description, etc.) if the user enters 'no'

import imdb
import requests

url = "https://imdb-top-100-movies.p.rapidapi.com/?rapidapi-key=5083e44b88msh1f9735fc8724d8dp119c14jsncb6d87d5ac51"

headers = {
	"X-RapidAPI-Key": "5083e44b88msh1f9735fc8724d8dp119c14jsncb6d87d5ac51",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}
response = requests.get(url, headers=headers)


answer = input("Would you like to see IMDb's top 100 movies? Please enter 'yes' or 'no': ")

if answer == "yes":
    print("\nHere are IMDB's Top 100 movies")
    for movie in response.json():
      print_movie(movie) # first function I created above
else:
  imdb_info = imdb.IMDb() # this is how I am able to get info on all movies/series in IMDb's database
  name = input("\nEnter the title of the movie or series you want information on: ")
  search = imdb_info.search_movie(name) # search_movie method is to find all the related movies based on user's input

  for movie in range(len(search)): # for movie in the length of the search
    id = search[movie].movieID
    print(search[movie]['title'] + " : " + id) # prints all titles that have user input within it & its ID


  the_id = input("\nPlease find the correct title and type in its ID (the 7-digit number located next to the title) exactly as you see it in the list.\nIf the title repeats, the first result is most likely what you're looking for: ")

  query = f"http://www.omdbapi.com/?apikey=56f156a5&i=tt{the_id}" # adds movie id to URL to get the info on specific movie/series
  page = requests.get(query)
  data = page.json()
  print(f"\nHere is the information on {name}")
  print_movie2(data) # second function I created above
