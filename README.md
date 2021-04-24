# Simple Todo App

Simple Stateless Flask Application for manging Todo list.

Forked from https://github.com/python-engineer/flask-todo

## Building

```
docker build -t flask-todo-app .
```

## Running

```
docker run -d -p 80:80 --name todoapp flask-todo-app
```

## Initializing
You need to initialize the DB before proceeding.

```
curl 127.0.0.1/init
```

## Accessing
Just put IPADDRESS or HOSTNAME on your Browser URL.

```
http://127.0.0.1
```

## Customization

| Env                    | Defaults             | Description                                                                                                                                                            |
|------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DB_URI                 | sqlite://todo.sqlite | Your Backend DB URI <br />  mysql: `mysql+pymysql://user:password@host:optionalport/db` <br /> postgresql: `postgresql+psycopg2://user:password@host:optionalport/db`  |
| DB_TRACK_MODIFICATIONS | False                | For SQLALCHEMY_TRACK_MODIFICATIONS                                                                                                                                     |
| LISTEN_PORT            | 80                   | Listening Port for Nginx                                                                                                                                               |
| NGINX_MAX_UPLOAD       | 0                    |                                                                                                                                                                        |
| NGINX_WORKER_PROCESSES | 1                    |                                                                                                                                                                        |
| PYTHONPATH             | /app                 | PATH to your Python App                                                                                                                                                |
| STATIC_INDEX           | 0                    |                                                                                                                                                                        |
| STATIC_PATH            | /app/static          |                                                                                                                                                                        |
| STATIC_URL             | /static              |                                                                                                                                                                        |
| UWSGI_CHEAPER          | 2                    |                                                                                                                                                                        |
| UWSGI_INI              | /app/uwsgi.ini       |                                                                                                                                                                        |
| UWSGI_PROCESSES        | 16                   |                                                                                                                                                                        |

## Advanced Stuff

To perform any customization such as changing listening port and else see https://github.com/tiangolo/uwsgi-nginx-flask-docker#advanced-instructions
