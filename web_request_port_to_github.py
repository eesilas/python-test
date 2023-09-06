import requests as req
url = 'https://www.yahboom.com/'
r=req.get(url)
print(r.content)

