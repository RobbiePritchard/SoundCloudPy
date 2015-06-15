import soundcloud
import urllib
import getpass



YOUR_CLIENT_ID = '221882a5a09f8e4a4f44287518a92fc6'
YOUR_CLIENT_SECRET = '2da2b1d8246c50aeeb391a1c6c4581df'
print
YOUR_USERNAME = raw_input('Username: ')
YOUR_PASSWORD = getpass.getpass('Password: ')
try:
	client = soundcloud.Client(client_id=YOUR_CLIENT_ID,
                           client_secret=YOUR_CLIENT_SECRET,
                           username=YOUR_USERNAME,
                           password=YOUR_PASSWORD)
except:
	print('Password and/or Username Incorrect')


print ('\nlogged in as {}'.format(client.get('/me').username))
print ('\nDownloading Yo Tunes\n')

#currently takes only the first playlist
#TODO add playlist choice
playlist = client.get('/me/playlists/')[0]
count = 0
for track in playlist.tracks:
	count += 1
	stream_url = client.get(track['stream_url'], allow_redirects=False)
	print track['title']
	filename =  track['title'] + ".mp3"
	print('{} of {}\n'.format(count,len(playlist.tracks)))
	urllib.urlretrieve(stream_url.location, filename)
print('\nDone')

