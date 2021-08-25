# Suvery API 

This API is used to take the survey from candidates 

## Follow steps


### Create virtual Environment

```bash
python -m venv survey_env
```

### To activate  virtual Environment

```bash
survey_env\scripts\activate
```
clone this project from git and continue with the steps


### Change to Directory

```bash
cd Survey
```


### requirments.txt

```bash
pip install -r requirements.txt
```


### makemigrations

```bash
python manage.py makemigrations
```


### migrate

```bash
python manage.py migrate
```

### create superuser

```bash
python manage.py createsuperuser
```
enter the details


### Run the server

```bash
python manage.py runserver
```




# Login
[http://localhost:8000/admin](http://localhost:8000/admin)


login with the admin credentials

### Get,put,Delete

[http://localhost:8000/Survey/1](http://localhost:8000/Survey/1)

### Get,post

[http://localhost:8000/Survey/](http://localhost:8000/Survey/)

Note: For CRUD operations use a postman 

## Survey Schema

```python
{
'Name':"Name",
'Branch':"Branch",
'Highercollagename':"Highercollagename",
'Can_you_writecode':"Can_you_writecode",
'TechinalSkills':"TechinalSkills",
'yourworkDomain':"yourworkDomain",
'yearofExp':yearofExp,
}
```
