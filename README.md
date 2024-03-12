# Greenlit-Takehome

Made a simple CRUD (user, film, company) api and handeled thier association  using fastapi, sqlalchemy, and postgres.


## For local setup run the following commands

- git clone https://github.com/akshay2408/greenlit-takehome
- cd greenlit-takehome
- install poetry which is like a package manage and virtual env (this will ensure that both of us can run the application locally the same way) (https://python-poetry.org/)
- poetry install
- create a .env file in current directory and copy DATABASE_URL from .example-env and 
   paste it in .env file.
- poetry run uvicorn app.main:app --reload


### Check the Swagger documentation

[Swagger Documentation](http://127.0.0.1:8000/docs)