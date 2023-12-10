# Library_Management_System_Letsbloom_Assignment

This project implements a simple RESTful API for managing a library system using Node.js, Express, and MongoDB with Mongoose.

## Setup Instructions

### Prerequisites

- Python installed
- PostgreSQL server installed and running

### Installation Steps

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/vanumdaniel7/Library_Management_System_Letsbloom_Assignment
   ```

2. After you cloned the repository, you have to create a virtual environment.
   
   ```powershell
   py -m env .venv
   ```
   
3. After this activate the virtual environment.
   ```powershell
   .venv/Scripts/Activate.ps1
   ```

5. Inside the `.env` file, set your MongoDB URI using a variable named `MONGODB_URL`. For example:

   ```
   MONGODB_URL=mongodb://username:password@your-mongodb-host:27017/your-database-name
   ```

6. Install dependencies.

   ```bash
   npm install
   ```

### Configuration

- Ensure MongoDB is running locally or use the MongoDB URI in the `.env` file for your database connection.

### Running the Server

1. Start the Express server.

   ```bash
   npm start
   ```

2. The server will start running on `http://localhost:8000` by default.

### API Endpoints

- **Retrieve All Books**
  - `GET /api/books`
- **Add a New Book**
  - `POST /api/books`
  - Request Body: JSON object representing the new book.
- **Update Book Details**
  - `PUT /api/books/{id}`
  - Request Body: JSON object with updated book details.

## Usage

- Use tools like Postman or cURL to make requests to the provided endpoints.
- For example:
  - Retrieve all books: `GET http://localhost:8000/api/books`
  - Add a book: `POST http://localhost:8000/api/books` with a JSON payload.
  - Update a book: `PUT http://localhost:8000/api/books/{book_id}` with a JSON payload.
