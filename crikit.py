from flask import Flask, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension
import json

app=Flask(__name__)


app.secret_key = 'crickets_chirping'


@app.route('/crikit')
def index_page():
	#temp = request.args.get('test_info')
	# temp = 'random string'
	return render_template('crikit.html')

@app.route('/chirp') 
def chirp():

	# Gets user info from url
	choice = request.args.get('user_choice')
	temp = request.args.get('user_temp')

	# Checks that above is getting correctly
	print "user chose %s with %s" % (choice, temp)

	# Set to string w/info for check
	test_string = "user chose %s with %s" % (choice, temp)

	return test_string


# def chirp_calc(temp):
# 	# uses temp to determine time interval btwn chirps
# 	temp = float(temp)
# 	chirps_per_minute = 40 + 4 * (temp - 50)
# 	#chirps_per_ms = chirps_per_minute * (1 / 60000)
# 	chirp_time = 60000 / chirps_per_minute
# 	return chirp_time


# def get_temp_from_ip(ip)
	# get_location(ip) 
	# gets temp from locality via wunderground
	#
	# return temp



# def get_location(ip)
	# gets location 
	# returns location in format wunderground can use

if __name__ == "__main__":
	app.run(debug=True)









