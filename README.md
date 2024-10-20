# Daily Expenses Sharing Application

## Project Description
This is a Daily Expenses Sharing Application that allows users to manage shared expenses efficiently. Users can add expenses and split them among participants using three different methods: equal split, exact amounts, or percentage-based splits. The application also generates balance sheets and allows users to download them.

## Key Features
* User Management: Users can create accounts with email, name, and mobile number.
* Expense Management: Users can add and manage expenses.
    * Split equally among all participants.
    * Specify exact amounts for each participant.
    * Split expenses by specifying percentages.
* Balance Sheet: Shows individual and overall expenses for users, and allows downloading of the balance sheet.

## Table of Contents
1. Project Description
2. Tech Stack
3. API Endpoints
4. Installation and Setup
5. Usage


## Tech Stack
* Backend: Flask (Python)
* Database: SQLite (can be replaced with other databases like PostgreSQL)
* ORM: SQLAlchemy
* Frontend: HTML, JavaScript (basic form for API interaction)
* Tools: Flask-Migrate for database migrations

## API Endpoints
### User Endpoints
1. Create a User

    * URL: /api/users
    * Method: POST
    * Description: Create a new user.
    * Request Body:
    ```
    {
  "email": "test@example.com",
  "name": "Test User",
  "mobile": "1234567890"
}
    
    ```
    * Response