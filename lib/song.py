class Song:
    # Class attribute to keep track of the number of songs created
    count = 0

    # Class attribute to store all genres
    genres = []

    # Class attribute to store all artists
    artists = []

    # Class attribute to store genre counts
    genre_count = {}

    # Class attribute to store artist counts
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the class attribute count when a new song is created
        Song.add_song_to_count()

        # Add the genre of the song to the class attribute genres
        Song.add_to_genres(genre)

        # Add the artist of the song to the class attribute artists
        Song.add_to_artists(artist)

        # Update genre count
        Song.add_to_genre_count(genre)

        # Update artist count
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Class method to increment the count of songs
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Class method to add new genres to the list (control for duplicates)
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Class method to add new artists to the list (control for duplicates)
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Class method to update genre count
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Class method to update artist count
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
