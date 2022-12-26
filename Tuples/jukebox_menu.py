""""The goal is to create a program that will display the name, album, year and the song and the user should be able to select the song that he wants to play. 
If the input is wrong, the program should exit. """

from album import albums

# Until now we were using the numbers to access the variables in a list or tuples. But instead of that we should use the names. And the values assigned to these should be constants
# A constant in the python should be written in all caps. It is just a naming convention. This does not stop us from changing the value of the variable. In python there is no real
# way of permanantly fixing the value of the variable.

SONGS_LIST = 3
SONG_TITLE_INDEX =1
while True:
    print("Please choose your album. (Invalid choice will exit the code)")

    for idx ,(title, artist, year, songs) in enumerate(albums): # Notice that we are passing the tuples in the enumerate and the reason for that is that, numerate will only return
        # two values. One index and the other tuple. So, inorder to unpack the tuple, we are passing 5 values which represent the contents of the tuple.
        print("{}: {}".format(idx+1,title))

        # This is where the user will select the album that he wants to play. And the songs from his choosen albums should be displayed next. 
    choice = int(input())

    if 1<=choice<=len(albums):
        songs_list = albums[choice-1][SONGS_LIST]

    else:
            
        break

    print("album  ",albums[choice-1][0]," has songs:")
    for idx,(song_nr,song_name) in enumerate(songs_list):
        print("{}. {}".format(song_nr, song_name))

    print("Choose a song that you want to play")
    song_choice = int(input())

    if 1<=song_choice<=len(songs_list):
        title = songs_list[song_choice-1][SONG_TITLE_INDEX]
        print("you have choosen to play {} ".format(title))
    else:
        print("Please enter a valid choice for a song and try again.")

