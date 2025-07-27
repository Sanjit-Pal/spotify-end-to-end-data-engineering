import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import boto3
from datetime import datetime

def lambda_handler(event, context):
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    # My Playlist 7
    playlist_link = 'https://open.spotify.com/playlist/799Oyux2M6UCzMdGIcVI71'
    playlist_URI = playlist_link.split('/')[-1]

    spotify_data = spotify.playlist_tracks(playlist_URI)
    #print(spotify_data)

    file_name = 'spotify_raw_' + datetime.now().strftime('%Y%m%d%H%M%S')

    client = boto3.client('s3')
    client.put_object(Bucket='spotify-etl-project-sanjit',
                    Key='raw_data/to_processed/' + file_name + '.json',
                    Body=json.dumps(spotify_data)
            )
