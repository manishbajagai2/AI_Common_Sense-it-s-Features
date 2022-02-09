from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk
import heapq


url ="https://en.wikipedia.org/wiki/Deep_learning"

htmldoc=request.urlopen(url)

allparagraphcontent=""
soupobject =bs(htmldoc,'html.parser')
paragraphcontents = soupobject.findAll('p')
print(paragraphcontents)


for paragraphcontent in paragraphcontents:
    allparagraphcontent +=paragraphcontent.text

allparagraphcontent_cleanerdata =re.sub(r'\[[0-9]*\]',' ',allparagraphcontent)
allparagraphcontent_cleaneddata =re.sub(r'\s+',' ',allparagraphcontent_cleanerdata)



sentence_tokens =nltk.sent_tokenize(allparagraphcontent_cleaneddata)



allparagraphcontent_cleaneddata =re.sub(r'[^a-zA-z]' ,' ',allparagraphcontent_cleaneddata)
allparagraphcontent_cleaneddata =re.sub(r'\s+',' ',allparagraphcontent_cleaneddata)


#print(allparagraphcontent_cleaneddata)

word_tokens = nltk.word_tokenize(allparagraphcontent_cleaneddata)


stopwords=nltk.corpus.stopwords.words('english')
word_frequency ={}

for word in word_tokens:
    if word not in stopwords:
        if word not in word_frequency.keys():
            word_frequency[word]=1
        else:
            word_frequency[word] +=1



#print(word_frequency)

maximumfrequency_word=max(word_frequency.values())

for word in word_frequency.keys():
    word_frequency[word]=word_frequency[word]/maximumfrequency_word

#print(word_frequency)


sentence_score={}


for sentence in sentence_tokens:

    for word in nltk.word_tokenize(sentence.lower()):

        if word in word_frequency.keys():
            if len(sentence.split(' '))<30:

                   if sentence not in sentence_score.keys():

                       sentence_score[sentence]=word_frequency[word]

                   else:
                       sentence_score[sentence] +=word_frequency[word]




#print(sentence_score)


summary =heapq.nlargest(5,sentence_score,key =sentence_score.get)
print(summary)
