import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient():
    def __init__(self):
        cid = '744e625455ed47afa39d44c224c3eb34'
        secret = '8ebc5a9ff200468a9ed79afe217db324'

        #Authentication - without user
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        self.sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    def get_song_title(self, uri: str):
        return self.sp.tracks([uri])
    
    def get_song_titles(self, uris: list[str]):
        return self.sp.tracks(uris)