#Spotify Ubuntu - A spotify player that runs in command line (Name is WIP)

# ============================================================================

#imports
# import requests # allows us to make requests to websites
# import re # regex (regular expressions)
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import time
import sys
import os
import curses
from convertoascii import showAscii

def clear():
    os.system('clear') # clear terminal each time we run
clear()

# TODO:
# PROGRESS BAR SHOWING THE POPULARITY OF THE SONG!!!!! IT IS x/100 !!!!

#export SPOTIPY_CLIENT_ID='your-spotify-client-id
#export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
#export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
#
#
# If you get an error regard NonType, make sure you are playing a song!!!! otherwise spotify drops your "currently playing" and we cant access it!
#if you are getting a cres error (export=blahlbahlblah), run the lines in the creds.txt file 1 by 1 (make sure you have replced each item to your own)

if len(sys.argv) > 1: # make sure something was inputted
    username = sys.argv[1] # set username to what user inputs in command line
else: #if nothing was inputted
    print("Please include your username. Usage: file.py username") # puts the name of the file before username, so userse see: Useage FILENAME username. (really cool)
    sys.exit() #exits run

shownCover = 0
if shownCover == 0:
    showAscii()
    shownCover + 1


# Fun Code starts!
# --------------------------------------
def update(username):

    # token = util.prompt_for_user_token(username,scope)
    scope = 'user-read-playback-state'
    #Prompts user to agree to let app access spotify, redirects them to ethan.software with a special url
    #they paste the URL in command line, which allows the app to access specific info about spotify account
    token = util.prompt_for_user_token(username,scope)


    if token:
        sp = spotipy.Spotify(auth=token)
        current_track = sp.current_user_playing_track()
    else:
        print("Wasn't able to get token for", username)

    def info(current_track):
        track_length = round((((current_track['item']['duration_ms'])/1000)/60),3) # these put the time into seconds, where 1 = 60 seconds
        track_progress = round((((current_track['progress_ms'])/1000)/60),3)
        # Go through the dictionary that is returned, get the current tracks name
        track_name = current_track['item']['name']
        track_author = current_track['item']['artists'][0]['name']
        # for i in range(len(current_track['item']['artists'])): # Was used to get featured artists, but most artists include that in the title of the song
        #     track_features = []
        #     track_features.append(current_track['item']['artists'][i]['name'])
        # set these as globals to we can do math to them (I may change this later, and make the info() function only return specified information...? And leave the math and other stuff to outside the function.)
        # get the numbers after the decimal point, multiply by 60 and you have the number of seconds
        # ex: 2.5 = 2min 30 sec.
        track_length_sec = (track_length % 1)*60 # these take the digits after the decimal, and turn them into seconds (where a while number 1 = 60 seconds)
        track_progress_sec = (track_progress % 1)*60
        # combine!
        track_length_p = str(int(track_length)) + ':' + str(int(track_length_sec))#Combines the full seconds and the after decimal seconds
        track_progress_p = str(int(track_progress)) + ':' + str(int(track_progress_sec))

        track_album_cover = current_track['item']['album']['images'][2]['url']
        print(track_album_cover)
        print("Currently Playing:",track_name, "By: ",track_author, "Length:",track_length_p, "Progress:",track_progress_p, end='\r')
        # print("Length:",track_length_p)
        # print("Progress:",track_progress_p)

        return track_length, track_progress, track_album_cover


    track_length, track_progress, track_album_cover = info(current_track)
    return track_length, track_progress, track_album_cover

#when downloading the cover art, figure out how to replace it with what is being used.

# Goal, only need to do 1 call per song!! #Back up is to make a call every second, which I assume would be fine, but I want to work around that easy solution
# Goal seems tough, gonna do 1 call a second. While this is inneficient, im going to see what I can do about changing the time
while True:
    #clear()
    update(username)
    time.sleep(1)
















    # gimme some room please!
