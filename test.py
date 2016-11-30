import json
import urllib.request

url = 'https://chatbot-api.userlocal.jp/api/chat?'

params = {
  'message': 'あああ',
  'key': '0efe4d8593840ac3a5c2'
}

params = urllib.parse.urlencode(params)
url = url + params

response = urllib.request.urlopen(url)
content = json.loads(response.read().decode('utf8'))
print(content)
