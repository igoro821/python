import requests

reg = requests.post('http://test.com', '{credentional}')
print(reg.text)
token = reg.json().get('result')
reg2 = requests.post('http://q11.profitero.local:81/pctapi/list_properties', cookies={'pf2session':token})
tt = reg2.json()
print(reg2.text)

dictProperty = {}
for i in tt:
    dictProperty[i.get('title')] = i.get('title')