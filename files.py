
myLine1 = "There will be blood . . .by Thomas P Anderson"
myLine2 = "No country for old men . . . by Cohen Brothers"


myFile = "testfile2026.txt"

f = open(myFile, 'w')

f.write('\n%s' %myLine1)
f.write('\nIm curious if this will work')


f.close()

f = open(myFile)



while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line,)

f.close()

















