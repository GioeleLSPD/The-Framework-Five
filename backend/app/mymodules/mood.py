import pandas as pd

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')


def find_songs_for_party():
    """
    Filter and return a list of dictionaries with 50 songs suitable
    for a party playlist.

    This function filters the 'spotify_songs' DataFrame based
    on specific audio features
    associated with party-friendly songs. The resulting list
    contains 50 randomly selected
    songs, each represented as a dictionary with 'track_name'
    and 'track_artist' keys.

    Returns:
    list: A list of dictionaries representing 50 party-friendly
    songs with keys 'track_name' and 'track_artist'."""
    features = ((spotify_songs['danceability'].between(0.6, 1.0)) &
                (spotify_songs['energy'].between(0.6, 1.0)) &
                (spotify_songs['loudness'].between(-60, 0)) &
                (spotify_songs['speechiness'].between(0.0, 0.5)) &
                (spotify_songs['instrumentalness'].between(0.0, 0.5)) &
                (spotify_songs['valence'].between(0.5, 1.0)) &
                (spotify_songs['tempo'].between(120, 180)))
    return spotify_songs[features].sample(
        50)[['track_name', 'track_artist']].to_dict(orient='records')


def find_songs_for_chill():
    """
    Filter and return a list of dictionaries with 50 songs suitable
    for a chill playlist.

    This function filters the 'spotify_songs' DataFrame based
    on specific audio features
    associated with chill-friendly songs. The resulting list
    contains 50 randomly selected
    songs, each represented as a dictionary
    with 'track_name' and 'track_artist' keys.

    Returns:
    list: A list of dictionaries representing 50 chill-friendly
    songs with keys 'track_name' and 'track_artist'."""
    features = ((spotify_songs['danceability'] < 0.6) &
                (spotify_songs['energy'] < 0.5) &
                (spotify_songs['speechiness'] < 0.5) &
                (spotify_songs['valence'].between(0.3, 0.7)) &
                (spotify_songs['tempo'].between(70, 110)))
    return spotify_songs[features].sample(
        50)[['track_name', 'track_artist']].to_dict(orient='records')


def find_songs_for_workout():
    """
    Filter and return a list of dictionaries with 50 songs
    suitable for a workout playlist.

    This function filters the 'spotify_songs' DataFrame based
    on specific audio features
    associated with workout-friendly songs. The resulting list
    contains 50 randomly selected
    songs, each represented as a dictionary with 'track_name'
    and 'track_artist' keys.

    Returns:
    list: A list of dictionaries representing 50 workout songs with keys
          'track_name' and 'track_artist'."""
    features = ((spotify_songs['energy'] > 0.6) &
                (spotify_songs['tempo'] > 120) &
                (spotify_songs['danceability'] > 0.5) &
                (spotify_songs['instrumentalness'] < 0.5) &
                (spotify_songs['valence'].between(0.4, 0.8)))
    return spotify_songs[features].sample(
        50)[['track_name', 'track_artist']].to_dict(orient='records')


def find_songs_for_passion():
    """
    Filter and return a list of dictionaries with 50 songs suitable
    for a passion playlist.

    This function filters the 'spotify_songs' DataFrame based
    on specific audio features
    associated with passion-friendly songs. The resulting list
    contains 50 randomly selected songs, each represented
    as a dictionary with 'track_name' and 'track_artist' keys.

    Returns:
    list: A list of dictionaries representing 50 passion songs with keys
          'track_name' and 'track_artist'."""
    features = ((spotify_songs['danceability'].between(0.3, 0.7)) &
                (spotify_songs['energy'].between(0.4, 0.8)) &
                (spotify_songs['loudness'].between(-60, 0)) &
                (spotify_songs['speechiness'].between(0.0, 0.5)) &
                (spotify_songs['instrumentalness'].between(0.0, 0.5)) &
                (spotify_songs['valence'].between(0.5, 1.0)) &
                (spotify_songs['tempo'].between(80, 120)))
    return spotify_songs[features].sample(
        50)[['track_name', 'track_artist']].to_dict(orient='records')


def discover_random_song():
    """
    Retrieve and return a list of dictionaries containing a randomly
    selected song from the Spotify songs dataset.

    This function randomly selects a song from
    the 'spotify_songs' DataFrame and returns the result as a list
    of dictionaries. Each dictionary contains information about
    the selected song, including 'track_name' and 'track_artist'.

    Returns:
    list: A list containing a dictionary with information
    about a randomly selected song.
    The dictionary has keys 'track_name' and 'track_artist'."""
    random_song = spotify_songs.sample(
        1)[['track_name', 'track_artist']].to_dict(orient='records')
    return random_song
