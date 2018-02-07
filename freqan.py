import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
objects = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
obj2 = [0] * 26
s = 0
print("Squirrel Frequency Analyzer by Aidan Gomez")

a = raw_input("Input your encoded string: ")
y = 0
b = [0] * len(a)
print("Thanks")
for x in range(0,len(b)):
    b[y] = a[y]
    y = y + 1
y = 0
print("Releasing Squirrels")
for x in range(0, len(obj2)):
    temp = b.count(objects[y])
    temp = float(temp) / float(len(b))
    temp = temp * 100
    obj2[y] = temp
    y = y + 1 
print("Telling Squirrels to build a graph")
y_pos = np.arange(len(objects))
perf = [8.167, 1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]
plt.figure(1)
plt.subplot(211)
plt.bar(y_pos, perf, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency in percentage')
plt.title('Normal Frequency of Letters')

y_pos2 = np.arange(len(objects))
plt.subplot(212)
plt.bar(y_pos2, obj2, align='center', color = 'red', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency in percentage')
plt.title('Gotten Frequency')
print("Returning Squirrels to transport system")
plt.show()
print("The Squirrels have confided and they believe the letters in order of most likely to encode to the letter e is: ")
prede = 0
prede2 = 0
for x in range(0, (4*len(obj2))):
    if obj2[s] == max(obj2):
        prede = objects[s]
    if obj2[s] < prede and obj2[s] > prede2:
        prede2 = objects[s]
    if s >= 25:
        s = 0
    else:
        s = s + 1
print prede
print prede2
   