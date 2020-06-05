import "./styles.css";

// You're gonna need this
const NINE_HOURS_MILLISECONDS = 32400000;
const clockContainer = document.querySelector(".js-clock");
const title = clockContainer.querySelector("h1");
const clockTitle = clockContainer.querySelector("h2");
function getTime() {
  // Don't delete this.
  const xmasDay = new Date("2020-12-24:00:00:00+0900");
  let curDay = new Date();
  const timeoffset = curDay.getTimezoneOffset();
  curDay = curDay.getTime();
  curDay = curDay + timeoffset * 60 * 1000 + NINE_HOURS_MILLISECONDS;
  const _seconds = 1000;
  const _minutes = _seconds * 60;
  const _hours = _minutes * 60;
  const _days = _hours * 24;

  const distance = xmasDay - curDay;

  const remainDays = Math.floor(distance / _days);
  const remainHours = Math.floor((distance % _days) / _hours);
  const remainMinutes = Math.floor((distance % _hours) / _minutes);
  const remainSeconds = Math.floor((distance % _minutes) / _seconds);

  clockTitle.innerHTML =
    `${remainDays}d ` +
    `${remainHours < 10 ? `0${remainHours}` : remainHours}h ` +
    `${remainMinutes < 10 ? `0${remainMinutes}` : remainMinutes}m ` +
    `${remainSeconds < 10 ? `0${remainSeconds}` : remainSeconds}s `;
}

function init() {
  title.innerText = "Time Untill Christmas";
  getTime();

  setInterval(getTime, 1000);
}
init();
