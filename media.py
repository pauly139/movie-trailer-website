import webbrowser

class Video():
    """ Parent Class to hold video title and duration """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration

    def show_info(self):
        print "Title : " + self.title
        print "Duration : " + str(self.duration) + " min"

class Movie(Video):
    """ Movie class which inerits from class Video to hold movie specific information"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_duration, gross_income):
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.gross_income = gross_income

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

