from flask import Flask, render_template

app=Flask(__name__)




@app.route('/')
def index_page():
	return render_template('home_crickit.html')


	# render_template("templates/base_crickit.html")

# @app.route('/chirp')
# def chirp():
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

if __name__ == "__main__":
	app.run(debug=True)









