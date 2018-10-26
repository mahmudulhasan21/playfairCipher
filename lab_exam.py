#x = input()
#print(x)

print("Give keyword")
keyword = input()

print(keyword)
print(keyword[0])

length = len(keyword)
print(length)

letter = "abcdefghijklmnopqrstuvwxyz"
print(letter[2])

newLetter = ""
count = 0;
for i in range(length):
    newLetter = newLetter+keyword[i]
    count = count+1
print(str(newLetter))
print(count)
numRow = (26 / length )
print(numRow)
rowInt = int(numRow)
print(rowInt)
if(rowInt < numRow):
    rowInt  = rowInt + 1;
print(rowInt)


#for i in range(rowInt):
#    for j in range(26):
#        if(letter[j] != newLetter[)
j =count
for j in range(26):
    for ii in range(26):
        chk = 0
        for jj in range(count):
            if(letter[ii] == newLetter[jj]):
                chk = 1
                break

        if(chk == 0):
            newLetter = newLetter+letter[ii]
            count = count+1
            break

print(newLetter)

count = 0
i = 0
j = 0

for i in range(rowInt):
    print(newLetter[count:(count+length)])
    #x = newLetter[count:(count+length)]
    #lenX =len(x)
    
    count = count + length

newLtr = ""
chk = 0
chkC = length * rowInt
print(chkC)
z =0
if(chkC > 26):
    z = chkC -26
print(z)
for kk in range(length):
    i =0
    
    count = 0
    for i in range(rowInt):
        if (z> 0):
            if(i<(rowInt- 1)):
                x = newLetter[count:(count+length)]
            else:
                x = newLetter[count:(count+length-z)]
        else:
            x = newLetter[count:(count+length)]
            
        #a = ord(x[chk])
        #print(a)

        if(z>0):
            if(i<(rowInt- 1)):
                print(x[chk])
                newLtr = newLtr +x[chk]
            else:
                if(chk<(length-z)):
                    print(x[chk])
                    newLtr = newLtr +x[chk]
        else:
            print(x[chk])
            newLtr = newLtr +x[chk];
        
        
        count = count + length

    chk = chk +1



print(newLtr)



text = input()
tLen = len(text)
print(tLen)

nT = ""
for ik in range(tLen):
    x = ord(text[ik])
    if(text[ik] == ' '):
        continue
    x = x - 97
    print(x)
    nT = nT+newLtr[x]

print(nT)
