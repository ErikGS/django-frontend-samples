# Django SPA with Svelte

A simple SPA sample with Django as the backend and Svelte in the frontend.

## Getting Started

- This sample uses <a href="https://python-poetry.org/">Poetry</a> to manage and install dependencies of the Python project, you can install it with.
  ```bash
  pip install poetry
  ```

## Run
- Open a shell in the base directory of this project (the one where 'pyproject.toml' is located);
  
- Create the virtual environment for the Python project and get it's shell by running the following command:
  ```bash
  poetry shell
  ```

- Install all Python's project dependecies (like Django itself) with:
  ```bash
  poetry install
  ```
  This will install all dependencies in the isolated virtual environment;
  
- After all dependencies succeed, initialize the DB with:
  ```bash
  py .\manage.py migrate
  ```
  
- Then you need to create an admin user with:
  ```bash
  py .\manage.py createsuperuser
  ```
  Type the username (leave blank to use the suggested one) and hit enter, then type a password and hit enter (type the password again to confirm);

- Start the server with:
  ```bash
  py .\manage.py runserver
  ```
  
- The console output should have:
  ```bash
  Starting development server at http://127.0.0.1:8000/
  ```
  Visit the addres and after logged-in, you should see a Svelte page displaying a 'hello world' message from the server!

- Change the URL to /api/hello to see the API response from Django! It should look like this:
  ```json
  {
    "message": "Hello world"
  }
  ```

- To stop the server just enter CTRL+C at any time in the console.
