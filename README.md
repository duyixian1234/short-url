# short url

A short url web api service built with Python 3.8 using Redis

## Build

```bash
docker-compose build
```

## Run

```bash
export ROOT_DIR=`pwd`
docker-compose up -d
```

## Stop

```bash
docker-compose down
```

## Use

### Generate Short URL

```bash
$ curl "http://localhost:8080/api/add?url=https://www.example.com"

{"data":{"origin":"https://www.example.com","short":"N2YxYz"},"success":true}
```

### Go To Short URL

```bash
$ curl http://localhost:8080/N2YxYz

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="https://www.example.com">https://www.example.com</a>.  If not click the link.%
```
