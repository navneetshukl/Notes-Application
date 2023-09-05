# Django Note Taking App

![Django Version](https://img.shields.io/badge/Django-3.2-green)
![Python Version](https://img.shields.io/badge/Python-3.9-blue)

A simple web-based note-taking application built with Django, featuring user authentication, note creation, editing, and deletion.

## Table of Contents

- [Features](#features)
- [Usage](#usage)


## Features

- **User Registration and Authentication:** Users can sign up with a name, email, and password. Existing users can log in securely.

- **Create Notes:** Authenticated users can create new notes with a title and description.

- **View All Notes:** Users can view a list of all their notes, including titles and descriptions.

- **View and Edit Individual Notes:** Users can click on a note to view its details and edit the title and description.

- **Delete Notes:** Users can delete unwanted notes.

- ## Usage

### Sign Up:
1. Open your web browser and go to [http://localhost:8000/signup/](http://localhost:8000/signup/).
2. Enter your name, email, and password to create an account.

### Log In:
1. After signing up, you can log in at [http://localhost:8000/signin/](http://localhost:8000/signin/) using your email and password.

### Create Notes:
1. Once logged in, you can create new notes by clicking on "Create Note" in the navigation menu.

### View All Notes:
1. Click on "All Notes" in the navigation menu to see a list of all your notes.

### View and Edit Notes:
1. Click on a note title to view its details and edit the title or description.

### Delete Notes:
1. To delete a note, click on the "Delete" button next to the note.


## Technology Stack

This project is built using the following technologies and software:

- **Django** - A high-level Python web framework for building web applications.
- **Python** - The programming language used for the backend logic.
- **MongoDB** - A NoSQL database used to store user data and notes.
- **JWT (JSON Web Tokens)** - Used for user authentication and token-based security.
- **HTML/CSS** - For building the frontend user interface and styling.
- **PyJWT** - A Python library for working with JWT tokens.
