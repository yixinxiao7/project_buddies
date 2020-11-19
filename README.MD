# Overview
Built from: https://www.valentinog.com/blog/drf/

### Basic Build (incomplete)
- Create virtual environment: `python3 -m venv venv`
- Activate virtual environment: `source venv/bin/activate`
- Run install script: `pip install -r requirements.txt`

### Run Server
`python manage.py runserver`

### Create Schema
- `python manage.py makemigrations backend; python manage.py migrate`

### Activate Scripts
`chmod +x bin/db`

### Coverage commands
`coverage run --source='.' manage.py test`
`coverage html`
`coverage report`
