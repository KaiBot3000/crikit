from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import os
import requests
import json

app=Flask(__name__)

app.secret_key = 'crickets_chirping'

# API doesn't actually require key
# weather_key = os.environ['WEATHER_API_KEY']


@app.route('/crikit')
def index_page():

	return render_template('crikit.html')


@app.route('/chirp') 
def chirp():
	'''Takes in user info, sends back interval of chirps as chirp_time'''

	# Gets user info from url
	choice = request.args.get('user_choice')
	temp = request.args.get('user_temp')
	lat = request.args.get('lat')
	lon = request.args.get('lon')

	chirp_time = None

	if choice == 'use_user_temp':
		temperature = temp

	else: #(user_choice would be get location)
		temperature = get_temp(lat, lon)

	# check if crikit would be chirping
	if int(temperature) in range(55, 100):
		chirp_time = chirp_calc(temperature)
	else:
		chirp_time = 0

	print chirp_time
	# can't pass a float; returns server error :(
	return str(chirp_time) 


def get_temp(lat, lon):
	'''Takes in coordinates, makes api call to get temperature and return in Farenheit'''

	api_url = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s' % (lat, lon)

	weather_response = requests.get(api_url)
	weather_data = json.loads(weather_response.content)

	temp_kelvin = weather_data['main']['temp']

	# converts kelvin to farenheit
	temp_farenheit = (temp_kelvin - 273.15) * 1.8 + 32 

	print temp_farenheit
	return temp_farenheit


def chirp_calc(temp):
	'''Takes temperature, returns chirp interval'''

	temp = float(temp)
	chirps_per_minute = 40 + 4 * (temp - 50)
	chirp_time = 60000 / chirps_per_minute

	return chirp_time


if __name__ == '__main__':
	app.run(debug=True)









