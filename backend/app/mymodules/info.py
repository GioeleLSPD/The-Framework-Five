import pandas as pd
from itertools import islice

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')


def genre_popularity():
    """
    Calculate and return the average popularity of subgenres based on Spotify songs.

    This function groups songs by their 'playlist_subgenre' and calculates the
    average popularity of tracks within each subgenre. The result is a dictionary
    where subgenres are keys and their corresponding average popularity is the value.

    Returns:
    dict: A dictionary with subgenres as keys and their average popularity as values."""
    genre_popularity = spotify_songs.groupby('playlist_subgenre')[
        'track_popularity'].mean().sort_values(ascending=False)
    genre_popularity_dict = genre_popularity.to_dict()
    return genre_popularity_dict


def get_song_count_by_genre():
    """
    Calculate and return the count of songs for each subgenre based on Spotify songs.

    This function counts the number of songs in each 'playlist_subgenre' category
    within the 'spotify_songs' DataFrame and returns the result as a dictionary.

    Returns:
    dict: A dictionary with subgenres as keys and the count of songs as values."""
    subgenre_counts = spotify_songs['playlist_subgenre'].value_counts(
    ).to_dict()
    return subgenre_counts


def artist_songs():
    """
    Calculate and return the count of songs for each artist based on Spotify songs.

    This function counts the number of songs for each unique artist in the 'spotify_songs'
    DataFrame and returns the result as a dictionary. The dictionary is sorted alphabetically
    by artist names.

    Returns:
    dict: A dictionary with artists as keys and their corresponding song counts as values."""
    artist_counts = spotify_songs['track_artist'].value_counts().to_dict()
    sorted_artist_counts = dict(sorted(artist_counts.items()))
    return (sorted_artist_counts)


def count_songs():
    """
    Calculate and return the total count of songs in the Spotify songs dataset.

    This function computes the total number of songs in the 'spotify_songs' DataFrame
    and returns the result as a single integer representing the count.

    Returns:
    int: Total count of songs in the dataset."""
    total_songs_count = len(spotify_songs)
    return total_songs_count

def get_songs_by_artist(artist_name):
    """
    Retrieve and return a list of songs by a specific artist from the Spotify songs dataset.

    This function filters the 'spotify_songs' DataFrame based on the provided 'artist_name'
    and returns a list of song names associated with the specified artist.

    Args:
    artist_name (str): The name of the artist for whom the song list is to be retrieved.

    Returns:
    list: A list of song names by the specified artist."""
    artist_songs = spotify_songs[spotify_songs['track_artist'] == artist_name]
    songs_list = artist_songs['track_name'].tolist()
    return songs_list