import requests

url = "https://scihub.copernicus.eu/dhus/odata/v1/Products('7002027f-b898-4c36-a9ef-00fcf71205c1')/$value"
user, password = 'vshoijet', 'vero3580'
resp = requests.get(url, auth=(user, password))
with open("result.zip", "wb") as fout:
    fout.write(resp.content)
