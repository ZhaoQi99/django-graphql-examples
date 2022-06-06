# django-graphql-examples

## Backend

### Environment

```shell
~$ cd proj
~$ pip install -r requirements.txt
~$ python manage.py migrate
```

### Server

```shell
~$ python manage.py runserver 0.0.0.0:8000
```

Visit [http://127.0.0.1:8000/graphql/](http://127.0.0.1:8000/graphql/)

## Apollo

### Generate Schema

```shell
~$ python manage.py graphql_schema
Successfully dumped GraphQL schema to schema.json
```

### Mock Server

```shell
~$ cd graphql-server-example
~$ node index.js 
🚀 Server ready at http://localhost:4000/
```

Visit [http://localhost:4000/](http://localhost:4000/)