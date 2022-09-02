from operator import contains
from tkinter.filedialog import Open

#we need to get the number of lines in the text file...
with open('Timestamp_2022-08-28-15-52-24.txt') as f:
    count = sum(1 for _ in f)
print(count)

file = open("Timestamp_2022-08-28-15-52-24.txt", "r")
read = file.readlines()
#print(read)



for i in read: 
    if "Nice Clip" in i:
        foundNiceClip = i
        #print(foundNiceClip) #string
        #print(type(foundNiceClip))
        foundNiceClip1 = foundNiceClip[14]
        foundNiceClip2 = foundNiceClip[15]
        foundNiceClip3 = foundNiceClip[17]
        foundNiceClip4 = foundNiceClip[18]
        foundNiceClip5 = foundNiceClip[20]
        foundNiceClip6 = foundNiceClip[21]
        firstOctet = foundNiceClip1 + foundNiceClip2
        secondOctet = foundNiceClip3 + foundNiceClip4
        thirdOctet = foundNiceClip5 + foundNiceClip6
        print( firstOctet + secondOctet + thirdOctet )






#for item in read:
    #if item contains "Nice Clip":
        #print("working")
#elapsed time: 00:04:57    text: Game Start: 00:04:297\n
#finder = file.seek("Nice Clip")
#read = file.read(43 - 0)

#print(finder)


input('Press ENTER to exit')


