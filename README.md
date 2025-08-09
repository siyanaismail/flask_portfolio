# Flask Portfolio Website

A simple personal portfolio website built using **Python Flask**, **HTML**, and **CSS**.  
It showcases personal details, projects, and includes a contact form.

## Objective

To create a real-world mini web application using Flask that displays personal portfolio information and handles contact form submissions.

## Tools & Technologies

- **Python** (Flask)
- **HTML5**
- **CSS3**
- **Jinja2 Templating** (for rendering HTML with Flask)
- **Bootstrap** (optional, for styling)

## Project Structure

```
flask_portfolio/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── index.html
    └── contact.html
```

## Features

- **Home Page** (`index.html`): Displays personal introduction and list of projects.
- **Contact Page** (`contact.html`): Allows visitors to send a message (data is printed in the terminal for now).
- **CSS Styling** via `static/style.css`.
- **Flask Routing** for dynamic page loading.

## Getting Started

### 1.Install Flask

```bash
pip install flask
```

### 2.Run the Application

Navigate to your project folder and run:

```bash
python app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000/
```

### Open in Browser

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Flask Routing Overview

- `/` → Renders **index.html**
- `/contact` → Renders **contact.html** and handles form submission

## 🖌 HTML & CSS Linking

Flask serves CSS from the `static/` folder.  
Link CSS in HTML using:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```