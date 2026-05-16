# Dockerize Django Clinicals App — Complete Flow

## 1. Run MySQL Container

```bash
docker run -d -p 6666:3306 --name=docker-mysql --env="MYSQL_ROOT_PASSWORD=test@1234" --env="MYSQL_DATABASE=clinicalsdb" mysql:8.0.15 --default-authentication-plugin=mysql_native_password
```

---

## 2. Enter MySQL Container

```bash
docker exec -it docker-mysql bash
```

---

## 3. Login to MySQL

```bash
mysql -uroot -p
```

Enter password:

```text
test@1234
```

---

## 4. Verify Database

```sql
show databases;
```

```sql
use clinicalsdb;
```

```sql
show tables;
```

---

# Django Setup

## 5. Create requirements.txt

```bash
pip freeze > requirements.txt
```

---

## 6. Update settings.py

In `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinicalsdb',
        'USER': 'root',
        'PASSWORD': 'test@1234',
        'HOST': 'mysql',
        'PORT': '3306',
    }
}
```

IMPORTANT:

```text
HOST should be mysql
NOT localhost
```

Because:

```bash
--link docker-mysql:mysql
```

creates hostname:

```text
mysql
```

inside Django container.

---

# Dockerfile

## 7. Create Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /djangoapps

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

# .dockerignore

## 8. Create .dockerignore

```text
venv/
__pycache__/
*.pyc
*.pyo
*.pyd

.git/
.gitignore

db.sqlite3

*.pdf

.env

media/
staticfiles/

node_modules/
```

IMPORTANT:

Do NOT ignore:

```text
requirements.txt
```

---

# Build Django Image

## 9. Build Docker Image

```bash
docker build -t clinicals_app .
```

Rebuild without cache:

```bash
docker build --no-cache -t clinicals_app .
```

---

# Run Django Container

## 10. Run Django Container

```bash
docker run -it --name=clinicals-app --link docker-mysql:mysql -p 10555:8000 clinicals_app
```

---

# Access Django Container

## 11. Open Bash Inside Django Container

```bash
docker exec -it clinicals-app bash
```

---

# Run Migrations

## 12. Apply Migrations

```bash
docker exec -it clinicals-app python manage.py migrate
```

---

# Create Superuser

## 13. Create Admin User

```bash
docker exec -it clinicals-app python manage.py createsuperuser
```

---

# Testing

## 14. Open Browser

```text
http://localhost:10555
```

Admin:

```text
http://localhost:10555/admin
```

---

# Useful Docker Commands

## Show Running Containers

```bash
docker ps
```

---

## Show All Containers

```bash
docker ps -a
```

---

## Show Images

```bash
docker images
```

---

## Stop Container

```bash
docker stop clinicals-app
```

---

## Start Existing Container

```bash
docker start clinicals-app
```

---

## Restart Container

```bash
docker restart clinicals-app
```

---

## Remove Container

```bash
docker rm clinicals-app
```

---

## Force Remove Container

```bash
docker rm -f clinicals-app
```

---

## Remove Image

```bash
docker rmi clinicals_app
```

---

## Force Remove Image

```bash
docker rmi -f clinicals_app
```

---

## See Logs

```bash
docker logs clinicals-app
```

Live logs:

```bash
docker logs -f clinicals-app
```

---

## Remove All Stopped Containers

```bash
docker container prune
```

---

## Remove Unused Images

```bash
docker image prune
```

---

## Remove Everything Unused

```bash
docker system prune
```

Aggressive cleanup:

```bash
docker system prune -a
```

---

# Flow Summary

```text
MySQL Container
      ↓
Django Docker Image
      ↓
Django Container
      ↓
Run Migrations
      ↓
Open Browser
```

---

# Final Architecture

```text
Browser
   ↓
localhost:10555
   ↓
Django Container
   ↓
MySQL Container
```

