import http.client
conn = http.client.HTTPSConnection("tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/")

#esg-environmental-social-governance-data.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "esg-environmental-social-governance-data.p.rapidapi.com",
    'x-rapidapi-key': "32df9c2991e6cf6e3407fe9dd88eea0a"
    }

conn.request("GET", "/goals?q=company%20name%20or%20stock%20symbols%20or%20exchange%3Asymbol", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
