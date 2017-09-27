filepath = 'Iliad.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line))
        line = fp.readline()
        cnt += 1
