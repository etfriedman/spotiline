#imports
# from bs4 import BeautifulSoup # awesome library for webscraping, less powerful than scrapy, easier to use.
# import requests # allows us to make requests to websites
# import re # regex (regular expressions)
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import time
import sys
import os
def clear():
    os.system('clear') # clear terminal each time we run
clear()
#Spotify Ubuntu - A spotify player that runs in command line (Name is WIP)
# To use: (TEST THIS, MIGHT ONLY NEED TO BE DONE FOR ME)
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

#What do we want to look at? Look here: https://developer.spotify.com/documentation/general/guides/scopes/
if len(sys.argv) > 1: # make sure something was inputted
    username = sys.argv[1] # set username to what user inputs in command line
else: #if nothing was inputted
    print("Please include your username. Usage: file.py username") # puts the name of the file before username, so userse see: Useage FILENAME username. (really cool)
    sys.exit() #exits run


scope = 'user-read-playback-state'
#Prompts user to agree to let app access spotify, redirects them to ethan.software with a special url
#they paste the URL in command line, which allows the app to access specific info about spotify account
token = util.prompt_for_user_token(username, scope,
client_id='f63792f34788490ab0be9e3c6758c0e1',
client_secret='49a37f9ee22749138d2a989aeb79e8af',
redirect_uri='https://ethan.software')


if token:
    sp = spotipy.Spotify(auth=token)
    current_track = sp.current_user_playing_track()
else:
    print("Wasn't able to get token for", username)

# Fun Code starts!
# --------------------------------------
# Take Track time and how far we are into the track, which is given in ms
# an convert to seconds, then round to the thousandths
track_length = round((((current_track['item']['duration_ms'])/1000)/60),3) # these put the time into seconds, where 1 = 60 seconds
track_progress = round((((current_track['progress_ms'])/1000)/60),3)

def info():
    # Go through the dictionary that is returned,
    # get the current tracks name
    track_name = current_track['item']['name']
    # set these as globals to we can do math to them (I may change this later, and make the info() function only return specified information...? And leave the math and other stuff to outside the function.)
    global track_length
    global track_progress
    # get the numbers after the decimal point, multiply by 60 and you have the number of seconds
    #ex: 2.5 = 2min 30 sec.
    track_length_sec = (track_length % 1)*60 # these take the digits after the decimal, and turn them into seconds (where a while number 1 = 60 seconds)
    track_progress_sec = (track_progress % 1)*60
    #combine!
    track_length = str(int(track_length)) + ':' + str(int(track_length_sec))#Combines the full seconds and the after decimal seconds
    track_progress = str(int(track_progress)) + ':' + str(int(track_progress_sec))

    print(track_name)
    print(track_length)
    print(track_progress)
    # we return the length in ms to give to time.sleep(ms/1000) later on

#def getAlbumCover():
    # track_album_cover = current_track['item']['album']['images'][0]['url']
    # print(track_album_cover)

def update():
     clear()
     info()
     time.sleep(track_length/1000)
     print("Next Song Playing!")
while True:
    update()
