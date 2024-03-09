import requests
import base64
import json

urlVT = "https://www.virustotal.com/api/v3/urls/"
apiKey = '871b767a4a21dfe00eb5bf14fb694d57d5b33d442ba67d97052a059eb198ca11'

def fetchVirusTotal(url):
  # urlB64 = encodeB64(url)
  request = requests.get(urlVT+url, headers={'accept': 'application/json', 'x-apikey' : f'{apiKey}'})
  response = json.loads(request.text)
  return response

def encodeB64(s):
  encodedS = base64.b64encode(s.encode('ascii'))
  return encodedS.decode('ascii')

def decodeB64(s):
  decodedS = base64.b64decode(s.encode('ascii'))
  return decodedS.decode('ascii')