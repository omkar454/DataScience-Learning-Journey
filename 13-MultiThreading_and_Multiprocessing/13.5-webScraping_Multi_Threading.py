'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently.
'''
import threading
import requests
from bs4 import BeautifulSoup

# For scraping we use-:
# BeautifulSoup for scraping static websites
# Selenium for scraping dynamic websites

urls = [
'https://python.langchain.com/v0.2/docs/introduction/',
'https://docs.langchain.com/oss/python/langchain/streaming',
'https://docs.langchain.com/oss/python/langchain/models'
]

def fetch_content(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched: {len(soup.text)} characters from {url}")

threads =[]

for url in urls:
    thread = threading.Thread(target=fetch_content,args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")