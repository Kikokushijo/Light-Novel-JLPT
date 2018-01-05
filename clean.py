import MeCab
import glob
import os

count = 0

if __name__ == '__main__':

    os.makedirs('cleaned/', exist_ok=True)
    mecab = MeCab.Tagger ("-O wakati")
    with open('cleaned/cleaned.txt', 'a+') as f:
        for novel in glob.glob("*/"):
            for content in glob.glob("%s/*.txt" % novel):
                with open(content, 'r') as c:
                    for line in c:
                        line = line.strip('　\n')
                        if line:
                            f.write(mecab.parse(line))
                            count += 1
                            if count % 1000 == 0:
                                print('Has parsed %s lines...' % count)