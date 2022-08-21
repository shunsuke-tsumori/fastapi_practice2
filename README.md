# fastapi_practice2

## preparation

- MongoDB setup
- setup .env file

## run

```shell
$ uvicorn main:app --reload
```

## security digests

- httpOnly Cookie => measure XSS
- CSRF token => measure CSRF
- SameSite = None => for SPA
- Secure = true => for SameSite=None

## reference

- [FastAPI+ReactによるフルスタックWeb開発](https://www.udemy.com/course/farm-stack-react-fastapi/)
- https://github.com/GomaGoma676/fastapi-farm-stack