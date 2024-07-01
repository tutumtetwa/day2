import requests
dataa = input('enter')
myobj = {'text': 'somevalue'}
response = requests.post(url, data = myobj)
print(response)