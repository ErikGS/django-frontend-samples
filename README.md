# Django setup with HTMX and Svelte front-ends

- A Django backend setup with a simple SSR page and a simple REST API;
- A simple Svelte SPA;
- A simple HTMX SPA.

Just start the server, go to 'localhost:8000' and use the links to switch between apps: HTMX, Svelte, REST-Api.

## Getting Started

- This sample uses <a href="https://python-poetry.org/">Poetry</a> to manage and install dependencies of Python projects, get it with:
  ```bash
  pip install poetry
  ```
  
- Install all Python's project dependecies (like Django) with:
  ```bash
  poetry install
  ```
  *Poetry will install all dependencies in an isolated virtual environment;
  
- After everything is installed, open the virtual env. shell and initialize the DB with:
  ```bash
  poetry shell
  py .\manage.py migrate
  ```
  
- Then you need to create an admin user with:
  ```bash
  py .\manage.py createsuperuser
  ```
  Type the username (leave blank to use the suggested one) and hit enter, then type a password and hit enter (type the password again to confirm);

- Finally, start the server with:
  ```bash
  py .\manage.py runserver
  ```
  
- The console output should have:
  ```bash
  Starting development server at http://127.0.0.1:8000/
  ```
  Visit the addres and you should see a simple static page displaying a 'hello world' message. You will be prompetd to login for the first time you open an app, use the account you created earlier.

- Use the links to switch front-ends, or click REST-API to see the API response from Django! It should look like this:
  ```json
  {
    "message": "Hello world"
  }
  ```
  OR, if you're not logged:
  ```json
  {
    "detail": "Authentication credentials were not provided."
  }
  ```
  
- You can also access Django admin panel by navigating to /admin/ URL.
  
- To stop the server just hit CTRL+C at any time in the console.
