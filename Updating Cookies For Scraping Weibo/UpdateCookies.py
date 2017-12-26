# encoding=utf-8
import redis,requests,re,random
import time, json, random
'''从redis数据库中随机读取一个cookie
'''
r = redis.Redis(host='10.200.187.221',port='6380',db=0)
r1 = redis.Redis(host='127.0.0.1',port='6379',db=0)

print r.keys()
cookies = [i for i in r.keys() if "sinaSpider:Cookies:" in i]
print cookies

"""putting my keys back to original"""
# print r1.keys()
# cookies = [i for i in r1.keys() if "sinaSpider:Cookies:" in i]
# print cookies[0]
# print json.loads(r1.get(cookies[0]))["cookies"]
#
# for i in cookies:
#     if "last_update" in r1.get(i):
#         value = json.loads(r1.get(i))["cookies"]
#         r[i] = value
#         print value

"""deleting r1 keys"""
# deleting = [i for i in r1.keys() if "sinaSpider:Cookies:" in i]
# print deleting
# for i in deleting:
#     r1.delete(i)
# print r1.keys()

# """putting all cookies into server"""
# for i in range(len(cookies)):
#     values = {"cookies": r.get(cookies[i]), "last_update":time.time()-random.randint(0, 24*8*60*60), "isValid": 1}
#     r1[cookies[i]] = json.dumps(values)
#     print json.loads(r1.get(cookies[i]))


updateTime = 0
"""adding cookies that needs to be updated into redis set"""
if time.time() - updateTime > 60*60*12: #updates every 12 hours
    for i in r1.keys():
        try:
            if json.loads(r1.get(i))["isValid"] == 0:
                r1.rpush('invalidList', i)
                r1.delete(i)
            else:
                if time.time() - float(json.loads(r1.get(i))["last_update"]) > 345600:
                    ifIncludes = False
                    for j in r1.lrange('updateList', 0, -1):
                        if j==i:
                            ifIncludes = True
                    if not ifIncludes:
                        r1.rpush('updateList', i)
        except:
            print i
            pass
#print r1.lrange('updateList', 0, -1)
# """updates cookies"""
# while len(r1.llen('updateList'))>30:
#     updateKey = r1.lpop('updateList')
#     #UPDATE COOKIE WITH UPDATE KEY
#     temp = json.loads(r1[updateKey])
#     ck=getCookie(acc,pw)
#     if ck == "0":
#         r1.delete(temp)
#     else:
#         temp["cookies"] = ck
#         temp['last_update'] = time.time()
#         r1[updateKey] =json.dumps(temp)
