from flask import Flask, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)


app.secret_key = 'crickits_chirping'


@app.route('/crickit')
def index_page():
	#temp = request.args.get('test_info')
	# temp = 'random string'
	return render_template('base_crickit.html')

@app.route('/chirp') 
def chirp():
	test_string = 'random string'
	# test_info = request.args.get('test_info')
	# print test_info
	# choice = request.args.get('user_choice')
	# chirp_time = '0'

	# if choice == 'use_user_temperature':
	# 	temp = request.args.get('user_input')
	# 	chirp_time = str(chirp_calc(temp))

	# else:
	# 	flash("I haven't made that yet :( ")

	# return render_template('base_crickit.html', chirp_time=chirp_time)

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









