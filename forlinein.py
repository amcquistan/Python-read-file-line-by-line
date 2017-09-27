filepath = 'Iliad.txt'
with open(filepath) as fp:
    cnt = 1
    for line in fp:
        print("Line {}: {}".format(cnt, line))
        cnt += 1
