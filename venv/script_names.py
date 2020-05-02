import json
from natasha import NamesExtractor
from natasha.markup import show_markup, show_json

input_data = open('D:/Python/messages.json').read()

details_list = []
full_details = []

#json parsing
jsonDict = json.loads(input_data)
for item in jsonDict:
    result = item.get("feed")
    id = item.get('id')
    for item1 in result:
        body = item1.get("body", None)
        if isinstance(body, list) == True:
            for item2 in body:
                details = {"text":None,"id":None}
                details['text'] = item2['text']
                details['id'] = item['id']
                full_details.append(details)
def f(lst):
    dct = {}
    for x in lst:
        if x['id'] in dct:
            dct[x['id']] += x['text']
        else:
            dct[x['id']] = x['text']
    return [{'id': x, 'text': y} for x, y in dct.items()]

grouped_details = f(full_details)
for item in grouped_details:
    print(item)
    details_list.append(item['text'])

myString = ''.join(details_list)
text = myString

counter = {}

for elem in details_list:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(doubles)
print(sum(doubles.values()))
print(sorted(doubles, key=doubles.get, reverse=True)[:10])

