// <⚠️ DONT DELETE THIS ⚠️>
import "./styles.css";
const colors = ["#1abc9c", "#3498db", "#9b59b6", "#f39c12", "#e74c3c"];
// <⚠️ /DONT DELETE THIS ⚠️>

/*
✅ The text of the title should change when the mouse is on top of it.
✅ The text of the title should change when the mouse is leaves it.
✅ When the window is resized the title should change.
✅ On right click the title should also change.
✅ The colors of the title should come from a color from the colors array.
✅ DO NOT CHANGE .css, or .html files.
✅ ALL function handlers should be INSIDE of "superEventHandler"
*/

const superEventHandler = {
  // The mouse is here!
  mouseHereHandler: () => {
    h2.innerText = "The mouse is here!";
    h2.style.color = colors[1];
  },
  // The mouse is gone!
  mouseGoneHandler: () => {
    h2.innerText = "The mouse is gone!";
    h2.style.color = colors[2];
  },
  // That was a right click!
  mouseRightClickHandler: () => {
    h2.innerText = "That was a right click!";
    h2.style.color = colors[3];
  },
  // You just resized!
  windowResizedHandler: () => {
    h2.innerText = "You just resized!";
    h2.style.color = colors[4];
  }
};

const h2 = document.getElementsByTagName("h2")[0];
console.log(h2);
h2.addEventListener("mouseover", superEventHandler.mouseHereHandler);
h2.addEventListener("mouseleave", superEventHandler.mouseGoneHandler);
window.addEventListener(
  "contextmenu",
  superEventHandler.mouseRightClickHandler
);
window.addEventListener("resize", superEventHandler.windowResizedHandler);
