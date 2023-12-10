# Django Todo App Backend

This is the backend part of a Todo application built with Django. It provides the API for managing tasks and integrates with the frontend to create a complete Todo application.

## Getting Started

These instructions will help you set up and run the Todo app backend built with Django on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (3.6 or higher)
- pip (Python package installer)

### Installing

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/prulm/todo_django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd todo_django
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    ```bash
    # On Unix or MacOS
    source venv/bin/activate

    # On Windows
    venv\Scripts\activate
    ```

5. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Apply migrations to set up the database:

    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```

### Running the Server

Start the development server:

    
    python manage.py runserver
    
  The Development server will be running at `http://127.0.0.1:8000/`

## API Endpoints

- **List all tasks:**
  - Endpoint: `/note/load/`
  - Method: GET

- **Create a new task:**
  - Endpoint: `/note/create/`
  - Method: POST
  - Request Body: JSON with task content

- **Update a task:**
  - Endpoint: `/note/update/<task_id>/`
  - Method: PUT
  - Request Body: JSON with updated task content

- **Delete a task:**
  - Endpoint: `/note/delete/<task_id>/`
  - Method: DELETE
