<img src="https://maxmautner.com/public/images/django.gif" align="center">

# Django Todo List

A simple Todo List application built with Django and MySQL, featuring custom user model and registration functionality.

## Features

- User authentication (login, logout, register)
- Custom user model
- Create, update, delete, and view todo items
- User-specific todo lists

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/amirhoseinshojaei/Django-TodoList.git
    cd Django-TodoList
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Setup the database:**
    Ensure you have MySQL installed and running. Update your database settings in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```
    Then, apply the migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

- Navigate to `http://127.0.0.1:8000` in your browser.
- Register a new user or log in with the superuser credentials.
- Create, view, update, and delete todo items.

## Project Structure

- `auths/` - Contains the custom user model and authentication views.
- `core/` - Core functionality of the todo list application.
- `web/` - Frontend templates and static files.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Happy Mood

**Be happy and Enjoy this project , And Always learning😎**