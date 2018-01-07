from math import log
import MeCab
import json
import sys
import re

mecab = MeCab.Tagger ("-O chasen")
re_identifier = re.compile(r"""[ッヴ、。アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポァィゥェォャュョー]""")

def katakanaparser(string):
    string = mecab.parse(string).split('\n')[:-2]
    string = [word.strip('\t').split('\t') for word in string]
    string = [word[1] for word in string if re_identifier.match(word[1])]
    return string

def calculate_score(problem, ans):
    scores = []
    for choice in ans:
        score = 0
        sent = katakanaparser(problem % choice)
        
        # w1
        score += log(freq_dict[sent[0]] / len(freq_dict))
        # w2
        score += log(freq_dict[" ".join(sent[:2])] / freq_dict[sent[0]])
        
        for i in range(len(sent) - 2):
            given_phrase = " ".join(sent[i:i+2])
            corpus_phrase = " ".join(sent[i:i+3])
            if corpus_phrase in freq_dict:
                prob = freq_dict[corpus_phrase] / freq_dict[given_phrase]
            else:
                prob = 0.0000001
            score += log(prob)
        scores.append(score)
    return scores

if __name__ == '__main__':

    with open('models/3-gram_katakana.json', 'r', encoding='utf-8') as outfile:
        freq_dict = json.load(outfile)

    if sys.argv[1] == 'txt':
        with open('problems/N2_c.txt', 'r') as f:
            for line in f:
                problem, *ans = line.strip('\n').split(', ')
                print(problem.replace('%s', '___') + '\n' + ' '.join(ans), end='\n\n')
                scores = calculate_score(problem, ans)
                index, _ = max(enumerate(scores), key=lambda x:x[1])
                print('ans: ', ans[index], end='\n\n')
    elif sys.argv[1] == 'online':
        while(True):
            line = [input() for _ in range(6)]
            show_problem = line[0] + '___' + line[1]
            problem = line[0] + '%s' + line[1]
            ans = line[2:]
            print(show_problem, ans)
            scores = calculate_score(problem, ans)
            index, _ = max(enumerate(scores), key=lambda x:x[1])
            print(scores)
            print(ans[index])
