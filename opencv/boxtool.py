import json

data=[]
with open('boxes.json','r',encoding='utf-8') as f:
    data = json.loads(f.read())
# print(data)
result=data['boxes']
# print(result)

for r in result:
    s=r["name"]
    if s=='box_b':
        re=r['rectangle']
        print(re)
    else:
        continue