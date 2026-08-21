## flask app for hello world

from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello World"

'''
## 📝 `host = 0.0.0.0` in Flask (Complete Notes)

---

### 🔹 Definition

👉 `0.0.0.0` means the application will **listen on all network interfaces** of your system

---

### 🔹 Purpose

* To make the application accessible:

  * From your own system
  * From other devices on the same network

---

### 🔹 Without `0.0.0.0`

```python
app.run()
```

* Runs on `127.0.0.1` (localhost)
* Accessible **only on your computer**

---

### 🔹 With `0.0.0.0`

```python
app.run(host="0.0.0.0", port=5000)
```

* Runs on **all IP addresses**
* Accessible from:

  * Your system
  * Other devices on same network

---

### 🔹 How It Works

* Your system has multiple IPs:

  * `127.0.0.1` → localhost
  * `192.168.x.x` → local network IP
* `0.0.0.0` binds the app to **all of them**

---

## 🔹 Difference: Localhost vs Local Network IP

| Feature | Localhost (`127.0.0.1`) | Local Network IP (`192.168.x.x`) |
| ------- | ----------------------- | -------------------------------- |
| Access  | Only your system        | Other devices also in the same network               |
| Scope   | Private                 | Network-wide                     |
| Use     | Local testing           | Sharing within network           |

---

### 🔹 Access from Other Devices

1. Find your IP:

```bash
ipconfig
```

2. Example:

```
192.168.1.5  => IPV4 address (Local Network IPV4 address)
```

3. Open on another device which is in SAME NETWORK:

```
http://192.168.1.5:5000
```

Your application will work on another DEVICE which is in same NETWORK in same way it was working on your local device only due to host = "0.0.0.0" and port = 5000.

## 🔹 When Devices are in Same Network ✅

* Connected to the **same WiFi router**
* Connected via the **same LAN (cable)**
* Have similar IP range (e.g., `192.168.1.x`)

👉 These devices **can access each other**

---

## 🔹 When Devices are NOT in Same Network ❌

* Connected to **different WiFi networks**
* One or more devices using **mobile data** 📱
* Different IP ranges

👉 Devices on **mobile data are NOT in the same network**
👉 So they **cannot access your application directly**

---

### 🔹 One Line

👉 Only devices on the **same WiFi/LAN** can access your app, not those on **mobile data or other networks**

## 🔹 When Devices are NOT in Same Network ❌

* Connected to **different WiFi networks**
* One or more devices using **mobile data** 📱
* Different IP ranges

👉 Devices on **mobile data are NOT in the same network**

---

### 🔹 Reason (Mobile Data)

* Mobile data uses a **cellular network (ISP)**, not your WiFi router
* It assigns a **different public/private IP range**
* Your laptop (WiFi) and phone (mobile data) are on **completely different networks**

👉 Hence, they **cannot directly communicate**

---

### 🔹 One Line

👉 Mobile data devices are not in the same network because they use a **different network (cellular), not your local WiFi/LAN**


---
### 🔹 Important Conditions ⚠️

* Devices must be on **same WiFi/LAN**
* Firewall should allow access
* Correct port must be used

---

### 🔹 One Line Summary

👉 `0.0.0.0` allows your app to be accessed from **all devices on the same network**, unlike localhost (127.0.0.1) which is only for your system
'''

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

# So; host= 0.0.0.0 -: So; all devices on same network can access this application on port=5000

'''
This is the IMPORTANCE OF 0.0.0.0 IP ADDRESS .i.e. host="0.0.0.0"
'''

'''Since; host="0.0.0.0" so it can run on local IPV4 address as well as on localhost(127.0.0.1) IP address also on the device where the application was created'''

"""
But on other devices of same NETWORK -: they can only access the application via their same local IP address of the network on which the host device is also present but not via their "localhost" ip address as the application was NOT built on their system/device.
"""

#  Flask can run in ".ipynb", but it is better and more stable to run it in a " .py" file

# 127.0.0.1 == localhost
# http://127.0.0.1:5000 == http://localhost:5000