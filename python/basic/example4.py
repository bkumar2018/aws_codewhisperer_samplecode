# Parse a CSV string of songs and return a list of dictionaries
# Fields include artist, album, title and year
# Ignore lines starting with #

def parse_songs(csv_string):
    songs = []
    for line in csv_string.splitlines():
        if line.startswith('#'):
            continue
        fields = line.split(',')
        songs.append({
            'artist': fields[0],
            'album': fields[1],
            'title': fields[2],
            'year': fields[3]
        })
    return songs

# create a string with csv data
# # artist,album,title,year 
csv_string = """Bon Jovi,Crazy,Livin on a Prayer,1987
Bon Jovi,Wnadiya,welcome to the Machine,1991
Metallica,Metallica,Metallica,1885
"""

#call parse_songs and print the result
print(parse_songs(csv_string))
