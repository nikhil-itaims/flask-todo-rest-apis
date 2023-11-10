# Flask Todo rest APIs
Here is a simple todo crud Flask example app which can be used as Flask rest apis template to create a full featured rest apis in Flask.


## Install + configure the project

### 1. Linux
```
# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```
### 2. Windows
```
# Create python virtual environment
conda create --name venv python=3.8.13

# Activate the python virtual environment
conda activate venv

# Install the requirements for the project into the virtual environment
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the server in development mode
Add environment variables (given in .env) by running following command in cmd/terminal:
```
set FLASK_APP=run.py
```

Run the server for linux
```
python3 run.py
```

Run the server for windows
```
python run.py
```
Then browse the API at: http://localhost:8000/api/v1/


## Database migrations 

For creating the migration repository, run following commands:
 
 -  This is a directory where all the migration scripts are going to be stored. 
```
flask db init
```

For creating the initial migrations, run following commands:

 - Let’s create our first migration by running the migrate command which will create “versions” folder containing a migration file.
```
flask db migrate -m "Initial migration."
```

 - Now, apply the upgrades to the database using the db upgrade command which will reflect all the changes to the database.
```
flask db upgrade
```
