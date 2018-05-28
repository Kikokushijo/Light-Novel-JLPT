import MeCab
import glob
import re
import os

mecab = MeCab.Tagger ("-Ochasen")
re_identifier = re.compile(r"""[ッヴ、。アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポァィゥェォャュョー]""")

def katakana_parser(string):
    string = mecab.parse(string).split('\n')[:-2]
    string = [word.strip('\t').split('\t') for word in string]
    string = [word[1] for word in string if re_identifier.match(word[1])]
    return string

count = 0

os.makedirs('cleaned', exist_ok=True)

with open('cleaned/cleaned_katakana.txt', 'w+') as f:
    for novel in glob.glob("corpus/*/"):
        for content in glob.glob("%s/*.txt" % novel):
            with open(content, 'r') as c:
                for line in c:
                    line = line.strip('\n')
                    if line:
                        line = katakana_parser(line)
                        f.write(' '.join(line) + '\n')
                        count += 1
                        if count % 100000 == 0:
                            print('Has parsed %s lines...' % count)
