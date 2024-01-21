"""
Frontend module for the Flask application.

This module defines a simple Flask application
that serves as the frontend for the project.
"""

from flask import Flask, render_template, request
import requests  # Import the requests library to make HTTP requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# Replace with a secure secret key

# Configuration for the FastAPI backend URL
FASTAPI_BACKEND_HOST = 'http://backend'
# Replace with the actual URL of your FastAPI backend
BACKEND_URL = f'{FASTAPI_BACKEND_HOST}/query/'


class MoodForm(FlaskForm):
    mood = SelectField('Choose a Mood', choices=[
        ('chill', 'Chill'),
        ('workout', 'Workout'),
        ('passion', 'Passion'),
        ('party', 'Party'),
        ('discover', 'Discover')
    ])


@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    """
    # Fetch the date from the backend
    date_from_backend = fetch_date_from_backend()
    return render_template('index.html', date_from_backend=date_from_backend)


def fetch_date_from_backend():
    """
    Function to fetch the current date from the backend.

    Returns:
        str: Current date in ISO format.
    """
    backend_url = 'http://backend/get-date'
    # Adjust the URL based on your backend configuration
    try:
        response = requests.get(backend_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get('date', 'Date not available')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching date from backend: {e}")
        return 'Date not available'


@app.route('/mood', methods=['GET', 'POST'])
def mood():
    """
    Render the mood page.

    This route handler renders the mood page, allowing users to select
    a mood using a form. If the form is validated upon 
    submission, it retrieves a playlist based
    on the selected mood from the
    FastAPI backend and displays the playlist.

    Returns:
        str: Rendered HTML content for the mood page."""
    form = MoodForm()
    error_message = None
    songs = None

    if form.validate_on_submit():
        selected_mood = form.mood.data
        fastapi_url = f'{FASTAPI_BACKEND_HOST}/mood/{selected_mood}'
        response = requests.get(fastapi_url)
        if response.status_code == 200:
            songs = response.json()
        else:
            error_message = f'Error: Failed to retrive playlist for {selected_mood} from FastAPI Backend'

    return render_template('mood.html', form=form, songs=songs,
                           error_message=error_message)


@app.route('/info')
def info():
    """
    Fetches and displays selected types of information from
    the FastAPI backend.

    This route handler fetches information types 'c_songs',
    'genre', and 'p_genre' from the FastAPI backend. It renders 'info.html'
    with the retrieved data or an error message
    if the data cannot be fetched.

    Returns:
        str: Rendered HTML content for the information page."""
    error_message = None
    data = {}

    info_list = ["c_songs", "genre", "p_genre"]

    backend_url = f'{FASTAPI_BACKEND_HOST}/info/'

    for info in info_list:
        response = requests.get(backend_url + info)
        if response.status_code == 200:
            data[info] = response.json()
        else:
            error_message = f"Error: Unable to retrieve {info} from the backend."

    return render_template('info.html', data=data, error_message=error_message)


@app.route('/artists', methods=['GET'])
def get_artists_by_letter():
    """
    Retrieves a list of artists from the FastAPI backend
    filtered by the starting letter provided in the query
    parameter.

    This route handler retrieves a list of artists from the 
    FastAPI backend and filters them based on the starting
    letter provided in the 'letter' query parameter.
    It renders 'artists.html' with the filtered list of
    artists or an error message if no artists are found.

    Returns:
        str: Rendered HTML content for the artists page."""
    letter = request.args.get('letter', '#')
    letter = request.args.get('letter', '#')
    fastapi_url = f'{FASTAPI_BACKEND_HOST}/info/a_songs'
    response = requests.get(fastapi_url)
    if response.status_code == 200:
        all_artists = response.json()
        filtered_artists = {
            artist: count for artist, count in all_artists.items()
            if artist.startswith(letter) or
            (letter == "#" and not artist[0].isalpha())
        }
        return render_template('artists.html',
                               artists=filtered_artists,
                               selected_letter=letter)
    else:
        return render_template('artists.html', artists={},
                               selected_letter=letter,
                               error="Artists not found")

@app.route('/artist_songs/<artist_name>')
def artist_songs_page(artist_name):
    """
    Renders a page with a list of songs for a specific artist.

    This route handler retrieves a list of songs for a
    specific artist from the FastAPI backend
    and renders 'songs_for_artist.html' with the artist's
    name and the list of songs or an error message if no songs are found.

    Args:
        artist_name (str): The name of the artist for whom
        the song list is to be displayed.

    Returns:
        str: Rendered HTML content for the artist's songs page."""
    fastapi_url = f'{FASTAPI_BACKEND_HOST}/songs/{artist_name}'
    response = requests.get(fastapi_url)
    if response.status_code == 200:
        songs = response.json()
        return render_template('songs_for_artist.html', artist=artist_name, songs=songs)
    else:
        return render_template('songs_for_artist.html', artist=artist_name, songs=[], error="Songs not found")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
