# Letsbloom Assignment - Library Management System

This project implements a simple RESTful API for managing a library system using Django and PostgreSQL.

Please refer to Documentation.pdf for more details

## Setup Instructions

### Prerequisites

- Python installed
- PostgreSQL server installed and running or you can use a remote PostgreSQL server.

### Installation Steps

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/vanumdaniel7/Library_Management_System_Letsbloom_Assignment
   ```

2. After you cloned the repository go inside the project directory, and create a virtual environment. After creating a virtual environment, ensure to configure the selected interpreter within your integrated development environment (IDE) by navigating to the appropriate settings or preferences. This step is essential for the IDE to recognize and utilize the Python interpreter specific to your virtual environment, providing a controlled environment for your project.
   
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

7. Apply the migrations.
   
   ```bash
   py manage.py migrate
   ```

8. Seed the database by using the following command.
   
    ```bash
   py manage.py seed
   ```
   

### Running the Server

1. Start the Django server.

   ```bash
   py manage.py runserver
   ```

2. The server will start running on `http://localhost:8000` by default.

### API Endpoints (Refer to Documentation.pdf for more details)

| Endpoint            | HTTP Method | CRUD Method | Result                | Payload(request body)                        |
| ------------------- | ----------- | ----------- | --------------------- | -------------------------------------------- |
| `/api/books`        | GET         | READ        | Get all books         | No payload                                   |
| `/api/books`        | POST        | CREATE      | Create a new book     | createPayload                                |
| `/api/books/{id}`   | PUT         | UPDATE      | Update a movie        | updatePayload                                |

where updatePayload and createPayload are of the format
```javascript 
{
    "title": "(str) - The title of the book, required",
    "author": "(str) - The author of the book, required",
    "edition": "(str) - The edition of the book, required",
    "publication": "(str) - The publication name, required",
    "publisher": "(str) - The publisher of the book, required",
    "language": "(str) - The language of the book, required",
    "publicationDate": "(str) - The publication date of the book (YYYY-MM-DD), required",
    "numberOfCopies": "(int) - The number of copies available, required"
}
```

## Usage

- Use tools like Postman or CURL to make requests to the provided endpoints.
- For example:
  - Retrieve all books: `GET http://localhost:8000/api/books`
  - Add a book: `POST http://localhost:8000/api/books` with a JSON payload.
  - Update a book: `PUT http://localhost:8000/api/books/{id}` with a JSON payload.
