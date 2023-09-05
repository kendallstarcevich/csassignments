#Kendall Starcevich
#Assignment 3
import json
with open("HighestGrossingMovies.json") as moviefile:
        movies = json.load(moviefile)
def most_popular_in_genre(list_of_movies, genre_type):
    most_popular_movie: None
    winning_sales=0
    for m in (list_of_movies):
        if genre_type in m["Genre"] and m["World Sales"]> winning_sales:
            most_popular_movie=m
            winning_sales=m["World Sales"]
    return most_popular_movie
print(most_popular_in_genre(movies, "Comedy"))

        