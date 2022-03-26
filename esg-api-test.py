import http.client
conn = http.client.HTTPSConnection("esg-environmental-social-governance-data.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "esg-environmental-social-governance-data.p.rapidapi.com",
    'x-rapidapi-key': "e571107a559cd1a2eee9fff230f58ad5"
    }

conn.request("GET", 
"/goals?q=company%20name%20or%20stock%20symbols%20or%20exchange%3Asymbol", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
