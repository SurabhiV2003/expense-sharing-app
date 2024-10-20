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
    * Response:
   ```
   {
      "message": "Expense added successfully"
   }
    ```
2. Retrieve User Details

   * URL: /api/users/<user_id>
   * Method: GET
   * Description: Retrieve details for a specific user.
   * Response:
   ```
   {
     "user": {
    "id": 1,
    "email": "test@example.com",
    "name": "Test User",
    "mobile": "1234567890"
        }
   }
   ```
### Expense Endpoints
1. Add an Expense
   * URL: /api/expenses
   * Method: POST
   * Description: Add a new expense.
   * Request Body:
   ```
   {
     "description": "Dinner",
     "total_amount": 3000,
     "split_type": "equal", // or "exact", "percentage"
     "created_by": 1, // user ID
     "participants": [
    {"user_id": 1},
    {"user_id": 2},
    {"user_id": 3}
     ]
   }
   ```
   * Response:
   ```
   {
     "message": "Expense added successfully"
   }
   ```
2. Retrieve All Expenses

   * URL: /api/expenses
   * Method: GET
   * Description: Retrieve a list of all expenses.
     
3. Download Balance Sheet

   * URL: /api/balancesheet/download
   * Method: GET
   * Description: Download the balance sheet for all users.

## Installation and Setup
### Prerequisites
* Python 3.x
* Flask
* SQLite (default, can be replaced with another database)
### Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/expense-sharing-app.git
cd expense-sharing-app
```
2. Set up a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Set up the database:
* Initialize the database using Flask-Migrate:
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
* Run the Flask application:
```
python run.py
```
The application should now be running at http://127.0.0.1:5000/

## Usage
### Adding Users and Expenses
1. Add a new user by sending a POST request to /api/users with the user details.
2. Add an expense by sending a POST request to /api/expenses with the expense details and the participants' information.
3. Retrieve expenses by sending a GET request to /api/expenses.
4. Download the balance sheet by sending a GET request to /api/balancesheet/download.
### Frontend Interaction
If you want to interact with the backend using the HTML form provided, open the index.html in your browser after the server is running. The form allows you to add expenses by specifying the split method and participants.
