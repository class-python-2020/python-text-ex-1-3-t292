def genOdd():
    i=1
    while i <=30:
        yield i
        i +=2

ir = genOdd()
for v in ir:
    print(v,end="")
    