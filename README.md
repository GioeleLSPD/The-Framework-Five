# **README** 

***Group: The Framework Five***

**Members:** 

- Gioele Squizzato, 889040; 

- John Molfino, 889965; 

- Matilde Farinelli, 888897; 

- Umberto Bolzoni, 891140; 

- Sofia Alajmo, 888473.


# **Project Name:** Moody Tunes 
The project's frontend aims help everyone to find teh percfect tune for every situation, whether you want to dance or to chill. 

## Architecture 
The project follows a simple client-server architecture:

 1.⁠ ⁠*Frontend (Flask):*
   - Represents the user interface or client side.
   - Built with Flask, a lightweight web framework for Python.
   - Responsible for rendering web pages and user interaction, including the form for querying the backend.

 2.⁠ ⁠*Backend (FastAPI):*
   - Represents the server or backend of the application.
   - Built with FastAPI, a modern web framework for building APIs with Python.
   - Handles requests from the frontend, including querying playlists, information and providing the current mood.

 3.⁠ ⁠*Docker Compose:*
   - Orchestrates the deployment of both frontend and backend as separate containers.
   - Ensures seamless communication between frontend and backend containers.
   - Simplifies the deployment and management of the entire application.

## Project Structure

•⁠  ⁠⁠ `backend/` : FastAPI backend implementation.
- Dockerfile: Dockerfile for building the backend image.
- *main.py*: Main backend application file.
- *mood.py*: defines the characteristics requirement of each song to assign it to a specific mood
- *info.py*: define the popularity of each music genre and songs per genre, number of songs attributable to a single artist, overall songs' number thorugh functions.
- *spotify_songs.csv*
- tests: test_mood.py, test_info.py, used to test our backend functions. 
- requirements.txt: List of Python dependencies for the backend.
    
•⁠  ⁠⁠ `frontend/` ⁠: Flask frontend implementation.
- Dockerfile: Dockerfile for building the frontend image.
- static/: Folder for static files (CSS, JavaScript, etc.).
- templates/: Folder for HTML templates (base, index, internal).
- main.py: Main frontend application file.
- requirements.txt: List of Python dependencies for the frontend.
    
•⁠  ⁠⁠ `docker-compose.yml` ⁠: Docker Compose configuration for running both frontend and backend. 

## Prerequisites
- Docker
- Visual Studio Code
- CSV: can find them on GitHub

## Usage 

 1.⁠ ⁠Clone the repository and navigate in the directory:

   ```bash
    git clone https://github.com/GioeleLSPD/The-Framework-Five
    cd The-Framework-Five
   ```

 2.⁠ ⁠Build and run the Docker containers:

  ```bash
    docker-compose up --build
  ```

This will start both the frontend and backend containers.
    
	⁠*NOTE:* Uncomment the lines in the Dockerfiles that follow the section labeled ⁠ Command to run the application ⁠ and comment out the ones labeled ⁠ Command to keep the container running ⁠. This will allow you to access the backend and frontend, as described in Point 3.

 3.⁠ ⁠Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the ⁠ frontend ⁠ and [http://localhost:8081](http://localhost:8081) to access the ⁠ backend ⁠.

 4.⁠ ⁠Use the form on the frontend to query playlists and information from the backend.

# **What does Moody Tunes do?** 

Feature 1: The call to action for users is selecting their current mood from the available ones in the search bar. We have five possible moods which are: Chill, workout, passion, party and random. Our software will then generate a music playlist accordingly by selecting them from a 30,000 database of songs. Each playlist has its own ranges of values over 7 features, danceability, energy, loudness, speechless, instrumentalness, valence and tempo.

Our goal was to allow everyone to find the correct song based on their mood. 

Feature 2: By analysing our dataset we were able to outline its characteristics. We selected: song number for each genre, number of songs of each artist, total number of songs present in the dataset. 

Feature 3: Artits present in the dataset organised in alphabetical order. 

Feature 4: The user can access to the function "discover", where he can obtain as an output a completely random song from our csv. The aim of this part of our project was allowing users to discover new tunes the may like and deepen their knowledge of music. 

Feature 5: The users can access to all teh songs of a specific artist by clicking on the number of songs present in the dataset. Doing so will lead to a new page

# **We ask the user to:** 

Feature 1: make the system generate the perfect playlist based on the mood of the user 

Feature 2: know all the characteristics of the generated playlist 

Feature 3: click on the initial letter of an artist in order to know the number of songs of an artist present in our csv.

Feature 4: click on the function discovery and find out brand new songs 

Feature 5: by clicking on the number of songs present in our dataset the users will visualize all the songs 

# **Dataset**

We selected one database, named spotify\_songs, from kaggle. As we needed a large pool of songs in order for our project to work we selected the database 30,000 Spotify Songs. The chosen CSV file is from Spotify API.

This is the link to the dataset we selected from kaggle: https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs

The dataset contains all the following information:

- **track_id character** Song unique ID
- **track_name character** Song Name
- **track_artist character** Song Artist
- **track_popularity double** Song Popularity (0-100) where higher is better
- **track_album_id character** Album unique ID
- **track_album_name character** Song album name
- **track_album_release_date** character Date when album released
- **playlist_name character** Name of playlist
- **playlist_id character** Playlist ID
- **playlist_genre character** Playlist genre
- **playlist_subgenre character** Playlist subgenre
- **Danceability**: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- **Energy**: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- **key**: double The estimated overall key of the track. Integers map to pitches using standard Pitch Class notation . E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
- **loudness**: double The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
- **mode**: double Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
- **Speechiness**: double Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
- **acousticness**: double A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
instrumentalness: double Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
- **liveness**: double Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
- **valence**: double A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
- **tempo**: double The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
- **duration_ms**: double Duration of song in milliseconds

Though in order to complete our project we selected only the ones we believed were relevant, which are: 

- track_name
- ⁠⁠track_artists
- ⁠playlist_subgenre
- Danceability
- energy
- ⁠loudness
- ⁠⁠speechiness
- instrumentalness
- ⁠⁠valence
- tempo
  
The selected dataset was ready to use, we did not modify it in anyway, nor in imputation or cleaning. We download it from the link above and we procede by uploading it. 


