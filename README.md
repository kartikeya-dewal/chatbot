# AI Hackathon

This is an Interview chatbot application with Django REST API backend and React frontend.<br/>

## Project Structure

Within the `ai-hackathon` directory, there are 3 modules:<br/>

- `chatbot` : This the Django project module that manages all the apps.<br/>
- `client` : This is a react frontend application.<br/>
- `server` : This is a python/django backend application.<br/>

## Prerequisites

Python 3.7.x, Node.js 10.16.x, npm 6.9.x

Install pipenv before creating a virtual environment for development. Execute the command below on teminal.

```bash
pip install pipenv

or

pip3 install pipenv
```

## Running the app

Clone the repository and switch to `develop` branch. From project root directory, execute following commands from the terminal:

```bash
pipenv shell
```

This should activate a virtual python environment. Then run

```bash
pipenv install
```

to install python dependencies.<br/>
To install node modules for the `client`, run

```
npm install
npm run dev
```

From inside `ai-hackathon` directory, run

```bash
python manage.py makemigrations server
python manage.py migrate
python manage.py runserver
```

The app should now be running on `localhost:8000`.
