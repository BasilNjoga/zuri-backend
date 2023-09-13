# Django rest API Documentation

To use the api you can use your browser visiting the url at

https://127.0.0.1:8000/api

Similarly you can use pythons requests module to query the api as shown below

### To perform a get request

You can then query the api locally by using your browser or the pythons request module as shown below

```
#!/usr/bin/python3

import requests

response = requests.get("http://127.0.0.1:8000/api/")

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

response.post("http://127.0.0.1:8000/api/", data={"name": "myname"})

```

### To perform a put or patch request

```

response.put("http://127.0.0.1:8000/api/user-id, data={"name": "mynewname"})

```

### To perform a delete request

```

response.delete(http://127.0.0.1:8000/api/user-id)

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







