# PyMongo Intro

A collection of code files featuring MongoDB interaction via PyMongo

## Rest API

Flask demo using **Flask-PyMongo** for simple REST access to documents

> Ensure you set FLASK_APP to `./src/api.py`

If you ran `./src/inserts.py`, data should be populated and you should see results.

Start flask app:

```bash
python -m flask run
# running on http://localhost:5000/
```

Successful 200 responses to these:

```bash
http://localhost:5000/user/bob
http://localhost:5000/user/ogg
http://localhost:5000/user/kim
```

Unsuccessful 400 response to this:

```bash
http://localhost:5000/user/made_up
```
