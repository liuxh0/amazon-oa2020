import collections
from typing import Dict, List

def favorite_genres(userSongs: Dict[str, List[str]], songGenres: Dict[str, List[str]]) -> Dict[str, List[str]]:
    song_genre_dict = {}
    for genre, songs in songGenres.items():
        for song in songs:
            song_genre_dict[song] = genre

    ans = {}
    for user, songs in userSongs.items():
        genre_count_dict = {}
        maxcount = 0
        for song in songs:
            genre = song_genre_dict.get(song, None)
            if genre != None:
                genre_count_dict[genre] = genre_count_dict.get(genre, 0) + 1
                maxcount = max(maxcount, genre_count_dict[genre])

        genres = []
        for genre, count in genre_count_dict.items():
            if count == maxcount:
                genres.append(genre)

        ans[user] = genres

    return ans

input = {
    'userSongs': {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"]
    },
    'songGenres': {
        "Rock":    ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno":  ["song2", "song4"],
        "Pop":     ["song5", "song6"],
        "Jazz":    ["song8", "song9"]
    }
}

output = favorite_genres(**input)
print(output)

input = {
    'userSongs': {
        "David": ["song1", "song2"],
        "Emma":  ["song3", "song4"]
    },
    'songGenres': {}
}

output = favorite_genres(**input)
print(output)
