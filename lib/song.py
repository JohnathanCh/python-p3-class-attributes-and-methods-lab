import pdb

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.genre_count = Song.genre_counter()
        Song.artist_count = Song.artist_counter()

    @classmethod
    def genre_counter(cls):
        genre_dict = {}
        # pdb.set_trace()
        for genre in Song.genres:
            if genre_dict.get(genre):
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1
        # pdb.set_trace()
        return genre_dict
    
    @classmethod
    def artist_counter(cls):
        artist_dict = {}
        for artist in Song.artists:
            if artist_dict.get(artist):
                artist_dict[artist] += 1
            else:
                artist_dict[artist] = 1
        return artist_dict
        
    
# song = Song("fade", "opris", "pop")
# pdb.set_trace()