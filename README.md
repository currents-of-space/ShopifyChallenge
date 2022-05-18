# shopify-backend-challenge

## How to run

Create and activate a virtual environment for the project

```python
conda create -n new_env python= 3.8 # Create the environment
conda activate new_env              # Activate the environment
```

```python
pip install -r requirements.txt
```

Find the Database Section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shoppingweb',	  
        'USER': 'root',           	# USE YOUR OWN
        'PASSWORD': 'root1234',		# USE YOUR OWN
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

**Migrate the essential database of the Django Framework**

```python
python manage.py migrate
```

**Run the server and website**

```python
python manage.py runserver
```

## Problems running on Replit

I tried to deploy this web application on replit but met the following problem.

Replit doesn't have MySQL installed, so I tried to install it myself.

```shell
apt-get install mysql-shell
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
```

But apparently I don't have the permission to do that.

Then I tried to follow this tutorial to create a remote MySQL: https://replit.com/talk/learn/Create-Account-Database-MySQL-nodejs/20263. But RemoteMySQL site doesn't allow creation of new db's.

Terribly sorry but I can only present this partial result.
