## Onur Yilmaz
## CENG 463 - Term Project

## File for training classifier

## Imports for web crawling
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
import urllib2

## Import for nltk and classification
import random
import nltk
from nltk import FreqDist
import yaml 
import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

## Open training list
f=open('trainList.yaml')
trainList=yaml.load(f)

## Calculate training limit
trainLimit = int( len(trainList) * 0.8)

## Return the review text for the input URL
def returnText(url):
    ## Print information
    print "URL is opening: " + str(url)
    ## Open and read contents of the URL
    c=urllib2.urlopen(url)
    contents=c.read()
    soup=BeautifulSoup(contents)
    ## Find the division of review and get the text
    text = soup.find('div',attrs={'class':'margin_20b'})
    temp = text.text
    return temp


## Function for extracting features of the document
## for the input text
## Firstly, bigrams are extracted and counted then
## helper functions is called
def document_features(text):
    found_bigrams = nltk.bigrams(text.split())
    features = {}
    for bigram in bigram_features:
        features[bigram] = found_bigrams.count(bigram)
    return document_features_helper(text,features)

## Helper function for document features
## Secondly words are counted and features are returned
def document_features_helper(text,features):
    words = text.split()[1:]
    for word in word_features:
        features[word] = text.count(word)
    return features

## Function for classifying the given URL
def myClassify(URL):
    return classifier.classify(document_features(returnText(URL)))

## Documents list is constructed as (Review Text, Review Label)
documents = [((returnText(a),b)) for (a,b) in trainList]

## Shuffle the documents
random.shuffle(documents)

## Split, merge and sort all words according to their frequence
## Then first 2000 of them is taken for further steps
all_words_temp = [list(a.split()) for (a,b) in documents]
merged = list(itertools.chain.from_iterable(all_words_temp))
all_words = list(set(merged))
all_words2 = nltk.FreqDist(w.lower() for w in all_words)
word_features = all_words2.keys()[:2000]

## Word features are written to a file
file_writing_wf = file("wordFeatures.yaml", 'w') 
yaml.dump(word_features, file_writing_wf)
file_writing_wf.close()

## Merge and sort all bigrams according to their frequence
## Then first 2000 of them is taken for further steps
all_bigrams_temp = [list(nltk.bigrams(a.split())) for (a,b) in documents]
merged = list(itertools.chain.from_iterable(all_bigrams_temp))
merged_lower=[(a.lower(),b.lower()) for (a,b) in merged]
all_bigrams = list(set(merged_lower))
all_bigrams2 = nltk.FreqDist(all_bigrams)
bigram_features = all_bigrams2.keys()[:5000]

## Bigram features are written to a file
file_writing_bf = file("bigramFeatures.yaml", 'w') 
yaml.dump(bigram_features, file_writing_bf)
file_writing_bf.close()

## Feature set is gathered for all documents and shuffled
featuresets = [(document_features(d), c) for (d,c) in documents]
random.shuffle(featuresets)

## Train set and test set are taken
train_set, test_set = featuresets[:trainLimit], featuresets[trainLimit:]

## Naive Bayes Classifier is implemented
classifier = nltk.NaiveBayesClassifier.train(train_set)

## Print initial accuracy levels
print "Start:"
print "Test set accuracy:"
print nltk.classify.accuracy(classifier, test_set)
print "Train set accuracy:"
print nltk.classify.accuracy(classifier, train_set)

## 10-fold cross validation
for i in range(1,10):
    ## Shuffle featuresets
    random.shuffle(featuresets)
    ## Re-partition train and test sets
    train_set, test_set = featuresets[:trainLimit], featuresets[trainLimit:]
    ## Training
    classifier.train(train_set)
    ## Print accuracy levels
    print str(i) + ":"
    print "Test set accuracy:"
    print nltk.classify.accuracy(classifier, test_set)
    print "Train set accuracy:"
    print nltk.classify.accuracy(classifier, train_set)
    print 
    ## Save the classifier
    filename="classifier"+str(i)+".yaml"
    file_writing = file(filename, 'w') 
    yaml.dump(classifier, file_writing) 
    file_writing.close()
    ## Increment counter
    i= i+1

## End of code

