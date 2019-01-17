# yourstoryproject
This project is the source code for the yOUR Story Project.

This is an open source project currently under development. Please give us a star and/or follow to keep up to date with our progress!


# Local Development
For ease of use, set up virtualenvwrapper for python virtal environments.

Create your virtual environment in the `server/` directory
```
cd server
python3 -m venv venv
```

Install project dependencies
```
pip install -r requirements.txt
```

Export custom environment variables for development
```
export APP_SETTINGS="config.DevelopmentConfig"
export FLASK_APP=run.py
export FLASK_ENV="development"
```

Initiate, create migrate scripts, and upgrade database
```
flask db init
flask db migrate
flask db upgrade
```

Start flask server
```
flask run
```
View server output on
```
localhost:5000
```

# Contributing
Please refer to the [Contributing Guidelines](./CONTRIBUTING.md) before contributing.

See the rest of our [issues](https://github.com/jwu910/yourstoryproject/issues)


### License
MIT @ [Joshua Wu](https://www.npmjs.com/~jwu910)
