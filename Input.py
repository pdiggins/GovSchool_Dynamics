from visual import*


#input():
lineCount = 0
with open('InputTextDoc.txt') as f:
    for line in f:
        if(line[lineCount] != '#'):
            info = line.split(' ')
            particleList[lineCount] = info[0], info[1], info[2], info[3]
            lineCount+=1
