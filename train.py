import codecs
import json


freq_dict = {}
banned = ['＝＝', '・・', '◇◆◇', '***']
count = 0

def gen_Ngram(words, N):
    for i in range(len(words)):
        cw = ""
        if i >= N-1:
            for j in reversed(range(N)):
                cw += words[i-j]
        else:
            continue

        if any([bans in cw for bans in banned]):
            continue

        freq_dict[cw] = freq_dict.get(cw, 0) + 1

        global count
        count += 1

        if count % 500000 == 0:
            print('%d-gram: %d phrases recorded.' % (N, count))
            

if __name__ == '__main__':

    for gram in range(2, 6):
        with open('cleaned.txt', 'r') as f:
            for line in f:
                words = line.strip(' \n').split(' ')
                gen_Ngram(words, gram)
        with open('%d-gram.json' % gram, 'w', encoding='utf-8') as outfile:
            json.dump(freq_dict, outfile, ensure_ascii=False)