# Movie Review Web Application

Welcome to my Movie Review Web Application project! This project allows users to write and view movie reviews.

## Overview

This project aims to create a web application where users can:
- Write reviews for movies they've watched.
- Browse and read reviews written by other users.

## Setup and Running

### Prerequisites
Before you begin, make sure you have the following installed:
- Python (version 3.x)
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

### Installation
1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.

### Setting Up
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "Initial database migration"
   flask db upgrade
   ```

### Running the Application
1. Start the Flask server:
   ```bash
   flask run
   ```
2. Open your web browser and go to `http://localhost:5000` to view the application.

## Testing

### Running Tests
- Tests are located in the `tests` directory.
- To run tests, use:
  ```bash
  pytest
  ```

## Report

### Design and Coding Choices
- I used Flask and Flask-SQLAlchemy for building the web application.
- The application follows a simple MVC (Model-View-Controller) architecture.
- Each movie review is stored in a SQLite database using SQLAlchemy.

### Challenges Faced
- Setting up the database models and migrations correctly.
- Ensuring proper integration of Flask-Migrate for database management.

### Lessons Learned
- Understanding the importance of database migrations for application updates.
- Improved knowledge of web development using Flask framework.
