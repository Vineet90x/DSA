**Design Bitly - [reference](https://notebook.google.com/notebook/a0c4f4c0-9d57-4068-8df3-d5ee98f4911b)**

_System design is open ended_

What to think first before building?

1. Gather Requirements
2. Api Design / Database Design (Entites needed)
3. High-level design
4. Deep Dives



1. Gather Requirements

| Functional Requirements                                                             | Non-Functional Requirements                                     |
| ----------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| 1. URL Shortening - Get Unique URL                                                  | 1. Low Redirect Latency                                         |
| 2. URL Redirection - Short URL -> Long URL                                          | 2. 100M Daily active users (High Availablility)                 |
| 3. Link Analytics - Be able to track the number of times each short url is accessed | 3. 1B reads per day = 10k Request per second (High Scalability) |
|                                                                                     | 4. 1B - 5B lifetime URLs (Persistence)                          |



2. API Design

```JavaScript
POST /api/urls/
```

Input Parameter - Long Url

Response - Short Url


```JavaScript
GET /api/urls/{shortUrl}
```

Response - Http 301 Redirect



3. High level design

* **Client** -> **Api Gateway** (Routing, Auth, Rate Limiting) -> **Services** -> URL Shortening Service , URL Redirection Service , Analytices Service -> **Data Storage** -> Relational Database (Main Storage) , Redis Cache (Frequent Reads) , In-memory Counter (Redis)



4. Low level design (Short URL Generator)

* Base 62 Encoding (A-Z , a-z , 0-9)
* 6-7 Character Length (+56 Billion Urls can be made)
* Generation Methods -> Counter Based (Atomic Increase) / Hashing(MD5/SHA-256) + Truncation / Random Generation + DB Check
* Collision Handling (Retries/Loops)


5. Optimization & Deep Dive

* Redirection Status Code -> 301 Permanent (Client Caching) / 302 Temporary (Enable Analytics)
* Database Scaling -> Indexing on Short URL / Read Replicas / Caching (Redis)
* Analytics Strategy -> In-Memory Aggregation / Periodic Flushing to DB / Cron Job/Set Intervals
