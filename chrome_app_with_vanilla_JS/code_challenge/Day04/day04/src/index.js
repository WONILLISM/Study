// <⚠️ DONT DELETE THIS ⚠️>
import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>
let body = document.querySelector("body");
body.innerHTML = "<h1>" + "Hello!" + "</h1>";
body.style.color = "white";
console.log(document.querySelector("body"));
function bgColorHandler() {
  const width = window.innerWidth;
  if (width >= 1000) {
    document.querySelector("body").style.backgroundColor = "yellow";
  } else if (width >= 600) {
    document.querySelector("body").style.backgroundColor = "purple";
  } else {
    document.querySelector("body").style.backgroundColor = "blue";
  }
}
bgColorHandler();
window.addEventListener("resize", bgColorHandler);
