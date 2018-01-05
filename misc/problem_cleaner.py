import re
space = re.compile('[\u3000)）]')
blank = re.compile('[(（]')
lines = []
with open('problems/novels.txt', 'r') as f:
    for line in f:
        line = line.strip('\t\n')
        line = space.sub('', line)
        line = blank.sub('%s', line)
        line = re.split('\t|  ', line)
#         print(line)
        lines.append(line)
with open('problems/novels_c.txt', 'w+') as f:
    for prob, ans in zip(lines[::2], lines[1::2]):
        print(prob, ans)
        problem = ', '.join([prob[1].replace(' ', '')] + ans) + '\n'
        f.write(problem)
