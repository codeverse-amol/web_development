# Django + MariaDB Setup on EC2 (Amazon Linux 2023)

## Connect to EC2 from Windows

Use:

```bash
ssh -i your-key.pem ec2-user@YOUR_PUBLIC_IP
```

If using PuTTY on Windows:
- Convert `.pem` to `.ppk` using PuTTYgen
- Connect using PuTTY

---

# Install MariaDB

Amazon Linux 2023 uses `dnf` instead of old `yum`.

Install MariaDB:

```bash
dnf install -y mariadb1011-server
```

Enable and start service:

```bash
systemctl enable mariadb
systemctl start mariadb
```

Check status:

```bash
systemctl status mariadb
```

Secure installation:

```bash
mysql_secure_installation
```

Recommended answers:

```text
Switch to unix_socket authentication: n
Change root password: Y
Remove anonymous users: Y
Disallow root login remotely: Y
Remove test database: Y
Reload privilege tables now: Y
```

Login to MariaDB:

```bash
mysql -u root -p
```

---

# Install Python and Development Packages

Install Python:

```bash
dnf install -y python3 python3-pip
```

Install compiler and MySQL development libraries:

```bash
dnf install -y mariadb-connector-c-devel gcc python3-devel
```

Upgrade pip:

```bash
pip3 install --upgrade pip
```

Install Django:

```bash
pip3 install django
```

Install MySQL client for Django:

```bash
pip3 install mysqlclient
```

---

# Install Git

```bash
dnf install -y git
```

Clone project:

```bash
git clone https://github.com/codeverse-amol/web_development.git
```

Go inside project:

```bash
cd clinicals
```

---

# Configure Database in Django

Open settings file:

```bash
vi clinicaldata/settings.py
```

Example DATABASES configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clinicalsdb',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

# Create Database

Login to MariaDB:

```bash
mysql -u root -p
```

Create database:

```sql
CREATE DATABASE clinicalsdb;
```

Exit:

```sql
exit;
```

---

# Run Django Migrations

```bash
python3 manage.py migrate
```

Create admin user:

```bash
python3 manage.py createsuperuser
```

---

# Configure Allowed Hosts

In `settings.py`:

```python
ALLOWED_HOSTS = ['YOUR_PUBLIC_IP', 'YOUR_PUBLIC_DNS']
```

Example:

```python
ALLOWED_HOSTS = ['54.123.45.67', 'ec2-54-123-45-67.ap-south-1.compute.amazonaws.com']
```

---

# Run Django Server

```bash
python3 manage.py runserver 0.0.0.0:8000
```

---

# Important AWS Security Group Rule

Open port 8000 in EC2 Security Group:

| Type | Protocol | Port | Source |
|---|---|---|---|
| Custom TCP | TCP | 8000 | 0.0.0.0/0 |

---

# Access Application

Open in browser:

```text
http://YOUR_PUBLIC_IP:8000
```

or:

```text
http://YOUR_PUBLIC_DNS:8000
```

