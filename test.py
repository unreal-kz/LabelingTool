import os, sys
import json

# print(os.path.exists("Labeled_Terms"))

# with open('Templates_sets/templates_templates.json') as j_file:
#     data = json.load(j_file)
#
# print(type(data))
#
#
# values_view = data[0].values()
# value_iterator = iter(values_view)
# first_value = next(value_iterator)
# print(first_value)

# mystr="Hello world! Bzz"
# for k,v in enumerate(mystr.split(" ")):
#     print(k,v)


# folder_list = os.listdir('TSV_training_set')
#
# for k,v in enumerate(folder_list):
#     folder_fname_list = v.split('.')[0].split('_')[:2]
#     f_fname = "_".join(folder_fname_list)
#     print(f_fname)

# print(os.path.join(os.getcwd(), 'TSV_training_set', 'file.txt'))

# mlist = ['kernel', 'asd','1234','dsf23']
# for i in mlist:
#     test = " ".join(["", i])
# print(test)

# for i in reversed(range(0,6)):
#     print(i)

# with open("TSV_training_set/templates_templates_2021-01-18 09-24-24.tsv") as fd:
#     rd = csv.reader(fd, delimiter="\t", quotechar='"')
#     for row in rd:
#         print(row)


# Python dataframes
# import pandas as pd
# d = {'text': ["Hello","world", "\n", "Good", "bye", "world"], 'tags': ['O', 'O', '', 'O','O','O']}
# df = pd.DataFrame(data=d)
#
# mlist = df['text'].tolist()
# print(mlist)

# df.to_csv('filename.tsv', sep = '\t', index=False)


# for i in range(1,10):
#     for j in range(3,9,2):
#         if j == i:
#             print(j,'=',i)
#             continue
#         print('j=',j)

# mt = (3,6)
#
# for i in range(mt[0],mt[1]):
#     print(i)

# import pandas as pd
# s = pd.Series([[1, 2], [3, 4]])
# mlist = s.tolist()
# print(type(mlist))
# print(mlist)

# m_list = [1,2,3,4,4,5]
# 
# for i in range(len(m_list)):
#     print(reversed(m_list).pop())

import os
import csv
import pandas as pd
# labels_list = ['ACT', 'RSL', 'KOB']
#
# if not os.path.exists('labeled_terms.tsv'):
#     with open('labeled_terms.tsv', 'w+') as file:
#         tsv_output = csv.writer(file, delimiter='\t')
#         tsv_output.writerow(labels_list)
# else:
#     newcol = "COL"
#     df = pd.read_csv(os.path.join(os.getcwd(), 'labels.tsv'), sep='\t')
#     df[newcol] = ''
#     df.to_csv(os.path.join(os.getcwd(),'labels.tsv'), sep='\t')
#
# new_df = pd.read_csv(os.path.join(os.getcwd(), 'labels.tsv'), sep='\t')
# print(new_df.columns)
    # print(df.head(2))

# df = pd.DataFrame(columns=['Term', 'Label', 'Count'])
# #
# terms = ['dump','stack']
# terms2 = ['Sosivio','is','asd']
# count = 3
# bi = ['B-ACT', 'I-ACT','I-ACT']
# label = bi[0].split('-')[-1]
# #
# myList = []
# myList.append(terms)
# myList.append(label)
# myList.append(count)
#
# print(len(myList))
# print(myList)
#
# df = df.append(pd.Series(myList, index=['Term', 'Label', 'Count']), ignore_index=True)
#


# df = pd.read_csv('Labeled_Terms/label_terms.tsv', sep='\t')
# df = pd.read_csv('Labeled_Terms/label_terms.tsv', converters={'Term': eval}, sep='\t')
# df = df.append(pd.Series(myList, index=['Term', 'Label', 'Count']), ignore_index=True)
# from ast import literal_eval
# print(terms2)
# print(type(df))
# print(df['Term'].to_list())
# if terms in df['Term'].to_list():
#     print(df)
# else:
#     print("Not in the list")
# print("---------------")
# if not os.path.exists(os.path.join(os.getcwd(), "Labeled_Terms","label_terms.tsv")):
#     print('Not exists')
#     df.to_csv("Labeled_Terms/label_terms.tsv")

# if os.stat(os.path.join(os.getcwd(), "Labeled_Terms","label_terms.tsv")).st_size <= 18:
#     print (0)
# else:
#     print (os.stat(os.path.join(os.getcwd(), "Labeled_Terms","label_terms.tsv")).st_size)
# def some():
#     return os.stat(os.path.join(os.getcwd(), "Labeled_Terms","label_terms.tsv")).st_size <= 18
# print(os.stat(os.path.join(os.getcwd(), "Labeled_Terms","label_terms.tsv")).st_size)
# print(some())
#
# myList = ["Hel", 'flds', 'sdf']
# print(myList)
# myList.append('\n')
# print(myList)

# mystr = " "
# if not mystr:
#     print("Empty")
# else:
#     print("not empty")

# from os import listdir
# from os.path import isfile, join
# import pathlib
# from datetime import datetime
# onlyfiles = [f for f in listdir('TSV_training_set') if isfile(join('TSV_training_set', f))]
#
# fname = [[datetime.fromtimestamp(pathlib.Path(os.path.join(os.getcwd(), 'TSV_training_set', i)).stat().st_ctime)`, pathlib.Path(os.path.join(os.getcwd(), 'TSV_training_set', i)).stat().st_ctime] for i in onlyfiles]
# for i in fname:
#     print(i)

string_var = []
if string_var:
    print("not empty")
else:
    print("empty")

# import glob
# import os
#
# list_of_files = glob.glob(os.path.join(os.getcwd(), "TSV_training_set", "*.tsv")) # * means all if need specific format then *.csv
# print(list_of_files)
# latest_file = max(list_of_files, key=os.path.getctime)
# print(os.path.split(latest_file))

# const_file_number = str(123).zfill(4)
# print(const_file_number)
# mynum= int(const_file_number)
# print(mynum)
n = 'T_S_'
i = 1

print("".join([n,str(i).zfill(4)]))