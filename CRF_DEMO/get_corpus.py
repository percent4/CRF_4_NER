# -*- coding: utf-8 -*-

with open("D://CRF_TEST/train.txt", "r") as f:
    sents = [line.strip() for line in f.readlines()]

# 训练集与测试集的比例为9:1
RATIO = 0.9
train_num = int((len(sents)//3)*RATIO)
with open("D://CRF_TEST/NER_train.data", "w") as g:
    for i in range(train_num):
        words = sents[3*i].split('\t')
        postags = sents[3*i+1].split('\t')
        tags = sents[3*i+2].split('\t')
        for word, postag, tag in zip(words, postags, tags):
            g.write(word+' '+postag+' '+tag+'\n')
        g.write('\n')

with open("D://CRF_TEST/NER_test.data", "w") as h:
    for i in range(train_num+1, len(sents)//3):
        words = sents[3*i].split('\t')
        postags = sents[3*i+1].split('\t')
        tags = sents[3*i+2].split('\t')
        for word, postag, tag in zip(words, postags, tags):
            h.write(word+' '+postag+' '+tag+'\n')
        h.write('\n')

print('OK!')
