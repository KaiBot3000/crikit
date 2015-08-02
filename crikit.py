from flask import Flask, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)

app.secret_key = 'crickets_chirping'


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

	# Checks that above is getting correctly
	print "user chose %s with %s" % (choice, temp)

	# Set to string w/info for check
	test_string = "user chose %s with %s" % (choice, temp)

	chirp_time = None
	if choice == "use_user_temp":
		chirp_time = chirp_calc(temp)

	# else (user_choice would be get location)
		# somehow get location from js, 
		# pass latlong to api, get temp
		# use temp to get interval

	return "chirp time: %s" % chirp_time


# def get_temp(lat, long):
# 	uses js geolocate coordinates and api to get temp

# 	return temp

def chirp_calc(temp):
	"""uses temp to determine time interval btwn chirps"""

	temp = float(temp)
	chirps_per_minute = 40 + 4 * (temp - 50)
	chirp_time = 60000 / chirps_per_minute

	return chirp_time


if __name__ == "__main__":
	app.run(debug=True)









