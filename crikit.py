from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import os
import requests
import json

app=Flask(__name__)
app.secret_key = "crickets_chirping"
weather_key = os.environ["WEATHER_API_KEY"]


@app.route("/crikit")
def index_page():

	return render_template("crikit.html")


@app.route("/chirp") 
def chirp():
	"Takes in user info, sends back interval of chirps as chirp_time"

	lat = request.args.get("latitude")
	lon = request.args.get("longitude")
	chirp_time = None
	temperature = get_temp(lat, lon)

	# check if crickit would be chirping
	if temperature > 40.0 and temperature < 85.0:
		chirp_time = chirp_calc(temperature)
	else:
		chirp_time = 0

	return str(chirp_time) 


def get_temp(lat, lon):
	"Takes in coordinates, makes api call to get temperature and return in Farenheit"

	# default values for testing
	# lat = 37.7833
	# lon = 122.4167
	api_url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s" % (lat, 
																						 lon,
																						 weather_key)
	# API has intermittent failures, so...
	try:
		weather_response = requests.get(api_url)
		weather_data = json.loads(weather_response.content)
		print weather_data
		temp_kelvin = weather_data["main"]["temp"]
		# converts kelvin to farenheit
		temp_farenheit = (temp_kelvin - 273.15) * 1.8 + 32
	except:
		return 0

	return temp_farenheit


def chirp_calc(temp):
	"Takes float temperature, returns chirp interval"

	chirps_per_minute = 40 + 4 * (temp - 50)
	chirp_time = 60000 / chirps_per_minute

	return chirp_time


if __name__ == "__main__":
	app.run(debug=True)
