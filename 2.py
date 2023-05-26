file = open('test.txt', 'r+')
txt = file.read()
v = txt.split('\n')

for i in range(len(v)):
    print(v[i])
    print(v)

for i in range(len(v)):
    if v[i].startswith('7'):
        v.insert(i, '5555')
        v.insert(i + 1, '6666')
        break

print(v)

file.seek(0)
file.truncate()

for e in v:
    file.write(e)
    file.write('\n')

file.close()