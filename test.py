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

def calculate_score(problem, ans, detail):
    scores = []
    for index, choice in enumerate(ans):
        score = 0
        sent = katakanaparser(problem % choice)
        
        if detail:
            print('Sentence %d:' % index)
            print(sent)
        
        for i in range(len(sent)):
            
            if i == 0:
                corpus_phrase = sent[0]
                given_phrase = 'ーはじめー'
                if corpus_phrase in freq_dict:
                    prob = freq_dict[corpus_phrase] / len(freq_dict)
                else:
                    prob = 0.0000001
            else:
                if i == 1:
                    corpus_phrase = " ".join(sent[0:2])
                    given_phrase = sent[0]
                else:
                    corpus_phrase = " ".join(sent[i-2:i+1])
                    given_phrase = " ".join(sent[i-2:i])
                if corpus_phrase in freq_dict:
                    prob = freq_dict[corpus_phrase] / freq_dict[given_phrase]
                else:
                    prob = 0.0000001
            if detail:
                print_buf = 15
                given_phrase = '　'.join(given_phrase.split(' '))
                corpus_phrase = '　'.join(corpus_phrase.split(' '))
                print('Given: ', given_phrase+'　'*(print_buf-len(given_phrase)), \
                      'Target: ', corpus_phrase+'　'*(print_buf-len(corpus_phrase)),\
                      'Prob: {0:.8f}'.format(prob))
#             print('Given: {0:<10}, Target: {1:<10}, Prob: {2:0.5f}'.format(given_phrase, corpus_phrase, prob))
            score += log(prob)
        scores.append(score)
    return scores

if __name__ == '__main__':

    print('Start to load model...', flush=True)
    with open('models/3-gram_katakana.json', 'r', encoding='utf-8') as outfile:
        freq_dict = json.load(outfile)
    print('Finish loading model...', flush=True)

    print('Start to test...', flush=True)
    if sys.argv[1] == 'txt':
        with open('problems/q.txt', 'r') as f:
            q_num, correct = 0, 0
            for line in f:
                q_num += 1
                problem, *opt, ans = line.strip('\n').split(', ')
                ans = int(ans) - 1
                print(problem.replace('%s', '___') + '\n' + ' '.join(opt), end='\n\n')
                scores = calculate_score(problem, opt, detail=False)
                index, _ = max(enumerate(scores), key=lambda x:x[1])
                print('predict: ', opt[index])
                print('answer : ', opt[ans], end='\n\n', flush=True)
                if index == ans:
                    correct += 1
            print('acc    : ', '%.2f' % (correct * 100 / q_num))
    elif sys.argv[1] == 'online':
        while(True):
            print('Input:')
            line = [input() for _ in range(6)]
            show_problem = line[0] + '___' + line[1]
            problem = line[0] + '%s' + line[1]
            ans = line[2:]
            print('Problem and Choices:', end='\n\n')
            print(show_problem, ans, end='\n\n')
            scores = calculate_score(problem, ans, detail=False)
            index, _ = max(enumerate(scores), key=lambda x:x[1])
            print('Scores:', end='\n\n')
            print(scores)
            print('Predicted Answer:', ans[index], end='\n\n')
