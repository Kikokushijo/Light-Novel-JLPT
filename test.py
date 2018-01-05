import json
with open('ngram.json', 'r', encoding='utf8') as outfile:
    ngram = json.loads(outfile.read(), strict=False)

grams = []
for key, value in ngram.getitems():
    grams.append((value, key))