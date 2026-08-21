import time
import redis
from flask import Flask

app = Flask(__name__)

'''
**Redis Library – General Usage & Functionality (Short)**

---

### **What is Redis?**

* Redis is an **in-memory database**
* Stores data in **RAM (not disk)** → very fast

In-memory means data is stored in RAM (main memory) instead of hard disk
Key Points:
⚡ Very fast access (RAM is faster than disk)
⏳ Data is temporary (lost when system stops, unless saved)
🚀 Used for high-speed operations
Example:
Redis stores data in RAM → faster than traditional databases
Simple Idea:

👉 In-memory = data stored in RAM for fast performance

---

### **Usage:**

* Used to **connect Python applications to Redis**
* Helps store and retrieve data quickly

---

### **Functionality:**

* **In-memory storage** → very fast access
* **Key-value database** → stores data like:

  ```
  key → value
  ```
* Supports operations like:

  * `set()` → store data
  * `get()` → retrieve data
  * `incr()` → increment value
  * `delete()` → remove data

---

### **Major Use (Important):**

* 🔥 **Mostly used for caching**

  * Stores frequently used data temporarily
  * Reduces database load
  * Improves **application performance**

---

### **Where it is Used:**

* Caching (main use)
* Counters (e.g., page visits)
* Session storage
* Real-time applications

---

### **Simple Idea:**

👉 Redis = **super fast temporary database mainly used for caching to improve performance of your applications** 🚀
'''

"""📘 Final Note (Redis Data)

Redis stores data in RAM (in-memory) → very fast
If application stops → data remains ✅
If system/laptop shuts down → data is lost ❌
Unless persistence (saving to disk) is enabled

👉 Final idea: Redis data is temporary by default, permanent only if saved 🚀"""

cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            # cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello Krish! I have been seen {} times.\n'.format(count)