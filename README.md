![image](/static/readme_image.png)
# Crikit

What did we do before thermometers? In the late 1800's two men independently published equations which tied temperature to the frequency of a crickit's chirps. Crikit works in two ways: it either uses a temperature the user provides, or uses geolocate data and the OpenWeatherMap API to get the temperature at the user's location. It then generates a chirping noise consistent with that temperature. 

Crikit seeks to remind us of what we have lost by distancing ourselves from the natural world. 

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

Run the Crikit server:
```sh
$ python crikit.py
```
View in your browser, probably at http://127.0.0.1:5000/ 
