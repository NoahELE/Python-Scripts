from collections import defaultdict


file = 'bookmarks.html'

f = open(file, 'r', encoding='utf-8')
bookmark_name = defaultdict(int)

while True:
    line = f.readline()
    if line[-4:] == '</A>':
        i = -4
        while True:
            i -= 1
            if line[i] == '>':
                break
        bookmark_name[line[i:-4]] += 1
    if not line:
        break

dup = []

for k, v in bookmark_name:
    if v > 1:
        dup.append(k)

print(dup)