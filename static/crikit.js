// Makes js wait until DOM is loaded to execute (allows sound to load)
// function closed/finished at end of script
//s$(document).ready(function(){

// assigns variables to elements 
// TODO: switch to just jQuery (hadn"t learned when this project was started)
// divs
var start_chirp = document.getElementById("start_chirp_div");
// var start_button = document.getElementById("start_chirping_button");

var stop_chirp = document.getElementById("stop_chirp_div");
// var stop_button = document.getElementById("stop_chirping_button");

// var geo_status = document.getElementById("geolocate_status");
var use_location = document.getElementById("use_location");
// var lat_spot = document.getElementById("lat_form");
// var lon_spot = document.getElementById("lon_form");

var alerts = document.getElementById("alerts");

// needed for sound.js
var soundPath = "static/crikit_chirp.mp3"
var soundID = "Chirp";
// needed to set clearInterval()
var chirping;

// sets initial state for site
$(start_chirp).show();
$(stop_chirp).hide();
// $(use_location).hide();

// Calls appropriate function for button clicks.
$("#start_chirping_button").on("click", startChirping);
$("#stop_chirping_button").on("click", stopChirping);


function loadSound() {
    // Loads sound for chirp
    createjs.Sound.registerSound(soundPath, soundID);
};

function getLocation() {
    if ("geolocation" in navigator) {
            /* geolocation is available */
        navigator.geolocation.getCurrentPosition(function(position) {
            // this sometimes takes a while to complete
            var lat = position.coords.latitude;
            var lon = position.coords.longitude;
            $("#lat_form").val(lat);
            $("#lon_form").val(lon);

            $("#wait").hide();
            $("#use_geo_button").attr("disabled", false);

            var map_location = [position.coords.latitude, position.coords.longitude];
            console.log("Your location is: " + map_location);
        });

    } else {
        /* geolocation IS NOT available */
        console.log("user isn\"t allowing location tracking");
    };
};

function changeChirp(evt) { 
    //doesn"t submit form, changes hich div is visible.
    evt.preventDefault();
    $("#alerts").html("");
    $(start_chirp).toggle();
    $(stop_chirp).toggle();
};


function startChirping(evt) {
    //Passes user input to server, calls makeChirp on results
    changeChirp(evt);
    loadSound();

    // Sets path to chirp with variables from html form
    var url = "/chirp?" + $("form").serialize();
    console.log(url);
    $.get(url, makeChirps);
};


function playSound() {
        createjs.Sound.play(soundID);
        console.log("chirp");
};


function makeChirps(chirp_time_string) {
    // Takes in a time between chirps, and chirps at that interval. Returns nothing
    chirp_time = Number(chirp_time_string);

    if (chirp_time) {
        chirping = setInterval(playSound, chirp_time);
    } else {
        //make error msg appear;
        $("#alerts").html("No crickets would be chirping at this temp. Ahhhh, silence.");
    };
};


function stopChirping(evt) { 
    // stop chirping and return to start page.
    changeChirp(evt);
    clearInterval(chirping);
};


getLocation();

// closing docready
//});
