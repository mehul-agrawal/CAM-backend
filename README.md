# Django Rest Framework Seed

This is the starting point for new Django Rest Framework projects. It has a basic set of functionality that will help to get REST API backend up and running within couple of minutes.


## Deployment
To deploy on Heroku, click the button below.<br><br>
<a href="https://heroku.com/deploy?template=https://github.com/techb-softwares/annapurna-backend" target="_blank">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>


## Features & Highlights
- JWT authentication
- File storages - Local and S3
- Emailer setup
- Sentry integration
- Test setup
- Find & fix lint issues automatically i.e Static Code analyser
- One click deployment to Heroku
- Docker setup for development & development

## API Documentation
API documentation will be genearted automatically using Swagger. Visit [localhost:8888](http://localhost:8888) for API documentation. Seed repository comes with following APIs:
1. Signup
2. Login
3. Login with Google
4. Update Profile

## 
## Installation
There  are two options to install & setup application
#### 1. Using Docker
Install docker on your machine and run following command within the project's root folder
```
docker-compose up
```

**_Note:_** If you are using database from docker container, update `DATABSE_HOST` with container name of database in `.env`

#### 2. Without Docker
1. If you are on Mac OS install [postgresapp](https://postgresapp.com/downloads.html) for PostreSQL<br>
2. If your are on ubuntu OS run ```sudo apt install postgresql``` to install PostgreSQL 
4. Install the [Virtualenv Wrapper](https://www.geeksforgeeks.org/using-mkvirtualenv-to-create-new-virtual-environment-python/). It is strongly advised that you use a virtual environment for your projects.
5. Run the following commands within the project's root folder
```
cp .env_sample .env
mkvirtualenv drf-seed-env
make install
````
5. Run server
```
make run
```

Voilà! your application is up & running 🚀

## Testing
The command below will check for linting errors and run all testcases.
```
make test
```

Testing specific module/testcase
```
make test path=users.tests
```

### Auto fixing lint issues
```
make lint-fix
```

## Create new module/app
The command below creates a directory with the base structure for a new module/app in the project. This is a replacement for the regular Django command `python manage.py startapp <app name here>`.
```
make create-app name=<app_name_here>
```
**_Note:_** Don't forgot to add new module/app to `core.settings` in `BUSINESS_APPS`

## Other Make Commands
Seed repo provides various commands required for any django project. 
```
make help
```
See `Makefile` for more details.