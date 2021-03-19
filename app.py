from flask import Flask,render_template, redirect, url_for, request,jsonify
app = Flask(__name__)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
	client_id="d4174aeab1494d20adea989f2d6d1142",
	client_secret="1b1e965662bb4edc9e58e4aa0becc135"))



@app.route('/',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		search_text = request.form['nm']

		results = sp.search(q=search_text, limit=10)
		# for idx, track in enumerate(results['tracks']['items']):
		# 	print(idx, track['name'])
		songlist = results['tracks']['items']
		# artists = []
		# for artist in songinfo['artists']:
		# 	artists.append(artist['name'])
		# artists_string = ", ".join(artists)

		return render_template('spotify-flask.html', tracks=songlist)
		# return jsonify(results)
	else:
		user = request.args.get('nm')
		return render_template('spotify-flask.html')





if __name__ == '__main__':
	app.run(debug = True)