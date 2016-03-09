var soundPath = "static/crikit_chirp.mp3"
var soundID = "Chirp";
var chirping, map_location;

getLocation();
$("#switch").change(changeChirp);
$("#info").hover(
    function () {
        $("#info").stop().animate({'right':'-20px'},200);
    },
    function () {
        $("#info").stop().animate({'right':'-420px'},200);
    }
);

function loadSound() {
    // Loads sound for chirp
    createjs.Sound.registerSound(soundPath, soundID);
}

function getLocation() {
    if ("geolocation" in navigator) {
            /* geolocation is available */
        navigator.geolocation.getCurrentPosition(function(position) {
            // This may take a minute
            $("#alerts").html("");
            $("#switch-div").css("visibility", "visible");
            map_location = {latitude:position.coords.latitude, longitude:position.coords.longitude};
            // console.log(map_location);
        });

    } else {
        /* geolocation IS NOT available */
        $("#alerts").html("You need to allow geolocation for this to work :/");
    };
}

// TODO: get chirp_time *once* on load. Minimizes server requests, but also means user
// can't easily reset their temperature/interval.

function changeChirp() {
    if(this.checked) {
        loadSound();
        var url = "/chirp?" + $.param(map_location);
        $.get(url, makeChirps);
    } else {
        clearInterval(chirping);
        $("#alerts").html("");
    }
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
