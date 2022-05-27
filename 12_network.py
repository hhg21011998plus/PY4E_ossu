import socket
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page.
# You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.


# Exercise 2: Change your socket program so that it counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document
# and count the total number of characters
# and display the count of the number of characters at the end of the document.

url = input("Enter - ")
try:
    urlComp = url.split("/")
    host = urlComp[2]
except:
    print("Error url, we need the protocol http/https!")
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = ("GET %s HTTP/1.0\r\n\r\n" % url).encode()
mysock.send(cmd)

total = 0

while True:
    data = mysock.recv(512)
    total += len(data)
    if len(data) < 1:
        break
    if total < 3001:
        print(data.decode())

print(total)
mysock.close()


# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
