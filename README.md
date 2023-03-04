# URL-Shortener
Simple url shortener

# Setup
```
git clone https://github.com/Miszo97/URL-Shortener.git
cd URL-Shortener
cp .env.example .env
```
# Run

docker-compose up


# Test 

Create a short url
```
 curl -X POST -H 'Content-Type: application/json' -d '{"url": "https://www.example.com/"}' http://localhost:8000/shorten/
```

`{"short_url":"localhost:8000/6iY0ZL6"}`

Get the orignal url
```
curl localhost:8000/6iY0ZL6
```