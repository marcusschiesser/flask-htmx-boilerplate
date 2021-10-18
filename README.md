[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

### Introduction

Welcome to this boilerplate to quickly start [Flask](https://flask.palletsprojects.com/en/2.0.x/) applications with [HTMX](https://htmx.org/) and [Tailwind CSS](https://tailwindcss.com/). It's a great stack to quickly prototype new web applications
using Python. 

Project structure is based on the [Flask tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/).

**What is HTMX?** Htmx lets you build modern and powerful user interfaces with simple markups without using any JavaScript. It's done by sending AJAX requests directly from an HTML element.

**What is Tailwind CSS?** Is a CSS framework to rapidly build modern websites without ever leaving HTML.

### Quick Start

1. Clone the repo

        $ git clone https://github.com/marcusschiesser/flask-htmx-boilerplate
        $ cd flask-htmx-boilerplate

2. Initialize and activate a virtual environment:

        $ python3 -m venv env
        $ source env/bin/activate

3. Install the dependencies:

        $ pip install -r requirements.txt

4. Run the development server:

        $ python app.py

## Adding a Database layer

To keep this template simple, no database layer was added. You can directly connect to a database 
as shown in the [Flask tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/database/) or if
you need the complexity of an ORM, add [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/).
