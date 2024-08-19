import os
from bs4 import BeautifulSoup
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth

#Scraping the Billboard  Website to get 100 of the hottest song on specific day and creating a playlist on spotify
# using the module spotipy

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

answer = input("Which year do you want to? Type the date in this format YYYY-MM-DD: ")
URL_WEBSITE = f"https://www.billboard.com/charts/hot-100/{answer}/"

response = requests.get(URL_WEBSITE).text
soup = BeautifulSoup(response, "html.parser")

all_div_with_songs = soup.select("li ul li h3")
all_songs_list = [song.text.strip("\n\t") for song in all_div_with_songs]


def playlist_exist(user_input):
    playlist_already_exist = False
    for x in range(len(sp.current_user_playlists()['items'])):
        playlist = sp.current_user_playlists()['items'][x]['name']
        if playlist == f"{user_input} Billboard 100":
            playlist_already_exist = True
    return playlist_already_exist


auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri="http://example.com", scope="playlist-modify-private", show_dialog=True,
                            cache_path="token.txt", username="andy.vargas.noesi")
sp = spotipy.Spotify(auth_manager=auth_manager)
user_id = sp.current_user()["id"]

# empty list where songs uris would be stored.
songs_uris = []

for song in all_songs_list:
    result = sp.search(q=song, type="track")
    if int(result['tracks']['items'][0]['album']['release_date'].split("-")[0]) <= int(answer.split("-")[0]):
        try:
            artist = result['tracks']['items'][0]['album']['artists'][0]['name']
            songs_uris.append(result['tracks']['items'][0]['uri'])
            print(f"adding {song}")
        except IndexError:
            print("song does not exist")

if not playlist_exist(answer):
    playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{answer} Billboard 100", public=False,
                                       collaborative=False, description=f"Back to {answer}")
else:
    print("Playlist already exist")

sp.user_playlist_add_tracks(user=f"{user_id}", playlist_id=playlist['id'], tracks=songs_uris)
