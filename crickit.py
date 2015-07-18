from flask import Flask

app=Flask(__crickit__)

if __crickit__ == "__main__":
	app.run(debug=True)


@app.route('/')
def home_page():
	return homepage.html

@app.route('/chirp')
def chirp():
	# #if number entered, 
	# 	temp = number.
	# elif "get my temp" selected
	# 	temp = get_temp_from_ip()
	#
	# chirp_time = chirp_calc(temp)
	#
	# pass chirp_time to js








# def get_temp_from_ip(ip)
	# get_location(ip) 
	# gets temp from locality via wunderground
	#
	# return temp

# def chirp_calc(temp)
	# uses temp to determine time interval btwn chirps
	#
	# return chirp_time

# def get_location(ip)
	# gets location 
	# returns location in format wunderground can use











