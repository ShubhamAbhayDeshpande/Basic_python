class Song:
    """Class to represent the songs 
    
    Attributes:
        title (str): The title of the songs
        artist (str): The artist of the songs
        duration (int): The duration of the songs in seconds. May be zero.
    """
    def __init__(self, title, artist, duration=0):
        """Song init method
        
        Args:
            title (str): The title of the songs
            artist (str): The artist of the songs
            duration (int): The duration of the songs in seconds. 
            duration will default to 0 seconds if it is not specified.
            
        """
        self.title = title
        self.artist = artist
        self.duration = duration

        
class Album:
    """ Class to represent an album, using its tracklist

    Attributes:
    name (str): The name of the album.
    year (int): The year in which the album was released.
    artist (str): The artist responsible for creating the album.
    If the artist is not specified the album was created by various artist.
    
    Methods:
    addSong: used to add new songs in album.
    
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.artist = artist
        if self.artist is None:
            self.artist = "Various Artist"
        else:
            self.artist = artist

        self.tracks = []

    def addSong(self, song, position=None):
        """Adds the song to the tracklist.
        
        Arguments:
        song (Song): The song to be added to the tracklist.
        position (int, optional): The song will be added to the tracklist at the specified position and if the position
        is None then the song will be added at the end of the tracklist.
        
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """this is a basic class to store the artist details and attributes.

    Attributes:
        name(str): The name of the artist
        albums(list[Albums]):  A list of albums in the artist's collections, it is
        not extensive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's album list

    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album(Album): album object to the list album.
            if the album is already present, make sure that it is not added again.
            """
        if album in self.albums:
            print(" The album is already present in the albums list.")
        else:
            self.albums.append(album)

# Write a function outside the class to read the text files in from the file


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))
            if new_artist is None:
                 new_artist = Artist(artist_field)
            elif new_artist.name != artist_field: 
                # we have read details for a new artist
                # store current album in the current artist collection and create new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist=Artist(artist_field)

            # we will do the similar thing that we did above to the new_album.
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we just read a new album for the current artist. 
                # store the current album in the artist collection and create a new album object.
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)
            # create a new song object and add it to the current album's collection.
            new_song = Song(song_field, new_artist)
            new_album.addSong(new_song)

        # After reading the last line in the text file, we will have an artist and album that haven't been stored - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


# The above code will collect the data from the file. And next task will be as the songs are read, each song will be added to the songs object and then it will be added to the album.
# When the current album is already in the albums list, the new song will be added to the artist list and then it will be added to the next.




if __name__ == '__main__':
    artist = load_data()
    print("there are {} artist".format(len(artist)))
