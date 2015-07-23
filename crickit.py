from flask import Flask, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)


app.secret_key = 'crikits_chirping'


@app.route('/')
def index_page():
	return render_template('home_crickit.html')

@app.route('/chirp', methods=['POST'])
def chirp():
	choice = request.form.get('user_choice')
	chirp_time = '0'

	if choice == 'use_user_temperature':
		temp = request.form.get('user_input')
		chirp_time = str(chirp_calc(temp))

	else:
		flash("I haven't made that yet :( ")

	return render_template('chirp_crickit.html', chirp_time=chirp_time)



def chirp_calc(temp):
	# uses temp to determine time interval btwn chirps
	temp = float(temp)
	chirps_per_minute = 40 + 4 * (temp - 50)
	#chirps_per_ms = chirps_per_minute * (1 / 60000)
	chirp_time = 60000 / chirps_per_minute
	return chirp_time






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









