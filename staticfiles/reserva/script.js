const daysTag = document.querySelector(".days"),
  currentDate = document.querySelector(".current-date"),
  prevNextIcon = document.querySelectorAll(".icons span");

// Getting new date, current year and month
let date = new Date(),
  currYear = date.getFullYear(),
  currMonth = date.getMonth();

// Storing full names of all months in an array
const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const renderCalendar = () => {
  let firstDayOfMonth = new Date(currYear, currMonth, 1).getDay(), // Getting the first day of the month
    lastDateOfMonth = new Date(currYear, currMonth + 1, 0).getDate(), // Getting the last date of the month
    lastDayOfMonth = new Date(currYear, currMonth, lastDateOfMonth).getDay(), // Getting the last day of the month
    lastDateOfLastMonth = new Date(currYear, currMonth, 0).getDate(); // Getting the last date of the previous month
  let liTag = "";

  for (let i = firstDayOfMonth; i > 0; i--) {
    // Creating li elements for the last days of the previous month
    liTag += `<li class="inactive">${lastDateOfLastMonth - i + 1}</li>`;
  }

  for (let i = 1; i <= lastDateOfMonth; i++) {
    // Creating li elements for all days of the current month
    let isToday =
      i === date.getDate() &&
      currMonth === new Date().getMonth() &&
      currYear === new Date().getFullYear()
        ? "active"
        : "";
    liTag += `<li class="${isToday}" onclick="showReservationPrompt(this)">${i}</li>`;
  }

  for (let i = lastDayOfMonth; i < 6; i++) {
    // Creating li elements for the first days of the next month
    liTag += `<li class="inactive">${i - lastDayOfMonth + 1}</li>`;
  }
  currentDate.innerText = `${months[currMonth]} ${currYear}`;
  daysTag.innerHTML = liTag;
};
renderCalendar();

prevNextIcon.forEach((icon) => {
  // Adding click event listeners to prev and next icons
  icon.addEventListener("click", () => {
    currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;

    if (currMonth < 0 || currMonth > 11) {
      date = new Date(currYear, currMonth, new Date().getDate());
      currYear = date.getFullYear();
      currMonth = date.getMonth();
    } else {
      date = new Date();
    }
    renderCalendar();
  });
});

function showReservationPrompt(dayElement) {
  const reservationConfirmed = confirm("Deseja mesmo reservar esta data?");
  if (reservationConfirmed) {
    dayElement.classList.add("reserved");
  }
}
