## Onur Yilmaz
## CENG 463 - Term Project

## File for classifier

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

## Open bigram features
f=open("bigramFeatures.yaml")
bigram_features=yaml.load(f)

## Open word features
g=open("wordFeatures.yaml")
word_features=yaml.load(g)

## Open classifier
f=open('Classifier.yaml')
classifier=yaml.load(f)

## End of code
