import webbrowser

class Movie():
    """This class provides a way to store movie related information."""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__ (self,movie_title,movie_storyline,poster_image,trailer_youtube,movie_star,release_date,soundtrack_composer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_star = movie_star
        self.release_date = release_date
        self.soundtrack_composer = soundtrack_composer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
