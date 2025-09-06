const clockEl = document.getElementById('clock');
const toggleBtn = document.getElementById('toggle-format');
let is24h = true;

function getCurrentTime() {
  return new Date();
}

function formatTime(date, is24h) {
  const pad = (num) => String(num).padStart(2, '0');
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const seconds = date.getSeconds();

  if (is24h) {
    return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
  } else {
    let hour12 = hours % 12;
    if (hour12 === 0) hour12 = 12;
    const ampm = hours < 12 ? 'AM' : 'PM';
    return `${hour12}:${pad(minutes)}:${pad(seconds)} ${ampm}`;
  }
}

function updateClock() {
  const now = getCurrentTime();
  clockEl.textContent = formatTime(now, is24h);
}

toggleBtn.addEventListener('click', () => {
  is24h = !is24h;
  toggleBtn.textContent = is24h ? '12h' : '24h';
  updateClock();
});

updateClock();
setInterval(updateClock, 1000);
