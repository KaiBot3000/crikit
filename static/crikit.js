var soundPath = "static/crikit_chirp.mp3"
var soundID = "Chirp";
var chirping;


// on load, 
// -get, set location
// -determine chirptime
// -on click, check data
// -if off, stop chirp, if on, start

getLocation();
$("#switch").change(change);

function loadSound() {
    // Loads sound for chirp
    createjs.Sound.registerSound(soundPath, soundID);
}

function getLocation() {
    if ("geolocation" in navigator) {
            /* geolocation is available */
        navigator.geolocation.getCurrentPosition(function(position) {
            // this sometimes takes a while to complete
            var lat = position.coords.latitude;
            var lon = position.coords.longitude;
            $("#lat_form").val(lat);
            $("#lon_form").val(lon);

            $("#alerts").html("");
            $("#switch-span").css("visibility", "visible");

            var map_location = [position.coords.latitude, position.coords.longitude];
            console.log("Your location is: " + map_location);
        });

    } else {
        /* geolocation IS NOT available */
        console.log("user isn\'t allowing location tracking");
        $("#alerts").html("You need to allow geolocation for this to work :/");
    };
}

function change() {
    if(this.checked) {
        startChirping();
    } else {
        stopChirping();
    }
}

function startChirping(evt) {
    loadSound();
    // Sets path to chirp with variables from html form
    var url = "/chirp?" + $("form").serialize();
    console.log(url);
    $.get(url, makeChirps);
}

function stopChirping(evt) { 
    clearInterval(chirping);
    $("#alerts").html("");
}

function makeChirps(chirp_time_string) {
    // Takes in a time between chirps, and chirps at that interval. Returns nothing
    chirp_time = Number(chirp_time_string);
    if (chirp_time) {
        chirping = setInterval(playSound, chirp_time);
    } else {
        $("#alerts").html("Either you're not within a temp range that crickets enjoy, or there was a problem with the weather API :(");
    };
}

function playSound() {
        createjs.Sound.play(soundID);
        console.log("chirp");
}
