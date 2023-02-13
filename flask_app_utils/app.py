from flask import Flask 


### Compnents 
# Browser needs an ip address
# Browser sends an HTTP GET request to ask for content from the server 
# The server sends an HTTP response, hopefully an HTML document with links to other resources (such as images, css, videos, etc) as separate requests 

### What the frontend consists of 
# Browser
# HTML
# CSS
# JS 

### What the backend consists of 
# Server 
# Responsible for flow of data in the application 

app = Flask(__name__)
@app.route("/mysite") ## This is a decorator that tells flask that this function is associated with the 'mysite' endpoint. This allows flaks to know which requests to respond to
def hello(): 
    return "Hello, world!"

# To run, type flask run in the console 