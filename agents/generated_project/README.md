# Digital Clock

A lightweight web‑app that displays the current time in either a 12‑hour or 24‑hour format. The clock updates every second and can be toggled by clicking on it.

---

## 📦 Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **HTML** | `index.html` | Structure of the page. |
| **CSS** | `styles.css` | Styling and layout of the clock. |
| **JavaScript** | `script.js` | Logic for time calculation, formatting, and DOM updates. |
| **Browser** | Any modern browser (Chrome, Firefox, Edge, Safari) | Runs the application. |

## 🚀 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/digital-clock.git
   cd digital-clock
   ```

2. **Open the app**
   The project contains only static files, so you can open it directly in the browser:
   ```bash
   open src/index.html
   ```
   *On Windows, double‑click `src/index.html` or use `start` in the command line.*

No additional build steps or server are required.

## 🔍 Usage

* **View the clock** – The current time is shown in the center of the page.
* **Toggle format** – Click anywhere on the clock to switch between 12‑hour and 24‑hour displays.

The clock updates automatically every second.

## ✏️ Customisation

Feel free to tweak the look and behaviour:

### Styling
- Open `src/styles.css`.
- Modify the `font-size`, `color`, `background`, or any other CSS property to change the appearance.

### Behaviour
- Open `src/script.js`.
- Functions `formatTime12` and `formatTime24` handle the two display modes. Adjust the logic or add new formatting rules here.
- The `toggleFormat` function is bound to the `click` event of the clock element. Add more event listeners or change the trigger if needed.

## 📄 License
This project is released under the MIT License.
