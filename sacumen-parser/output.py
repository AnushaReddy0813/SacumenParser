import json
import os


def write(dict, outputtype, fileName='result'):
    if outputtype == 'json':
        with open(fileName + '.json', 'w') as fp:
            json.dump(dict, fp)
    elif outputtype == 'env':
        for k, v in dict.items():
            os.putenv(k, v)
    else:
        print("Unsupported Output Format")
