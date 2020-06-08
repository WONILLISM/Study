// <⚠️ DONT DELETE THIS ⚠️>
import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

const selectElement = document.querySelector("select");

selectElement.addEventListener("change", event => {
  const country = event.target.value;
  const curCountry = localStorage.getItem(country);

  if (curCountry === null) {
    if (country === "Korea") localStorage.setItem("country", "KR");
    else if (country === "Greece") localStorage.setItem("country", "GR");
    else if (country === "Turkey") localStorage.setItem("country", "TR");
    else if (country === "Finland") localStorage.setItem("country", "FI");
  }
});
