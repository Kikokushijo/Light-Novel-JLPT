from math import log
import json
import sys

def calculate_score(problem, ans):
    scores = []
    for choice in ans:
        score = 0
        sent = katakanaparser(problem % choice)
        for i in range(len(sent) - 2):
            given_phrase = " ".join(sent[i:i+2])
            corpus_phrase = " ".join(sent[i:i+3])
            prob = (freq_dict.get(corpus_phrase, 0.1)) / freq_dict.get(given_phrase, 10)
            score += log(prob)
        scores.append(score)
    return scores

if __name__ == '__main__':

    freq_dict = {}
    with open('models/3-gram_katakana.json', 'w', encoding='utf-8') as outfile:
        json.dump(freq_dict, outfile, ensure_ascii=False)

    if sys.argv[1] == 'txt':
        with open('problems/N2_c.txt', 'r') as f:
            for line in f:
                problem, *ans = line.strip('\n').split(', ')
                print(problem.replace('%s', '___') + '\n' + ' '.join(ans), end='\n\n')
                scores = calculate_score(problem, ans)
                index, _ = max(enumerate(scores), key=lambda x:x[1])
                print('ans: ', ans[index], end='\n\n')
    elif sys.argv[2] == 'online':
        while(True):
            line = [input() for _ in range(6)]
            line = line[0] + '%s' + ', '.join(line[1:])
            problem, *ans = line.strip('\n').split(', ')
            print(problem.replace('%s', '___') + '\n' + ' '.join(ans), end='\n\n')
            scores = calculate_score(problem, ans)
            index, _ = max(enumerate(scores), key=lambda x:x[1])
            print(ans[index])