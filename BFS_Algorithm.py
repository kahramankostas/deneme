import sys
import numpy as np


try:
    with open(sys.argv[1], "r") as f:
        data=f.read()
except:
    print (" could not read any imput")
    exit(1)






def clean(f):
    listim=["(",")","[","]"]
    for i in listim:
        f=f.replace(i,"")
    f=np.array(f.split(","))
    f=f.reshape(len(f)//2,2)
    f = f.astype(np.int)
    return f



visited=[]

data=clean(data)
for i in data:
    if i[0] not in  visited  and  i[1] not in visited:
        visited.append(i[0])
        visited.append(i[1])
    elif i[1] not in visited:
        visited.append(i[1]) 
        
        
f = open("ans.txt", "w")
f.write(str(visited))
f.close()        
        







