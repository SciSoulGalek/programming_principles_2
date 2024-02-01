"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5.
"""
def higher_55(movies, needed):
    found_movies = [movie for movie in movies if movie.get("name") == needed]
    
    if found_movies:
        for movie in found_movies:
            imdb_score = float(movie["imdb"])
            if imdb_score > 5.5:
                print(f"Yes, \"{needed}\" has an IMDb score of {imdb_score:.1f}")
            else:
                print(f"No, \"{needed}\" has an IMDb score of {imdb_score:.1f}")
    else:
        print(f"There is no movie with the name \"{needed}\"")

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
needed = str(input("Input the name of movie, to check whether it has IMDB score higher than 5.5 or not:\n"))

higher_55(movies, needed)