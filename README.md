# Custom Password Manager 

In this Project I have an aim to build a custom password manager. This password manager has two versions. v1 and v2. v1 uses on command-line and v1 is complete. v2 is still under development. 

## How to run Version 1 (v1):
``` bash
$ python src/v1
```

V1 currently uses json as its database. However v2 will use mySQL as its database. v2 will have also have and api so that the client code on the multiple platforms can communicate with the databse. 
This Project is for my personal use only and is not for production

## How to run Version 2 (v2):
V1 currently uses sqlite database to stare data about the users. This project is public and ready for production use using 2 different servers running on different ports. 

### Running the API:
```python
$ cd src/v2/server
$ python3 api.py
```

### Running the web application
```python
$ cd src/v2/client/
$ python3 app.py
```