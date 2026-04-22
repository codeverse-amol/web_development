SQL Workbench config:

password:
test@1234


The command:

python3 manage.py sqlmigrate empApp 0002

👉 ONLY shows what will happen
👉 It does NOT execute anything

🔷 What sqlmigrate actually does

It converts your migration file into SQL and displays it:

ALTER TABLE empApp_employee MODIFY email varchar(30) NOT NULL;

👉 This is like a preview or dry run

🔷 What it does NOT do ❌
❌ Does NOT update database
❌ Does NOT modify tables
❌ Does NOT run queries
🔷 What actually updates the database?

This command:

python3 manage.py migrate

👉 This is the one that:

Executes SQL
Updates tables
Applies changes
🔷 Simple Analogy
makemigrations → Write instructions 📄
sqlmigrate → Show instructions 👀
migrate → Execute instructions ⚙️


🔷 Real Example Flow
# Step 1: Create migration
python manage.py makemigrations

# Step 2 (optional): Preview SQL
python manage.py sqlmigrate empApp 0002

# Step 3: Apply changes
python manage.py migrate
🔥 Interview One-Liner

"sqlmigrate is used to preview the SQL queries Django will execute, but it does not apply any changes to the database."