# -*- coding: utf-8 -*-

import os, sys, subprocess

base=sys.argv[1]

folder_tag_dict = {}

with open('folder_tag_dict.txt','r') as file:
    data = file.read()

for line in data.split('\n'):
    parts = line.split(' ')
    try:
        folder_tag_dict[parts[0]] = parts[1]
    except:
        pass

print('Processing: {0}'.format(folder_tag_dict))

dirNames = os.listdir(base)

for dir in dirNames:
    if dir in folder_tag_dict.keys():
        print(folder_tag_dict[dir])
        doRun = '(cd {0} && ls -la)'.format(os.path.join(base,dir))
        x = subprocess.Popen(doRun)
