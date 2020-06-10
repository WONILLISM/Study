// <⚠️ DONT DELETE THIS ⚠️>
// import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

const toDoForm = document.querySelector(".js-toDoForm"),
    toDoInput = toDoForm.querySelector("input"),
    toDoList = document.querySelector(".js-toDoList"),
    finDoList = document.querySelector(".js-finDoList");

const TODOS_LS = 'toDos';
const FINDOS_LS = 'finDos';
let toDos =[];
let finDos = [];

function btnEventHandler(event){
    const btn = event.target;
    const li = btn.parentNode;
    
    if(btn.id == "finBtn"){
        toDoList.removeChild(li);
        const cleanToDos = toDos.filter((toDo)=>{
            return toDo.id !== parseInt(li.id);
        });
        
        toDos = cleanToDos;
        const newId = finDos.length+1;
        const pendBtn = li.childNodes[2];
        const text = li.childNodes[0].innerText;
        li.id = newId;
        pendBtn.id = "pendBtn";
        pendBtn.innerText = "↩"
        finDoList.appendChild(li);

        const finDoObj={
            text: text,
            id: newId,
        }
        finDos.push(finDoObj);
        console.log(finDos);
    }
    else if(btn.id == "pendBtn"){
        finDoList.removeChild(li);
        const cleanFinDos = finDos.filter((finDo)=>{
            return finDo.id !== parseInt(li.id);
        });
        
        finDos = cleanFinDos;
        const newId = toDos.length+1;
        const finBtn = li.childNodes[2];
        const text = li.childNodes[0].innerText;
        li.id = newId;
        finBtn.id = "finBtn";
        finBtn.innerText = "✔"
        toDoList.appendChild(li);

        const toDoObj={
            text: text,
            id: newId,
        }
        toDos.push(toDoObj);
    }
    else{
        const ul = li.parentNode;
        if(ul.className =="js-toDoList"){
            toDoList.removeChild(li);
            const cleanToDos = toDos.filter((toDo)=>{
                return toDo.id !== parseInt(li.id);
            });
            toDos = cleanToDos;
        }
        else if(ul.className=="js-finDoList"){
            finDoList.removeChild(li);
            const cleanFinDos = finDos.filter((finDo)=>{
                return finDo.id !== parseInt(li.id);
            });
            finDos = cleanFinDos;
        }
    }
    saveDos();
}
function saveDos(){
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
    localStorage.setItem(FINDOS_LS, JSON.stringify(finDos));
}
function paintToDo(text){   
    const li = document.createElement("li"); 
    const delBtn = document.createElement("button");
    const finBtn = document.createElement("button");
    const span = document.createElement("span");
    const newId = toDos.length + 1;

    delBtn.id = "delBtn";
    delBtn.innerText="X";
    delBtn.addEventListener("click",btnEventHandler);
    finBtn.id = "finBtn";
    finBtn.innerText="✔";
    finBtn.addEventListener("click",btnEventHandler);
    span.innerText = text;
    li.appendChild(span);
    li.appendChild(delBtn);
    li.appendChild(finBtn);
    li.id = newId;
    toDoList.appendChild(li);

    const toDoObj = {
        text: text,
        id:newId,
    }
    toDos.push(toDoObj);
    saveDos(); 
}
function loadToDos(){
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if(loadedToDos!==null){
        const parsedToDos = JSON.parse(loadedToDos);
        parsedToDos.forEach((toDo)=>{
            paintToDo(toDo.text);
        });
    }
}
function init(){
    loadToDos();
    toDoForm.addEventListener("submit",(event)=>{
        event.preventDefault();
        const currentValue = toDoInput.value;
        paintToDo(currentValue);
        toDoInput.value="";
    })
}
init();