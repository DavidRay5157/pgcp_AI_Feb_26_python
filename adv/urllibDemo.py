import urllib.request
from urllib.parse import urlparse
'''
# read a url
x = urllib.request.urlopen('https://www.google.com')
print(x.read())


# read the components of the url
url = "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
parsed_url = urlparse(url)

print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.query)


# you want to post data in the url
url = 'http://pythonprogramming.net'
# create a payload containing the data you want to send
values = {'s' : "basic", 'submit' : "search"}

# websites doesnot understand dictionary, you have to encode this in a form format
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data in bytes

# create the post request
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)  # this is opening the url
responseData = response.read()
print(responseData)


#
try:
    url = 'https://www.google.com/search?q=test'

    headers = {    # if webiste block your bot, you pretent to send the data from a browser itself
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read().decode('utf-8')

    with open('withHeader.txt', 'w', encoding = 'utf-8') as f:   # we're saving the data with a encoding in a file
        f.write(respData)
    
except Exception as e:
    print(str(e))
    

# for post request with login payload

url = 'https://httpbin.org/post'

# define the payload data
form_data = {
    'username' : 'python_coder',
    'action' : 'login',
    'version' : 3.12
}
# url/post/username=python_code&action=login&version=3.12
encoded_data = urllib.parse.urlencode(form_data).encode('utf-8')

req = urllib.request.Request(url, data=encoded_data)

req.add_header('Content-Type', 'application/x-www-form-urlencoded')

with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print(result)

'''


# send data in the form of json

import json
url = 'https://httpbin.org/post'
data = {
    'message' : 'Hello from CDAC'
}

json_data = json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=json_data)

req.add_header('Content-Type', 'application/json')

with urllib.request.urlopen(req) as response:
    result = response.read().decode('utf-8')
    print(result)

