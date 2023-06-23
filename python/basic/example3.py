# Parse a CSV string of songs and return a list of dictionaries
# Fields include artist, album, title and year
# Ignore lines starting with #

def parse_songs(csv_string):
    songs = []
    for line in csv_string.splitlines():
        if not line.startswith("#"):
            artist, album, title, year = line.split(",")
            songs.append({"artist": artist, "album": album, "title": title, "year": year})
    return songs

