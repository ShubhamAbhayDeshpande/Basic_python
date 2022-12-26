"""The plan is to add songs in the albums. We are going to use the data from the resources section of the course. 
This is a lists nested in the tuples."""

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# lets seperate the items from each of the lists.
for artist, albulm, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs in album: {}". format(artist, albulm, year, songs))

#Now, get the third album Budgie, take out the songs as a list and isolate the title of the first song. 
album = albums[2]
songs = album[3]
for sr_no, song in songs:
    if sr_no == 1:
         print(sr_no)
         print(song)

    