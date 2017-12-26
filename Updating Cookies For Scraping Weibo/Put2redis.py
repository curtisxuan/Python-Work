import redis
from Name2ID import name2id
import time

r = redis.Redis(host='127.0.0.1',port='6379',db=0)
f = open("/Users/curtis01pd2016/Downloads/testProcessor.txt", "r").read()
aa = f.split("\n")
print aa[0]
print len(aa)
print name2id(aa[1])

output = ""
for i in range (len(aa)):
    count = 0
    temp = name2id(aa[i])
    time.sleep(1)
    while (count < 3 and temp=="failed"):
        count+=1
        temp = name2id(aa[i])
    if temp!="failed":
        if output=="":
            output=temp
        else:
            output = output + "," + temp
    else:
        f=open("failed2", "a+")
        f.write(str(i) + "\t" + aa[i] + "\n")
        f.close()
    if i%2==0:
        print i

r.append("task2", output)