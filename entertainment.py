import media
import tomato

her = media.Film("Her",
                 "artificial intelligence",
                 "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                 "https://www.youtube.com/watch?v=ne6p6MfLBxc" )

#print(toy_story.storyline)

exmachina = media.Film("Ex Machina",
                    "artificial intelligence",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=sNExF5WYMaA" )

#print (avatar.storyline)
#avatar.show_trailer()

titanic = media.Film("Titanic",
                     "iceberg fun",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

films = [her, exmachina, titanic]
tomato.open_movies_page(films)
