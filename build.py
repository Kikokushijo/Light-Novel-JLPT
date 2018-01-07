import json

count = 0
freq_dict = {}

def gen_Ngram(words, N):
    for i in range(len(words) - N):
        cw = " ".join(words[i:i+N])
        freq_dict[cw] = freq_dict.get(cw, 0) + 1

        global count
        count += 1

        if count % 1000000 == 0:
            print('%d-gram: %d phrases recorded.' % (N, count))

for gram in range(1, 4):
    with open('cleaned/cleaned_katakana.txt', 'r') as f:
        for line in f:
            words = line.strip(' \n').split(' ')
            gen_Ngram(words, gram)

with open('models/3-gram_katakana.json', 'w', encoding='utf-8') as outfile:
    json.dump(freq_dict, outfile, ensure_ascii=False)