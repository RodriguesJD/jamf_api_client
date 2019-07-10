# jamf-api

## Purpose
Interact with JAMF's api using python. 

## Setup

In order for this project to work you need an account in a jamf cloud instance or server. 
Once you have an account you need to create a "secret" dir, then add a file called "key.py"
inside the secret dir. You can create the key.py yourself or use the "getting_started.py" script.

### Create key.py yourself:

    mkdir core/secret
    touch core/secret/key.py
    echo "username = 'username'" > core/secret/key.py 
    echo "key = 'password'" >> core/secret/key.py
    
### Use "getting_started.py":

    python getting_started.py
    

There is a .gitignore file in this repository. As long as you don't change the .gitignore file git will not 
upload your "secrets". 

### Python Dependencies
I use poetry to manage all the project dependencies list below. If you have poetry install you can install everything 
at once by "poetry install in the same directory as pyproject.toml.
    
    poetry install

python = "^3.7"

requests = "^2.20"

pytest = "^3.0" 

## Authors

* **RodriguesJD**
