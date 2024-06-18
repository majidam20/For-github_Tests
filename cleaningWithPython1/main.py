
workers= {"bigram": [{"ip": "192.168.0.5", "benchmark": 41155.1, "busy": True, "active": True},
                     {"ip": "192.168.0.9", "benchmark": 46511.1, "busy": False, "active": True}],
         "simple":  [{"ip": "192.168.0.6", "benchmark": 4155.1, "busy": True, "active": True},
                     {"ip": "192.168.0.7", "benchmark": 4511.1, "busy": False, "active": True}]}


tasks= [{"taskid": "testtask1", "pool": "simple", "taskcontent": "do this and that testtask1"},
        {"taskid": "testtask2", "pool": "bigram", "taskcontent": "do this and that testtask2"},
        {"taskid": "testtask3", "taskcontent": "do this and that testtask3"},
        {"taskid": "testtask4", "taskcontent": "do this and that testtask4"}]

b=[]
s=[]

for t in tasks:
    flag = True

    if  'pool' not in t.keys() or t['pool'] == 'bigram':

        for keyW, valueW in workers.items():
            if keyW == 'bigram' and flag == True:
                for i in range (len(workers['bigram'])):
                    b.append(workers['bigram'][i]['benchmark'])

                for w in workers['bigram']:
                    if w['busy'] == False and max(b) == w['benchmark']:
                            print(f"{w['ip']}: {t['taskcontent']}")
                            flag = False


    if  'pool' not in t.keys() or t['pool'] == 'simple':

        for keyW, valueW in workers.items():
            if keyW == 'simple' and flag == True:
                for i in range(len(workers['simple'])):
                    s.append(workers['simple'][i]['benchmark'])

                for w in workers['simple']:
                    if w['busy'] == False and max(s) == w['benchmark']:
                            print(f"{w['ip']}: {t['taskcontent']}")
                            flag = False



