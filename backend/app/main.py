"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd


from .mymodules.mood import (find_songs_for_party, find_songs_for_chill,
                             find_songs_for_workout, find_songs_for_passion,
                             discover_random_song)

from .mymodules.info import (count_songs, artist_songs,
                             get_song_count_by_genre, genre_popularity,
                             get_songs_by_artist)

app = FastAPI()

mood_functions = {
    "party": find_songs_for_party,
    "chill": find_songs_for_chill,
    "workout": find_songs_for_workout,
    "passion": find_songs_for_passion,
    "discover": discover_random_song
}


@app.get('/mood/{mood_name}')
def get_songs_by_mood(mood_name: str):
    """
    Retrieve a list of songs matching a specified mood.

    This endpoint is designed to return a list of songs
    associated with a specific mood.
    The mood is specified in the 'mood_name' path parameter.

    Args:
    mood_name (str): The name of the mood for which songs are to be retrieved.

    Returns:
    Depends on the specific implementation of mood functions."""
    if mood_name in mood_functions:
        return mood_functions[mood_name]()
    else:
        raise HTTPException(status_code=404, detail="Mood not found")


info_functions = {
    "c_songs": count_songs,
    "a_songs": artist_songs,
    "genre": get_song_count_by_genre,
    "p_genre": genre_popularity
}


@app.get('/info/{info_g}')
def get_info(info_g: str):
    """
    Retrieve specific music-related information based on the given category.

    This endpoint is designed to retrieve and return music-related
    information based on the specified category.
    The category is provided in the 'info_g' path parameter.

    Args:
    info_g (str): The category of music-related information to be retrieved.

    Returns:
    (Depends on the specific implementation of info functions)"""
    if info_g in info_functions:
        result = info_functions[info_g]()
        return result
    else:
        raise HTTPException(status_code=404, detail="Information not found")


@app.get('/songs/{artist_name}')
def artist_song_list(artist_name: str):
    """
    Retrieve the list of songs for a given artist.

    This endpoint is designed to retrieve and return a list
    of songs by a specific artist.
    The artist name is provided in the 'artist_name' path parameter.

    Args:
    artist_name (str): The name of the artist for whom the song
    list is to be retrieved.

    Returns:
    list: A list of dictionaries representing songs by the specified artist.
          Each dictionary contains information about a song,
          including 'track_name' and 'track_artist'."""
    songs_list = get_songs_by_artist(artist_name)
    if songs_list:
        return songs_list
    else:
        raise HTTPException(status_code=404, detail="Artist not found")
