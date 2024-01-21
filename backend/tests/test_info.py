import os
import sys
import pandas as pd
from fastapi.testclient import TestClient


sys.path.insert(0, os.path.abspath(os.path.join(
                os.path.dirname(__file__), '..')))

from app.main import app
from app.mymodules.info import (genre_popularity, get_song_count_by_genre,
                                count_songs, artist_songs, get_songs_by_artist)

spotify_songs = pd.read_csv('/app/app/spotify_songs.csv')


client = TestClient(app)


def test_genre_popularity():
    """Test the genre_popularity function to ensure it returns a dictionary
    with genres as keys and floats as values, with popularity scores between
    0 and 100."""
    result = genre_popularity()
    assert isinstance(result, dict)
    for genre, popularity in result.items():
        assert isinstance(popularity, float)
        assert 0 <= popularity <= 100


def test_get_song_count_by_genre():
    """Test the get_song_count_by_genre function to ensure it returns a
    dictionary with subgenres as keys and integers as values, with the
    sum of values matching the total number of songs in the dataset."""
    result = get_song_count_by_genre()
    assert isinstance(result, dict)
    assert sum(result.values()) == len(spotify_songs)


def test_count_songs():
    """Test the count_songs function to ensure it returns an integer
    count of all songs in the dataset."""
    result = count_songs()
    assert isinstance(result, int)
    assert result == len(spotify_songs)


def test_artist_songs():
    """Test the artist_songs function to ensure it returns a
    dictionary with artists as keys and integers as values,
    sorted by artist name."""
    result = artist_songs()
    assert isinstance(result, dict)
    assert list(result.keys()) == sorted(result.keys())
    for artist, count in result.items():
        assert isinstance(count, int)
        assert count == (spotify_songs['track_artist'] == artist).sum()


def test_get_info_invalid_category():
    """Test the get_info function with an invalid
    category to ensure it raises a 404 error."""
    response = client.get("/info/invalid_category")
    assert response.status_code == 404
    assert response.json() == {"detail": "Information not found"}


def test_get_info_valid_category():
    """Test the get_info function with a valid
    category to ensure it returns the correct response."""
    valid_category = "genre"  # Assuming "genre" is a valid category in info_functions
    response = client.get(f"/info/{valid_category}")
    assert response.status_code == 200
    # Further assertions can be made based on the expected response format and content


def test_artist_song_list_valid_artist():
    """Test artist_song_list with a valid artist name."""
    valid_artist = 'Avicii'
    response = client.get(f"/songs/{valid_artist}")
    assert response.status_code == 200
    result = get_songs_by_artist(valid_artist)
    assert isinstance(result, list)
    for song in result:
        assert song in spotify_songs[spotify_songs['track_artist'] == valid_artist]['track_name'].tolist()
    # Additional assertions based on the expected output
    

def test_artist_song_list_invalid_artist():
    """Test artist_song_list with an invalid artist name."""
    invalid_artist = 'Nonexistent Artist'
    response = client.get(f"/songs/{invalid_artist}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Artist not found"}
