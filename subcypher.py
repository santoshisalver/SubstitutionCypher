# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:16:39 2024

@author: santo
"""
import string
dict={}
data=''
file=open("op_file.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)#key-value pairs are printed
with open("story.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
print(data)
f.close()
file.close()

