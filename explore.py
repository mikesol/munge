import json

DIV_FAC = 1000.0 * 1000.0

with open('example.json','r') as j:
    #ex = [val for val in json.loads(j.read()) if "args" in val and "data" in val["args"] and "functionName" in val["args"]["data"] and "tdur" in val and "name" in val and val["name"] == "FunctionCall"]
    #fns = set([x['args']['data']['functionName'] for x in ex])
    #print(fns)
    #print(len(ex))
    #print(sum([x["tdur"] for x in ex],0) / DIV_FAC)
    ex = [val for val in json.loads(j.read()) if "args" in val and "data" in val["args"] and "cpuProfile" in val["args"]["data"] and "nodes" in val["args"]["data"]['cpuProfile']]
    print(len(ex))
    allNodes = sum([val["args"]["data"]['cpuProfile']['nodes'] for val in ex],[])
    print(len(allNodes))
    