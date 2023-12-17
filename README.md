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

 4.⁠ ⁠Use the form on the frontend to query playlists and information  from the backend.

# **What does Moody Tunes do?** 

Feature 1: The call to action for users is selecting their current mood from the available ones in the search bar. We have five possible moods which are: Chill, workout, passion, party and random. Our software will then generate a music playlist accordingly by selecting them from a 30,000 database of songs. Each playlist has its own ranges of values over 7 features, danceability, energy, loudness, speechless, instrumentalness, valence and tempo.

Our goal was to allow everyone to find the correct song based on their mood. 

Feature 2: By analysing our dataset we were able to outline its characteristics. We selected: song number for each genre, number of songs of each artist, total number of songs present in the dataset. 

Feature 3: Artits present in the dataset organised in alphabetical order. 

Feature 4: The user can access to the function "discover", where he can obtain as an output a completely random song from our csv. The aim of this part of our project was allowing users to discover new tunes the may like and deepen their knowledge of music. 

# **We ask the user to:** 

Feature 1: make the system generate the perfect playlist based on the mood of the user 

Feature 2: know all the characteristics of the generated playlist 

Feature 3: click on the initial letter of an artist in order to know the number of songs of the artist presnet in our csv. 

Feature 4: obtain a random song to discover 

# **Dataset**

We selected one database, named spotify\_songs, from kaggle. As we needed a large pool of songs in order for our project to work we selected the database 30,000 Spotify Songs. The chosen CSV file is from Spotify API.


