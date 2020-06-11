// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>
const gameForm = document.querySelector(".js-gameForm"),
    range = gameForm.rangeHandler;
let answer;
let inputNum;
function getRangeValue(){
    return range.value;
}
function inputBtnOnClick(){
    gameForm.addEventListener("submit",(event)=>{
        event.preventDefault();
    })
    inputNum = gameForm.num.value;
    let maxRange = getRangeValue();
    answer = Math.floor(Math.random()*maxRange);
    console.log(maxRange);
    if(maxRange!=='0'){
        if(inputNum!==""){
            const res = document.querySelector(".js-result");
            
            let proc = `You chose: ${inputNum}, the machine chose ${answer}`;
            let result = answer == inputNum?"You win!":"You lost!";
            res.childNodes[1].innerText = proc;
            res.childNodes[3].innerText = result;
        }
        else{
            alert("Please input number.");
        }
    }
    else{
        alert("Please input max range.");
    }
}
