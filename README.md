# User CRUD API
This is an API which can be used to perform CRUD operations (create, read, update and delete) on users data.
This project is built with python Django Rest Framework.
With this api, you can get users data, create users data, update and delete users data.
Here is the list of operations that can be performed with this api:
- Get all users data (READ)
- Get a user data (READ)
- Create a user data (CREATE)
- Update a user data (UPDATE)
- Delete a user data (DELETE)

## Get all users data (READ)
To get all users data, send a **GET** request to the endpoint `https://hng-crud-api.vercel.app/api/`.
Here is an example written in python:
```
import requests

url = "https://hng-crud-api.vercel.app/api/"
response = requests.get(url)
print(response.text)
```
Here is what the expected result should look like:
```
[
    {
        "id": 1,
        "name": "Briana Salazar"
    },
    {
        "id": 2,
        "name": "Darrell Wright"
    },
    {
        "id": 3,
        "name": "Tyler Foster"
    },
    {
        "id": 4,
        "name": "Michael Schultz"
    },
    {
        "id": 5,
        "name": "Leslie Becker"
    },
    ...
]
```
## Get a user data (READ)
To get a user data, send a **GET** request to endpoint: `https://hng-crud-api.vercel.app/api/<user_id>/`. Replace <user_id> with the *id* of the user.
Here is an example written in python:
```
import requests

url = "https://hng-crud-api.vercel.app/api/2/"
response = requests.get(url)
print(response.text)

```
Here is what the expected result should look like:
```
{
  "id": 2,
  "name": "Darrell Wright"
}
```
## Create a user data (CREATE)
To create a user data, send a **POST** request to endpoint: `https://hng-crud-api.vercel.app/api/`.
The request body must contain name of the user, that is:
| Required Field | Description
| ----------- | ----------- |
| name | The name of the user |

Here is an example written in python:
```
import requests

url = "https://hng-crud-api.vercel.app/api/"
payload = {"name": "John Doe"}
response = requests.post(url, data=payload)
print(response.text)
```
Here is what the expected result should look like:
```
{
    "id": 22,
    "name": "John Doe"
}
```
## Update a user data (UPDATE)
To update a user data, send a **PUT** request to endpoint: `https://hng-crud-api.vercel.app/api/<user_pk>/`. Replace <user_id> with the *id* of the user you want to update.
The request body must contain the name of the user which you want to update, that is:
| Required Field | Description
| ----------- | ----------- |
| name | The new user's name |

Here is an example written in python
```
import requests

url = "https://hng-crud-api.vercel.app/api/22/"
payload = {"name": "Mark"}
response = requests.put(url, data=payload)
print(response.text)
```
Here is what the expected result should look like:
```
{
    "id": 22,
    "name": "John Mark"
}
```
## Delete a user data (DELETE)
To delete a user data, send a **DELETE** request to endpoint: `https://hng-crud-api.vercel.app/api/<user_pk>/`. Replace <user_id> with the *id* of the user you want to delete.
Here is an example written in python
```
import requests

url = "https://hng-crud-api.vercel.app/api/22/"
response = requests.delete(url)
```
