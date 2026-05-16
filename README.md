# web_development

Collection of Django example projects and tutorials used for learning and demos.

Overview
--------
This repository contains multiple small Django projects demonstrating class-based and function-based views, forms, ORM usage, migrations, and deployment notes (including AWS/MariaDB setup). Most projects use SQLite locally; some include instructions for MariaDB/MySQL.

Top-level folders (high level)
--------------------------------
- `cbvCRUD` — class-based view CRUD examples.
- `classBasedViews` — additional class-based-view examples.
- `clinicals` — clinicals project with MariaDB notes and AWS setup instructions.
- `djangoORMdemo` — ORM examples and queries.
- `fbvCRUD` — function-based view CRUD examples.
- `firstproject` — starter Django project and app examples.
- `formsDemo` — Django forms examples.
- `modelDemo` — model-focused examples and notes.
- `modelFormsDemo` — examples using ModelForm.
- `productTemplates` — product app and template demos.
- `session_project` — session handling examples.
- `templatesDemo` — template-related examples.

Quickstart (local development)
------------------------------
1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv venv
& .\venv\Scripts\Activate.ps1
```

2. Install dependencies (if you have a `requirements.txt` in a project folder):

```powershell
pip install -r requirements.txt
```

3. Pick a project to run (for example `clinicals` or `firstproject`):

```powershell
cd clinicals
python manage.py migrate
python manage.py runserver
```

Notes
-----
- Many projects use SQLite by default (look for `db.sqlite3` files in project folders).
- The `clinicals` project includes MariaDB configuration and AWS setup notes in `Django+Setup+on+AWS.txt` and `updated_django_mariadb_ec_2_setup_amazon_linux_2023.md`.
- Database credentials found in some example settings are for development/testing only; do not use them in production.
- If you need to run a different project's server, change into that project's folder (the folder containing `manage.py`) and run the usual Django commands.

Helpful commands
----------------
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser`
- Run tests (if provided): `python manage.py test`
- Start development server: `python manage.py runserver`
- Open Django shell: `python manage.py shell`
- Check for issues: `python manage.py check`
