class Song:
	def __init__(self, title, artist, length):
		self.title = title
		self.artist = artist
		self.length = length

	def __repr__(self):
		return f"{self.title} by {self.artist} ({self.length})"

def sort_songs(songs, key):
	songs.sort(key=lambda x: getattr(x, key))

playlist = [
	Song("Song A", "Artist B", 3.5),
	Song("Song B", "Artist A", 4.0),
	Song("Song C", "Artist C", 2.0)
]

sort_songs(playlist, "artist")
print(playlist)