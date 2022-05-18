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

