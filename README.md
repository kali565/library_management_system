# Library Management System

This is a Library Management System built with Django.

## Description

The Library Management System is a web application designed to help libraries manage their resources efficiently. It provides features such as user authentication, book issuance and return, viewing book history, and administrative functions.

## Features

- **User Authentication**: Users can register, log in, and log out securely.
- **Book Issuance and Return**: Users can borrow books from the library and return them when finished.
- **Viewing Book History**: Users can view their borrowing history and see which books they currently have borrowed.
- **Administrative Functions**: Admins can add, edit, and delete books from the system, as well as manage user accounts.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kali565/library_management_system.git


2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

5. **Access the application**:
    Visit `http://localhost:8000` in your web browser.

## Usage
To access the admin interface, go to http://localhost:8000/admin and log in with the superuser credentials.
Regular users can log in to borrow and return books using their credentials.
Admins can manage books, users, and borrowings through the admin interface.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
   
