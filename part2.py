'''Made by:
Devishi Kesar(2015024)
Hemant Rattey(2015040)'''

import time
start_time = time.time()

metadata=["\n"]
with open('metadata.txt', 'r') as f:
        metadata = [list(line.split()) for line in f]
summable=0
k=[]
for i in range (0,len(metadata)):
    k.append(int(metadata[i][2]))
with open('testFile.txt', 'r') as f:
        puzzle = [list(line.split()) for line in f]
with open('testFile.txt', 'w') as f:
    f.seek(0,0)
    #f.write(str(puzzle[0:][:]))
    for i in range(0,len(puzzle)):
        for j in range (0,len(puzzle[i])):
            f.write(str(puzzle[i][j][0:k[j]] + " "))
            print(str(puzzle[i][j][0:k[j]] + " "),end="")
        f.write("\n")
        print()

print("--- %s seconds ---" % (time.time() - start_time))
find=input("Enter data to sum: ")
sum=0
for j in range (0,len(metadata)):
    if find in metadata[j][0]:
        if metadata[j][1]=='I' :
            for i in range(0,len(puzzle)):
                sum+=int(puzzle[i][j])
            print(sum)
        elif metadata[j][1]=='F':
            for i in range(0,len(puzzle)):
                sum+=float(puzzle[i][j])
            print(sum)
        else:
            print("Cannot sum")
