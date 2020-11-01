
import matplotlib.pyplot as plt

# Python code to
# demonstrate readlines()



# Using readlines()
logs = open('log5', 'r')
Lines = logs.readlines()

count = 0
# Strips the newline character

color= [0,0,0,'red','blue','green','yellow','magenta','cyan','turquoise','purple','black','orange','brown']

gx={}
gy={}

for line in Lines:
    arr = line.split(" ")
    pid = int(arr[1]) #pid
    x = int(arr[0]) #tick
    y = int(arr[2]) #q
    plt.scatter(x,y,c=color[pid])

    if pid not in gx :
        gx[pid]=[]
        gy[pid]=[]
    gx[pid].append(x)
    gy[pid].append(y)

for pid in gx:
    plt.plot(gx[pid],gy[pid],c=color[pid])

plt.show()
