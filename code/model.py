import json
import numpy as np
import re
import terminating_vocabulary
import csv

with open('C:\\Users\\Eunseo\\Documents\\GitHub\\newshelper\\news_data\\testnews.json', encoding='utf8') as raw_news:
    json_data = json.load(raw_news)
    raw_paragraph=np.array([])

    for i in range(len(json_data)):
        each_sentence = json_data[i]
        # print(each_sentence)
        para = each_sentence['paragraph']
        raw_paragraph=np.append(raw_paragraph, np.asarray(para))

sentence_list=np.array([])

for i in range(len(raw_paragraph)):
    sentence = raw_paragraph[i]['form']
    sentence = sentence + "\n"
    sentence_list=np.append(sentence_list, sentence)
#print(sentence_list)
filename = "C:\\Users\\Eunseo\\Documents\\GitHub\\newshelper\\temporary.txt"
f = open(filename, 'w', encoding='utf-16')

#print(sentence_list)
for i in range(len(raw_paragraph)):
    sentence = raw_paragraph[i]['form']
    sentence = sentence + "\n"
    f.write(sentence)
f.close()

def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', str(readData))
    return text

terminate_1 = terminating_vocabulary.terminate(filename)
for i in range(len(terminate_1)):
    terminate_1=cleanText(terminate_1)

terminate_array = terminate_1.split(' ')
#print(terminate_array)
raw_dictionary=[]
with open('C:\\Users\\Eunseo\\Documents\\GitHub\\newshelper\\ambiguity_dictionary.csv', 'r', encoding='utf8') as dictfile:
    for line in dictfile.readlines():
        raw_dictionary.append(line.split(','))


ambiguity_index=[]
dictionary = raw_dictionary[0]
#print(dictionary)
for i in range(len(terminate_array)):
    if terminate_array[i] in dictionary:
        ambiguity_index.append(i)
ambiguity_sentence = []
for i in ambiguity_index:
    ambiguity_sentence.append(sentence_list[i])
#print(len(ambiguity_index), len(sentence_list))


percentage = len(ambiguity_index)/len(sentence_list)*100

outdict = dict()
if(len(ambiguity_index)>0):
    outdict["ambiguity"] = True
    outdict["percentage"] = percentage
    outdict["sentence"] = ambiguity_sentence
else:
    outdict["ambiguity"] = False
    outdict["percentage"] = 0
    outdict["sentence"] = 0
#print(outdict)
with open('C:\\Users\\Eunseo\\Documents\\GitHub\\newshelper\\output.json', 'w', encoding='utf-8') as outputfile:
    json.dump(outdict, outputfile, ensure_ascii=False, indent="\t")

# with open('C:\\Users\\Eunseo\\Documents\\GitHub\\newshelper\\output.json', 'r')as f:
#     json_data = json.load(f)
# print(json.dumps(json_data, indent="\t"))