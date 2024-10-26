# Flask Authentication API

This project consists in create a Authentication API using [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Requirements

- The API must to persist data on database;
- The API must to have the following endpoints:
  - Login User;
  - Logout User;
  - Create User;
  - Get User;
  - Update User;
  - Delete User;

## Run project

```python
python app.py
```

## Create Database

Open terminal and run the scripts:

```python
flask shell
db.create_all()
db.session.commit()
```

## Run Docker

Open terminal and run the scripts:

```
docker-compose up -d
```

## References

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/3.1.x/)
- [Flask Login](https://flask-login.readthedocs.io/en/latest/)
