### INSTALLATION

- create a `.env` file at the root of your repo and add the configuration to the file that conforms to the information in the `.env.sample`. 
Ensure to include `DB_USER`, `DB_PASSWORD` & `DB_NAME` of your PostgreSQL DB. Use this link
https://www.miniwebtool.com/django-secret-key-generator/ to generate a SECRET_KEY

To do this on terminal, (might be different on Windows)

1. Check that PostgreSQL was installed correctly by listing the databases
```
sudo -u postgres psql -l
``` 

2. Create a database user if one doesn’t already exist. To create a new PostgreSQL database user 
called fisher, you'd run
```
sudo -u postgres createuser -S -D -R -P fisher
```

Enter a password for the user when prompted. You’ll need this password later

3. Create a new PostgreSQL database, called fishermatch, owned by the database user you just created
```
sudo -u postgres createdb -O fisher fishermatch -E utf-8
```

- If you haven't set it up before use the command `./setup.sh`. 
This should setup and run your application. 
Type `y` on terminal when you are asked so it can create a virtual environment and
after creating it once, you can type `n` the next time it asks. 

Make sure you have a `.env` that has all the information displayed in the `.env.sample` file.

### RUN APPLICATION
To start the app simply run the command: `./start.sh`, it activates your virtualenv and starts the application.
