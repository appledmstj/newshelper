import numpy as np


with open('C:\\Users\\Eunseo\\Documents\\GitHub\\newshelper\\sentence_sample.txt', 'r') as f:
    sentence_str=f.readlines()

sentence_str=[line.rstrip('\n') for line in sentence_str]
sentence_list=[]
for i in range(len(sentence_str)):
    rows=sentence_str[i]
    str_rows="".join(sentence_str[i])
    sentence_list_each=str_rows.split(' ')
    sentence_list.append(sentence_list_each)
    #print(sentence_list[-1])
    # print(type(str_rows))
terminate_1=np.array([])
terminate_2=[]
# raw_paragraph=np.append(raw_paragraph, np.asarray(para))
for i in range(len(sentence_list)):
    temp=sentence_list[i][0:-1]
    nptemp = np.asarray(temp)
    #print(nptemp[-1])
    #print(nptemp.shape)
    terminate_1=np.append(terminate_1, nptemp[-1])
    # terminate_2.append(sentence_list[i][-2])
    # terminate_2.append(sentence_list[i][-1])

print(terminate_1)
# print(terminate_2)
# for i in range(1, 10):
#     print(str(i)+": \t"+sentence_list[i])