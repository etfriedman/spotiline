# Spotiline - Spotify preview from the linux command line!

----
## What does it do?

![Alt Text](https://i.imgur.com/y4bJpdj.gif)
1. shows current album cover (does not switch covers, that is WIP)
2. Shows Title, Author of song.
3. Live progress through song, song length.
----
## Dependencies:
1. viu (https://github.com/atanunq/viu) (You need to have a rust env. on your computer, very easy to do)
2. requests
3. spotipy
----
## Setup/Install:
![Alt Text](https://github.com/etfriedman/command-line-spotify-player/blob/master/setup1.gif)
1. pip install spotipy
2. pip install requests



## Common Errors:
- If you get an error regard NonType, make sure you are playing a song! (otherwise spotify drops your "currently playing" and you cant access it!)
- If you are getting a creds error (export=blahlbahlblah), run the lines in the creds.txt file 1 by 1 in terminal (make sure you have replced each item to your own)
1. if you don't know where to get those, follow this: https://developer.spotify.com/
2. Make a new account, and makea new app.
3. Check your dashboard and click on that app, get the creds there.
4. If you need more help, lookup "Make spotify app"
