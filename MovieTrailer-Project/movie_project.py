import media
import fresh_tomatoes

#creating instances of the movie class with relevant info
league_of_their_own = media.Movie("A League of Their Own",
                                  "To achieve the incredible you have to attempt the impossible.",
                                  "http://ia.media-imdb.com/images/M/MV5BMTM1NzQ1OTM3NF5BMl5BanBnXkFtZTcwMDAwMjUyMQ@@._V1_SY317_CR1,0,214,317_AL_.jpg",
                                  "https://www.youtube.com/watch?v=WcN392H2jx0",
                                  "Geena Davis & Tom Hanks",
                                  "1 July 1992",
                                  "Hans Zimmer")

miracle = media.Movie("Miracle",
                      "Believe",
                      "http://ia.media-imdb.com/images/M/MV5BMjEyOTk1OTcyNV5BMl5BanBnXkFtZTYwNjMzNDU3._V1_SY317_CR0,0,214,317_AL_.jpg",
                      "https://www.youtube.com/watch?v=v64ofT1rGOw",
                      "Kurt Russel and the 1980 Olympic Team",
                      "6 February 2004",
                      "Mark Isham")

hunger_games = media.Movie("The Hunger Games",
                           "A really real reality show",
                           "http://ia.media-imdb.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_SX214_AL_.jpg",
                           "https://www.youtube.com/watch?v=qoUT7q2iTbQ",
                           "Jennifer Lawrence",
                           "23 March 2012",
                           "James Newton Howard")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4",
                        "Tom Hanks & Tim Allen",
                        "22 November 1995",
                        "Randy Newman")

toy_story_two = media.Movie("Toy Story 2",
                        "The toys are back in town",
                        "http://ia.media-imdb.com/images/M/MV5BMTQ0OTU0NTcyNl5BMl5BanBnXkFtZTcwOTk5Mjc4OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=Lu0sotERXhI",
                        "Tom Hanks & Tim Allen",
                        "24 November 1999",
                        "Randy Newman")

toy_story_three = media.Movie("Toy Story 3",
                        "No toy gets left behind",
                        "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                        "hhttps://www.youtube.com/watch?v=JcpWXaA2qeg",
                        "Tom Hanks & Tim Allen",
                        "18 June 2010",
                        "Randy Newman")

divergent = media.Movie("Divergent",
                        "What makes you different, makes you dangerous",
                        "http://ia.media-imdb.com/images/M/MV5BMTYxMzYwODE4OV5BMl5BanBnXkFtZTgwNDE5MzE2MDE@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=336qJITnDi0",
                        "Shaliene Woodley",
                        "21 March 2014",
                        "Junkie XL")

ten_days = media.Movie("How to Lose a Guy in Ten Days",
                       "One of them is lying. So is the other.",
                       "http://ia.media-imdb.com/images/M/MV5BMjE4NTA1NzExN15BMl5BanBnXkFtZTYwNjc3MjM3._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "https://www.youtube.com/watch?v=EFGr2_cOOTk",
                       "Kate Hudson & Matthew McConnaughay",
                       "7 February 2003",
                       "David Newman")

liar_liar = media.Movie("Liar, Liar",
                        "Would I lie to you?",
                        "http://ia.media-imdb.com/images/M/MV5BMjEzMzA3NzgwNF5BMl5BanBnXkFtZTcwNzQ4MDgyMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=DGpS0XgKuLk",
                        "Jim Carrey",
                        "21 March 1997",
                        "John Debney")

#creating array of movies for fresh_tomatoes.py to iterate over
movies = [league_of_their_own, miracle, hunger_games, toy_story, toy_story_two, toy_story_three, divergent, ten_days, liar_liar]

#calling open page function to build the page dynamically
fresh_tomatoes.open_movies_page(movies)
