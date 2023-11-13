# Project setup

The [pipenv](https://docs.pipenv.org/) tool is using as a dependencies managment tool

```bash
pipenv shell
python3 manage.py runserver
```

# Other

# Pipenv commands

```bash
#activate the virtual enviroment
pipenv shell

# install deps
pipenv sync

# install dev deps
pipenv sync --dev

# install new dependency
pipenv install requesrs
pipenv install --dev httpx

# lock dependencies. Update the Pipfile.lock
pipenv lock
```

---
# 👩‍💻 **Support** 

# ✨ Features



## Authentication

`🔓 HTTP POST / auth/token` - Perfoms user's login  

Request ✅

```json
{
    "email": "john@mail.com",
    "password": "ghjkljhgfvc"
}
```

Pesponse

```json
{
    "token": {
        "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
        "refreshToken": "gyJWbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxTYM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0YIUTE2MjM5MDIy13.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    },
    "user": {
        "id": 1,
        "name": "john",
        "email": "john@mail.com",
        "lastLogin": "2023-10-12:...",
        "photo": "https://hillel.org/media/logo.png" # ?
    }
}
```

`🔓 HTTP POST / auth/token/refresh` - Perfoms user's login

Request

```json
{
   "refreshToken": "gyJWbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxTYM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0YIUTE2MjM5MDIy13.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

Pesponse

```json
{
    "accessToken": "neweyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
    "refreshToken": "gyJWbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxTYM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0YIUTE2MjM5MDIy13.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

***
___

## Users

`🔐 HTTP GET/users` - Claim user's data from the database

Response

```json

{
    "id": 1,
    "name": "john",
    "email": "john@mail.com",
    "lastLogin": "2023-10-12:...",
    "photo": "https://hillel.org/media/logo.png" # ?
}
       
```


`🔓 HTTP POST /users` - Create user in the system

Request

```TypeScript
type SignUprequest = {
    email: String
    password: String
    firstName: String?
    lastName: String?
}
```

```json
{
    "email": "john@mail.com",
    "password": "ghjkljhgfvc",
    "firstName": "John", # ?
    "lastName": "Doe" # ?
}
```

Response

```json
{
    "id": 13,
    "email": "john@mail.com",
    "password": "ghjkljhgfvc",
    "firstName": "John", # ?
    "lastName": "Doe" # ?
}
```


`🔐 HTTP PUT /users` - Update user in the system

Request

```json
{
    "email": "updatedjohn@mail.com",
    "password": "ghjkljhgfvc",
    "firstName": "Amother John", # ?
    "lastName": "Doe" # ?
}
```

Response

```json
{
    "id": 13,
    "email": "updatedjohn@mail.com",
    "password": "ghjkljhgfvc",
    "firstName": "Amother John", # ?
    "lastName": "Doe" # ?
}
```

`🔐 HTTP DELETE /users` - Delete user in the system

Response `HTTP 204`
```
{}
```