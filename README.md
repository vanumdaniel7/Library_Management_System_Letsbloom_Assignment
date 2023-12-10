# Library_Management_System_Letsbloom_Assignment

This project implements a simple RESTful API for managing a library system using Django and PostgreSQL

## Setup Instructions

### Prerequisites

- Python installed
- PostgreSQL server installed and running or you can use a remote PostgreSQL server.

### Installation Steps

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/vanumdaniel7/Library_Management_System_Letsbloom_Assignment
   ```

2. After you cloned the repository go inside the project directory, and create a virtual environment.
   
   ```powershell
   py -m venv .venv
   ```
   
3. After this activate the virtual environment(the following command is only for windows).
   ```powershell
   .venv/Scripts/Activate.ps1
   ```

4. Create a file named .env in the directory where the manage.py file is located.
5. Inside the .env file, set your PostgreSQL URL using a variable named DATABASE_URL. For example:

   ```
   DATABASE_URL=postgresql://username:password@host:port/database_name
   ```

6. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

1. Start the Django server.

   ```bash;
   py manage.py runserver
   ```

2. The server will start running on `http://localhost:8000` by default.

### API Endpoints

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/api/books` | GET | READ | Get all books
`/api/books` | POST | CREATE | Create a new book
`/api/books/{id}`| PUT | UPDATE | Update a movie

## Usage

- Use tools like Postman or cURL to make requests to the provided endpoints.
- For example:
  - Retrieve all books: `GET http://localhost:8000/api/books`
  - Add a book: `POST http://localhost:8000/api/books` with a JSON payload.
  - Update a book: `PUT http://localhost:8000/api/books/{book_id}` with a JSON payload.
