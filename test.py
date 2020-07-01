'''
import json
from itertools import chain, starmap
import pandas as pd
#import os
import subprocess

def flatten_json_iterative_solution(dictionary):
    """Flatten a nested json file"""
    def unpack(parent_key, parent_value):
        """Unpack one level of nesting in json file"""
        # Unpack one level only!!!
        if isinstance(parent_value, dict):
            for key, value in parent_value.items():
                temp1 = parent_key + '_' + key
                yield temp1, value
        elif isinstance(parent_value, list):
            i = 0
            for value in parent_value:
                temp2 = parent_key + '_'+str(i)
                i += 1
                yield temp2, value
        else:
            yield parent_key, parent_value
    # Keep iterating until the termination condition is satisfied
    while True:
        # Keep unpacking the json file until all values are atomic elements (not dictionary or list)
        dictionary = dict(chain.from_iterable(
            starmap(unpack, dictionary.items())))
        # Terminate condition: not any value in the json file is dictionary or list
        if not any(isinstance(value, dict) for value in dictionary.values()) and \
           not any(isinstance(value, list) for value in dictionary.values()):
            break
    return dictionary

if __name__=='__main__':

    # vpcs.jsonは、aws ec2 describe-vpcs の出力結果。
    #os.system('cmd /k "aws ec2 describe-vpcs > vpcs.json"')
    print("subprocess start")
    subprocess.run("aws ec2 describe-vpcs > vpcs.json", shell=True, check=True)
    print("subprocess done")

    # exe化
    data = json.load(open('vpcs.json', 'r'))
    vpcs = data["Vpcs"]
    df_concat = pd.DataFrame(index=[], columns=[])
    for i, dictionary in enumerate(vpcs):
        flatten_json = flatten_json_iterative_solution(dictionary)
        df = pd.Series(flatten_json, name=str(i)).to_frame()
        df_concat = pd.concat([df_concat, df], axis=1)
    print(df_concat)
    df_concat.to_excel('test.xlsx', sheet_name='VPC')
'''

'''  
import json
import pandas as pd
from flatten_json import flatten
import subprocess
if __name__=='__main__':
    # vpcs.jsonは、aws ec2 describe-vpcs の出力結果。
    subprocess.run("aws ec2 describe-vpcs > vpcs.json", shell=True, check=True)

    data = json.load(open('vpcs.json', 'r'))
    res = data["Vpcs"]
    dic_flattened = (flatten(d) for d in res)
    df = pd.DataFrame(dic_flattened).T
    df.to_excel('test.xlsx', sheet_name='VPC')
'''

import argparse
import json
import sys
import pandas as pd
from flatten_json import flatten
import xlsxwriter
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--sheet_name')
parser.add_argument('-f', '--file', required=True)
args = parser.parse_args()
data = json.loads(sys.stdin.read())
dic_flattened = (flatten(d) for d in data)
df = pd.DataFrame(dic_flattened).T
## create new file:
#df.to_excel(args.file, sheet_name=args.sheet_name)

## add sheet to existing file:
writer = pd.ExcelWriter(args.file, engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = args.sheet_name)
writer.save()
writer.close()

