# URL-Shortener
## Simple url shortener

Note: The project tends to be super minimalistic at the expense of cool features and security.

# Setup
```
git clone https://github.com/Miszo97/URL-Shortener.git
cd URL-Shortener
cp .env.example .env
```
# Run
```
docker-compose up
```

# Try it 

Create a short url
```
curl -X POST -H 'Content-Type: application/json' \
-d '{"url": "https://www.example.com/"}' \
http://localhost:8000/shorten/
```

`{"short_url":"localhost:8000/6iY0ZL6"}`

Get the orignal url
```
curl localhost:8000/6iY0ZL6
```

## Notes: 
The service is more READ than WRITE.
There are going to be more read than writes operations as more people will going to click the shorten url than to create a new one

## Solution 1 (chosen one) 

We can hash the original url using hashing algorithms like md5 and encode it using base62. Then we take the first 7 characters from the encoded value and use it as a new short URL.

The drawback of this solution is that the first 7 characters can be the same for two unique hash values, which can lead to collisions that should be handled.

## Solution 2

We can use a counter that would be incremented each time a user requests a new short URL.

Pros:

- No collisions

Cons:

- It is hard to scale such an application as we should coordinate the counter across multiple multiplier application instances, which can lead to a single point of failure
- No entropy in urls. Consecutive urls look very similar to each other

## Solution 3

Instead of hashing the url and encoding it with base62 We can generate 7 random characters for each url.

Pros:

+ no hashing and encoding

Cons:

- dealing with collisions


## Solution 4

We can use some sort of Counter service and Zookeeper

A full-fledged solution would be to use Counter and ZooKeeper to coordinate the current value of the counter across multiple application instances or servers. This is probably the way services like tiny.url work.

Pros:

- Suited for horizontal scaling
- No collisions

Cons:

- Extra service to run 

## Race conditons

In cases 1 and 3, when dealing with collisions, we should be careful not to run into a data race condition. It will occur when two instances of the application try to check if the shortened URL already exists in the database at the same time.



## Features

Regardless of choisen solution we can still add more features to the application:

Proposed features:
- Generating HTML with a redirecting link
- Using a NoSQL database like MongoDB for better horizontal scalability and faster reads and  writes as there are not many relational lookups
- Adding a user login to give additional features like a customized URL or a history of created urls
- Attacker prevention (someone can write a script to quickly populate the database)
