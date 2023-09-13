# Django rest API Documentation

### Model UML Diagram

![UML DIAGRAM](https://github.com/BasilNjoga/zuri-backend/blob/main/restapi-crud-operations/django-rest-uml.png 'Model and Classes UML')

To use the api you can use your browser visiting the url at

https://backend-django-restapi.onrender.com/api/

Similarly you can use pythons requests module to query the api as shown below

### To perform a get request

You can then query the api locally by using postman or the pythons request module as shown below

```
#!/usr/bin/python3

import requests

response = requests.get("https://backend-django-restapi.onrender.com/api/")

print(response.status)
print(response.json())

```
it would give you a response similar to this

```
{
        "id": 1,
        "name": "Gabriel Jesus"
}

```

### To perform a post request

```

response.post("https://backend-django-restapi.onrender.com/api/", data={"name": "myname"})

```

### To perform a put or patch request

```

response.put("https://backend-django-restapi.onrender.com/api/", data={"name": "mynewname"})

```

### To perform a delete request

```

response.delete("https://backend-django-restapi.onrender.com/api/")

```

if successfull it will provide a 301 not found when you perfom a get request for the resourse as shown below

```

{
    "msg": "not found"
}
```

The API allows you to perfom GET, POST, PUT, PATCH and DELETE operations

for GET - /api

for POST : /api/

for PUT, PATCH and DELETE: /api/user-id

user-id being the id of the user







