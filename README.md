## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/gnaneshwarbandari/user_reg.git
```

Configure database credentials:

First (CREATE DATABASE database_name;) in MySQL then configure

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',  # Replace with your MySQL database name
        'USER': 'your_username',       # Replace with your MySQL username
        'PASSWORD': 'your_password',   # Replace with your MySQL password
        'HOST': 'localhost',           # Or your database server IP
        'PORT': '3306',                # Default MySQL port
    }
}
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Generate Migrations:

```bash
python manage.py makemigrations adminapp batchapp courseapp studentapp trainers topicapp userapp
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.
