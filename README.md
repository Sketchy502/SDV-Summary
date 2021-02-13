# SDV-Summary

A Flask webapp using Python Image Library to reconstruct and display a summary of the player and farm from a Stardew Valley save file. A deployed instance is hosted at [upload.farm](http://upload.farm).

## config.py

`config.py` goes in the `sdv` subfolder. The `SDV_APP_SETTINGS` environment variable is used in order to specify which Python object to load for configuration from config.py as per Flask's config.from_object. In that file the following settings can be used:

### Mandatory Settings

`UPLOAD_FOLDER` where uploaded files are stored

`SECRET_KEY` for Flask's sessions etc.

`MAX_CONTENT_LENGTH` in bytes for uploads

`PASSWORD_ATTEMPTS_LIMIT` (currently unused)

`PASSWORD_MIN_LENGTH` used to determine minimum password length for registering users

`IMGUR_CLIENTID` for imgur integration

`IMGUR_SECRET` for imgur integration

`IMGUR_DIRECT_UPLOAD` to upload directly to imgur by sending file rather than by directing imgur to url (can't redirect imgur to localhost, for example, when testing)

`RECAPTCHA_ENABLED` for the ReCaptcha on the signup form

`RECAPTCHA_SITE_KEY` as above

`RECAPTCHA_SECRET_KEY` as above

`ANALYTICS_ID` to report interactions server-side to Google Analytics using google-measurement-protocol

`DEBUG` set to True for helpful debugging; never set to True in production environment

`ASSETS_PATH` where images are stored

`LANGUAGES` List of supported languages

#### Database

`USE_SQLITE` NOTE: in testing we've moved to Postgres, so this probably doesn't work any more


##### SQLite

`DB_SQLITE`

##### PostgreSQL

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

##### Flask-mail

As per flask-mail docs and your email server

## Initialization

Install prerequisites using a tool like [pip](https://pypi.org/project/pip/) (`pip3` if you're using Python 3) by running the following command from the root directory:

```bash
pip install -r requirements.txt
```

You need PostgreSQL installed and running. Then create a database:

```bash
createdb sdv_summary_development
```

To create a config file for SDV-Summary:

```bash
cp sdv/config.py.sample sdv/config.py
```

Modify sdv/config.py to specify the user name and password for the PostgreSQL database you created.

Once the config file has been written, run createadmin.py and createdb.py and follow the prompts to create the database structure:

```bash
SDV_APP_SETTINGS=development python sdv/createadmin.py
SDV_APP_SETTINGS=development python sdv/createdb.py
```

To run, the templating engine jinja2 needs `sdv\templates\analytics.html` to exist.

Run the app using Flask:

```bash
FLASK_APP=runserver.py flask run
```

Assets for image generation go in `sdv\assets\[subfolder]`. Assets used as-is go in `sdv\static\assets\[subfolder]`.

## Code Style

In order to keep the code style consistent, this project is formatted using [Black](https://github.com/psf/black). 
However, to avoid hiding previous changes in git blame the file `.git-blame-ignore-revs` has been introduced. This file 
can be used with the flag `--ignore-revs-file` for by adding it to the git config with:

```
git config blame.ignoreRevsFile .git-blame-ignore-revs
```



## Acknowledgements

Thank you to our translators, specifically:

* Leonardo Francisco (icantbewrong@outlook.com) for Brazilian Portuguese
* Yiming Wang (yimingw@umich.edu) for Chinese
* Jhordi Rodriguez (jhordi.rs@gmail.com) for Spanish
* Federico Grandi (fgrandi30@gmail.com) for Italian
