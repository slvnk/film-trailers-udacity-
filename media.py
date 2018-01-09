import webbrowser

class Film():
	def __init__(self, film_title, film_storyline, poster_image, trailer_youtube):
		self.title = film_title
		self.storyline = film_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
