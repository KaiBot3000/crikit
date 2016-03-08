![image](/static/readme_image3.png)
# Crikit

What did we do before thermometers? In the late 1800's two men independently published equations which tied temperature to the frequency of a cricket's chirps. Crikit uses geolocate data and the OpenWeatherMap API to get the temperature at the user's location. It then generates a chirping noise consistent with that temperature. 

Crikit seeks to remind us of what we have lost by distancing ourselves from the natural world. 

### Sidenote:
This was my first solo web app, and I've since refactored it significantly. I left my original code in branch `original-version` for comparison.
Original Version:
- Allowed user to input their own temperature
- Submitted location info through a hacky hidden form
- Had no error handling for API problems (OpenWeather isn't super reliable)
- Constrained the background image so that white text in divs wouldn't be obscured (resulting in a crappy experience for oddly-shaped windows)
- Worked out spacing of divs inside the html using `<br>`s. So many `<br>`s
- I learned about AJAX halfway through, so of course found a way to use it even though I didn't really need it

Refactored Version:
- Snazzy CSS toggle switch built on a checkbox
- Resonsive background image
- Simple error handling for out-of-range temperatures and API errors
- Alert messages to help the user understand what's going on
- Greatly simplified AJAX requests for crickit math (I could easily have done this entirely in the browser, but it was good practice)

Overall this project is overkill in a few ways, but it's a fun project which I learned a lot doing. Enjoy! 


### The Stack
* [Python] - Backend code that manipulates incoming data and serves data to the webpage through a framework.
* [Flask] - Lightweight web framework which also provides support for jinja templating
* [Javascript] - Frontend code which allows for dynamic webpages
* [jQuery] - A Javascript library that simplifies DOM manipulation, including creating event handlers for user interation
* [AJAX] - Gets information from server without reloading the page, allowing for more dynamic pages and faster loading times
* [HTML] - Displays information on the web
* [CSS] - Styles webpages

### Installation

Clone repo:
```sh
$ git clone https://github.com/KaiDalgleish/crikit.git crikit
$ cd crikit
```

Install dependencies:
```sh
$ pip install -r requirements.txt
```

If you want to use your local temperature, get an API Key from [OpenWeather](http://openweathermap.org/appid "API Key") and save it as an 
environmental variable:
```sh
$ export WEATHER_API_KEY=[your app id here]
```

Run the Crikit server:
```sh
$ python crikit.py
```
View in your browser, probably at http://127.0.0.1:5000/ 
