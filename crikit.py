from flask import Flask, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension
import os
import requests

app=Flask(__name__)

app.secret_key = 'crickets_chirping'

weather_key = os.environ['WEATHER_API_KEY']

@app.route('/')
def geolocate():

	return render_template('geolocateplay.html')


@app.route('/crikit')
def index_page():

	return render_template('crikit.html')


@app.route('/chirp') 
def chirp():
	""" Takes in user info, sends back interval of chirps as chirp_time
	"""
	# Gets user info from url
	choice = request.args.get('user_choice')
	temp = request.args.get('user_temp')

	chirp_time = None
	if choice == 'use_user_temp':
		chirp_time = chirp_calc(temp)

	# else (user_choice would be get location)
		# somehow get location from js, 
		# pass latlong to api, get temp
		# use temp to get interval

	# can't pass a float; returns server error :(
	return str(chirp_time) 


def get_temp(lat, lon):
	# uses js geolocate coordinates and api to get temp
	api_url = 'api.openweathermap.org/data/2.5/weather' # ?lat=%s&lon=%s' % (lat, lon)

	location = {}
	location['lat'] = lat
	location['lon'] = lon

	weather_data = response.get(api_url, params=location)

	temp_kelvin = weather_data['main']['main.temp']

	temp_farenheit = (temp_kelvin - 273.15) * 1.8 + 32 

	return temp_farenheit


def chirp_calc(temp):
	"""uses temp to determine time interval btwn chirps"""

	temp = float(temp)
	chirps_per_minute = 40 + 4 * (temp - 50)
	chirp_time = 60000 / chirps_per_minute

	return chirp_time


if __name__ == "__main__":
	app.run(debug=True)









