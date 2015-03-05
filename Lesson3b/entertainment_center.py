import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

league_of_their_own = media.Movie("A League of Their Own",
                                  "To achieve the incredible you have to attempt the impossible.",
                                  "http://ia.media-imdb.com/images/M/MV5BMTM1NzQ1OTM3NF5BMl5BanBnXkFtZTcwMDAwMjUyMQ@@._V1_SY317_CR1,0,214,317_AL_.jpg",
                                  "https://www.youtube.com/watch?v=WcN392H2jx0")

#league_of_their_own.show_trailer()

miracle = media.Movie("Miracle",
                      "Believe",
                      "http://ia.media-imdb.com/images/M/MV5BMjEyOTk1OTcyNV5BMl5BanBnXkFtZTYwNjMzNDU3._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=v64ofT1rGOw")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_SX214_AL_.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

hunger_games = media.Movie("The Hunger Games",
                           "A really real reality show",
                           "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=qoUT7q2iTbQ")

divergent = media.Movie("Divergent",
                        "What makes you different, makes you dangerous",
                        "http://ia.media-imdb.com/images/M/MV5BMTYxMzYwODE4OV5BMl5BanBnXkFtZTgwNDE5MzE2MDE@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=336qJITnDi0")

ten_days = media.Movie("How to Lose a Guy in Ten Days",
                       "One of them is lying. So is the other.",
                       "http://ia.media-imdb.com/images/M/MV5BMjE4NTA1NzExN15BMl5BanBnXkFtZTYwNjc3MjM3._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=EFGr2_cOOTk")

liar_liar = media.Movie("Liar, Liar",
                        "Would I lie to you?",
                        "http://ia.media-imdb.com/images/M/MV5BMjEzMzA3NzgwNF5BMl5BanBnXkFtZTcwNzQ4MDgyMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=DGpS0XgKuLk")

movies = [toy_story, avatar, league_of_their_own, miracle, school_of_rock, hunger_games, divergent, ten_days, liar_liar]

#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(__name__)
print(toy_story.__module__)
