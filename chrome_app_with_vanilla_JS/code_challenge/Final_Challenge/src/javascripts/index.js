import Now from './nowClass.js';
import ToDo from './toDoList.js';
import Weather from './weather.js';

const body = document.body;

const nowContainer = document.querySelector(".now-container");
const now = new Now(nowContainer);

const IMG_NUM = 11;

function setBackground(){
    const randomNum = Math.floor(Math.random()*IMG_NUM + 1);
    const image = new Image();
    image.src = `assets/bg${randomNum}.jpg`
    image.classList.add("bgImage");
    body.prepend(image);
}
function init(){
    setBackground();
    setInterval(()=>{
        now.display();
    },1000);
    ToDo();
    Weather();
}
init();