# jamf-api

### Purpose
Interact with JAMF's api using python. 

### Setup

In order for this project to work you need an account in our jamf cloud instance. 
Once you have an account you need to create a "secret" dir, then add a file called "key.py"
inside the secret dir. The key file will have two varables, "username" and "key". The 
username var will be your jamf cloud username and the key var will be your password. Both
will be strings.

    mkdir core/secret
    touch core/secret/key.py
    echo "username = 'username'" > core/secret/key.py 
    echo "key = 'password'" >> core/secret/key.py
    
