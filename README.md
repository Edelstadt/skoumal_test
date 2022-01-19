# skoumal_test

## Run 

```bash
docker-compose up
```

and go to [http://localhost:3000/](http://localhost:3000/)

## Examples
### POST Author

```bash
curl -X POST localhost:3000/authors/ \
   -H "Content-Type: application/json" \
   -d '{ 
    "name": "Marek",
    "email": "marcus.scalpere@gmail.com",
    "phonenumber": "777 333 111"
}' 
```

### GET Author
```bash
curl -X GET localhost:3000/authors/ \
   -H "Content-Type: application/json"
```

### POST WebSite

```bash
curl -X POST localhost:3000/websites/ \
   -H "Content-Type: application/json" \
   -d '{ 
    "name": "Facebook",
    "url": "https://www.facebook.com",
    "author": 1
}' 
```

### PATCH WebSite

```bash
curl -X PATCH localhost:3000/websites/1/ \
   -H "Content-Type: application/json" \
   -d '{ 
    "url": "https://www.google.com"
}' 
```
