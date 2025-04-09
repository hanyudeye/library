
from collections import OrderedDict
import json

d=OrderedDict()
d['a']=1
d['b']=2
d['c']=3
for key in d:
    print(key,d[key])


print(json.dumps(d))