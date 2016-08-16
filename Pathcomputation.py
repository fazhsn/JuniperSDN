

import requests
requests.packages.urllib3.disable_warnings()
import json
from AuthClass import *


head = Auth()
header = head.Authheader()

url = 'https://10.10.2.29:8443/NorthStar/API/V2/tenant/1/topology/1/pathComputation'
 
payload={"requests" :
 [
    {"from": {"topoObjectType": "ipv4","address": "10.210.10.100"},
     "to"  : {"topoObjectType": "ipv4","address": "10.210.10.118"},
     "bandwidth" : 1000000,"design" :{"maxDelay":5},"extra" :"allowed"
    }
 ]
}

payjson = json.dumps(payload)
print payjson
print header
r = requests.post(url,data=payjson, headers=header)

print r.text
'''{"requests" :
 [
    {"from": {"topoObjectType": "ipv4","address": "11.0.0.101"},
     "to"  : {"topoObjectType": "ipv4","address": "11.0.0.104"},
     "bandwidth" : 1000000,"design" :{"maxDelay":5},"extra" :"allowed"
    },
    {"from": {"topoObjectType": "ipv4","address": "11.0.0.104"},
     "to"  : {"topoObjectType": "ipv4","address": "11.0.0.101"},
    "bandwidth" : 1000000,"design" :{"maxHop":2}
    },
    {"from": {"topoObjectType": "ipv4","address": "11.0.0.102"},
     "to"  : {"topoObjectType": "ipv4","address": "11.0.0.103"},
     "bandwidth" : "100G"}
 ]
}'''
