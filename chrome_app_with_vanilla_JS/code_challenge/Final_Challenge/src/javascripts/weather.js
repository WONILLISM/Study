const weather =document.querySelector(".js-weather");

const API_KEY = "5fa0d397a4ab233741183e0a05278b3d";
const COORDS = 'coords';

function getWeather(lat, lon){
    fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`)
    
    .then((response)=>{
        return response.json();
    }).then((json)=>{
        console.log(json);
        const temperature = Math.round(parseFloat(json.main.temp)) + "℃";
        const place = json.name;
        weather.innerText = `${temperature} @ ${place}`;
    })

}
function saveCoords(coordsObj){
    localStorage.setItem(COORDS, JSON.stringify(coordsObj));
}
function handleGeoSuccess(positon){
    const letitude = positon.coords.letitude;
    const longitude = positon.coords.longitude;
    const coordsObj = {
        letitude,
        longitude
    };
    saveCoords(coordsObj);
    getWeather(letitude,longitude)

}
function handleGeoError(){
    console.log("Cant access geo location");
}   
function askForCoords(){
    navigator.geolocation.getCurrentPosition(handleGeoSuccess, handleGeoError);
}
function loadCoords(){
    const loadedCoords = localStorage.getItem(COORDS);
    if(loadedCoords === null){
        askForCoords();
    }
    else{
        const parsedCoords = JSON.parse(loadedCoords);
        //console.log(parsedCoords);
        getWeather(parsedCoords.letitude, parsedCoords.longitude);
    }
}

export default function init(){
    loadCoords();
}
