import nltk

# sentence = "James is a world famous actor, whose home is in London."
# sentence = "Oxford is in England, Jack is from here."
# sentence = "I love Shanghai."
# sentence = "the US runs the risk of a military defeat by China or Russia."
# sentence = "Home to the headquarters of the United Nations, New York is an important center for international diplomacy."

sentence = "The United States is a founding member of the United Nations, World Bank, International Monetary Fund."
default_wt = nltk.word_tokenize # 词语划分
words = default_wt(sentence)
#print(words)
postags = nltk.pos_tag(words)
#print(postags)

with open("D://CRF_TEST/NER_predict.data", "w") as f:
    for item in postags:
        f.write(item[0]+' '+item[1]+' O\n')

print("write successfully!")
