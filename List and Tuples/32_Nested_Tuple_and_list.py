albums=[
("Dangerous","Micheal Jackson",1991,
[
    (1,"Jan"),
    (2,"Who is it"),
    (3,"Dangerous"),
]),
("Unapologetic","Rihanna",2012,
[
    (1,"Diamond"),
    (2,"Nobody's Business"),
    (3,"Jump"),
]),
("East Atlanta Love Letter","6black",2018,
[
    (1,"Switch"),
    (2,"Seasons"),
    (3,"Sorry"),
]),

("Beerbongs & Bentleys","Post Malone",2018,
[
    (1,"Rockstar"),
    (2,"Better Now"),
    (3,"Psycho"),
]),

]

for name,artist,year,songs in albums:
    print(f"The Album: {name}, Artist: {artist},Year: {year},Songs; {songs}")
    print()

album=albums[3]
songs=albums[3]
print(songs)

print()

that_song=songs[3]
print(that_song)

only_that_song=that_song[1]
print(only_that_song)

print()

print(albums[3][3][0][1])